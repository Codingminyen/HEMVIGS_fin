
FOR %%f IN (C:\Users\lumin\python_CODE\Dicomo_tools\face_track\demo\*.mp4) DO (
start  /wait/b python face_track.py --videoPath %%f 

)

