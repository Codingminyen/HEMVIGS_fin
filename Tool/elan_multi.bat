FOR %%f IN (C:\Users\lumin\python_CODE\MS_thesis\Tools\raw_imu\*.csv) DO (
start  /wait/b python elan.py --dataPath %%f --outputPath C:\Users\lumin\python_CODE\MS_thesis\Tools\elan_imu

)