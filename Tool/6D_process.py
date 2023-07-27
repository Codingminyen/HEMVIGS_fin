import pandas as pd
import numpy as np
import argparse
import os

from scipy import signal



# setting up argument
parser = argparse.ArgumentParser()
parser.add_argument('--dataPath',   type=str,   help='target data path')
parser.add_argument('--outputPath',   type=str,  default='./',   help='output of result data path')
#parser.add_argument('--start_data_row',   type=int , help='pick up a starting row')

# assign variable to each argument
args = parser.parse_args()
df_path = args.dataPath
outpath = args.outputPath
#start_row = args.start_data_row

# start of project
if __name__=='__main__':

        
    gyro = pd.read_csv(df_path)
    
    of_norm = gyro.copy()
    of_diff= pd.DataFrame()
    of_filter= pd.DataFrame()
    of_final= pd.DataFrame()
    of_keys =['x','y','z']    
    
    # due to the position of the sensor, correct the data to right direction    

    for k in ['x','y','z']:
        tmp_arr=of_norm[k].to_numpy().flatten()
        of_diff[k]=np.diff(tmp_arr)    
        m,s= of_diff[k].mean(),of_diff[k].std()
        if s ==0:
            of_diff[k]=of_diff[k]-m
        else:
            of_diff[k]=(of_diff[k]-m)/s

    # setting filter parameter

    # set up parameter
    cut_off= 2.5# cut off frequency (Hz)
    fs = 25#sampling frequency
    nyq = 0.5 * fs  # Nyquist Frequency
    digit_cutt_freq =  cut_off/nyq # the normalization required in scipy's digital filter


    # Filter
    b, a = signal.butter(4, digit_cutt_freq,'low',analog=False)
    # Filter for 

    of_filter= of_diff.copy()
    #of_filter= of_norm.copy()
    of_filter[of_keys[0]] = signal.filtfilt(b, a, of_filter[of_keys[0]])
    of_filter[of_keys[1]] = signal.filtfilt(b, a, of_filter[of_keys[1]])
    of_filter[of_keys[2]] = signal.filtfilt(b, a, of_filter[of_keys[2]])



    of_final[of_keys[0]]=-of_filter[of_keys[2]]
    of_final[of_keys[1]]=of_filter[of_keys[0]]
    of_final[of_keys[2]]=of_filter[of_keys[1]]     






            
    leng = len(of_diff['x'])
    count = 0
    timestamp=[]
    while count<leng:
        timestamp.append(0.04*count)
        count+=1
        
    timestamp= np.array(timestamp)
    # output file for ELAN
    filename = os.path.basename(df_path).split('.')[0]
    output_elan = os.path.join( outpath, filename)+'_gyro.csv'
    of_final['timestamp']=timestamp[:]
    gyro_elan = of_final[['timestamp','x','y','z']]
    gyro_elan.to_csv(output_elan,header=True,index=False)
    print("Successful.")
    print("The file is saved at ", gyro_elan)
    



