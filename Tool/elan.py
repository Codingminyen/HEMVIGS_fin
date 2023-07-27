import pandas as pd
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
    
    
    # due to the position of the sensor, correct the data to right direction
    """
    gyro_correct['temp']= gyro_correct['z-axis (deg/s)']
    gyro_correct['z-axis (deg/s)']=gyro_correct['y-axis (deg/s)']
    gyro_correct['y-axis (deg/s)']=gyro_correct['temp']    
    gyro_correct.drop(columns=['temp'], inplace=True)
    """
    
    
    # output file for ELAN
    filename = os.path.basename(df_path).split('.')[0]
    output_elan = os.path.join( outpath, filename)+'_elan.csv'
    gyro_elan = gyro[['elapsed (s)','x-axis (deg/s)','y-axis (deg/s)','z-axis (deg/s)']].copy()
    gyro_keys = ['x-axis (deg/s)','y-axis (deg/s)','z-axis (deg/s)']
    for k in gyro_keys: 
        m,s= gyro_elan[k].mean(),gyro_elan[k].std()
        print(s)
        if s ==0:
            gyro_elan[k]=gyro_elan[k]-m
        else:
            print('s is non zero')
            gyro_elan[k]=(gyro_elan[k]-m)/s
    print(f'After standarized, the deviation on {k} becomes {gyro_elan[k].std()}')
    
    
    
    
    gyro_elan.to_csv(output_elan,header=False,index=False)
    
 

 