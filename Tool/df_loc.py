import pandas as pd
import argparse
import os
# input template
# python df_loc.py --dataPath ./Ristsu1_25 --start_data_row 71
# setting up argument
parser = argparse.ArgumentParser()
parser.add_argument('--dataPath',   type=str,   help='target data path')
parser.add_argument('--outputPath',   type=str,  default='./',   help='output of result data path')
parser.add_argument('--start_data_row',   type=int , help='pick up a starting row')

# assign variable to each argument
args = parser.parse_args()
df_path = args.dataPath
outpath = args.outputPath
start_row = args.start_data_row

# start of project
if __name__=='__main__':
    gyro = pd.read_csv(df_path)
    
    gyro_norm = gyro.copy()
    
    
    # due to the position of the sensor, correct the data to right direction
    gyro_norm['temp']= gyro_norm['z-axis (deg/s)']
    gyro_norm['z-axis (deg/s)']=gyro_norm['x-axis (deg/s)']*(-1)
    gyro_norm['x-axis (deg/s)']=gyro_norm['temp']
    
    # Normalization
    for k in ['x-axis (deg/s)','y-axis (deg/s)','z-axis (deg/s)']:
        m,s= gyro_norm[k].mean(),gyro_norm[k].std()
        if s ==0:
            gyro_norm[k]=gyro_norm[k]-m
        else:
            gyro_norm[k]=(gyro_norm[k]-m)/s
    # Cut the data         
    elapse = gyro_norm['elapsed (s)'][start_row]
    gyro_norm['elapsed (s)']=gyro_norm['elapsed (s)']-elapse
    
    gyro_norm = gyro_norm.iloc[start_row:].reset_index().drop(columns='index')

    
    #gyro_correct[['x-axis (deg/s)','y-xis (deg/s)','z-axis (deg/s)']].plot()
    filename = os.path.basename(df_path).split('.')[0]
    output_file = os.path.join( outpath, filename)+'_norm.csv'
    gyro_norm.to_csv(output_file)

    # output file for ELAN
    output_elan = os.path.join( outpath, filename)+'_elan_norm.csv'
    gyro_elan = gyro_norm[['elapsed (s)','x-axis (deg/s)','y-axis (deg/s)','z-axis (deg/s)']]
    gyro_elan.to_csv(output_elan,header=False,index=False)
    

    