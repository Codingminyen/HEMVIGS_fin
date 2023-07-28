import glob
import os

# Import everything needed to edit video clips 
from moviepy.editor import *


video_path = r"C:\Users\lumin\python_CODE\Dicomo_tools\face_track\change_fps_space"
work_list = os.listdir(video_path)
for w in work_list:
    vid = os.path.join(video_path, w)
    clip = VideoFileClip(vid)
    new_clip = clip.set_fps(25)
    new_clip.write_videofile(w)
# loading video dsa gfg intro video 
#clip = VideoFileClip("dsa_geek.mp4") 
     
# getting only first 5 seconds
#clip = clip.subclip(0, 5)
  
# new clip with new fps
#new_clip = clip.set_fps(5)
  
# displaying new clip
#new_clip.ipython_display(width = 360)