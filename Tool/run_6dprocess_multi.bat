FOR %%f IN (C:\Users\lumin\python_CODE\MS_thesis\Tools\6d_imu\*.csv) DO (
start  /wait/b python 6D_process.py --dataPath %%f --outputPath C:\Users\lumin\python_CODE\MS_thesis\Tools\6d_processed

)
