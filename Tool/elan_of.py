import pandas as pd
import numpy as np
import argparse
import os

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
    
    '''
    # due to the position of the sensor, correct the data to right direction
    gyro_correct['temp']= gyro_correct['z-axis (deg/s)']
    gyro_correct['z-axis (deg/s)']=gyro_correct['x-axis (deg/s)']*(-1)
    gyro_correct['x-axis (deg/s)']=gyro_correct['temp']
    '''
    for k in ['pose_Rx','pose_Ry','pose_Rz']:
        tmp_arr=of_norm[k].to_numpy().flatten()
        of_diff[k]=np.diff(tmp_arr)    
        m,s= of_diff[k].mean(),of_diff[k].std()
        if s ==0:
            of_diff[k]=of_diff[k]-m
        else:
            of_diff[k]=(of_diff[k]-m)/s

    # output file for ELAN
    filename = os.path.basename(df_path).split('.')[0]
    output_elan = os.path.join( outpath, filename)+'_elanof.csv'
    of_diff['timestamp']=of_norm['timestamp'][:-1]
    gyro_elan = of_diff[['timestamp','pose_Rx','pose_Ry','pose_Rz']]
    gyro_elan.to_csv(output_elan,header=False,index=False)
    
 

 