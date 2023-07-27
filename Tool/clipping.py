import argparse
import os
from moviepy.editor import *



# setting up argument
parser = argparse.ArgumentParser()
parser.add_argument('--dataPath',   type=str,   help='target data path')
parser.add_argument('--start',   type=float,  default=0.0,   help='starting time ')
parser.add_argument('--end',   type=float,  default=0.0,   help='end time ')
parser.add_argument('--outputPath',   type=str,  default='./',   help='output of result data path')
#parser.add_argument('--start_data_row',   type=int , help='pick up a starting row')

# assign variable to each argument
args = parser.parse_args()

df_path = args.dataPath
time_start = args.start
time_end = args.end
outpath=args.outputPath

if __name__== '__main__':
    
    clip = VideoFileClip(df_path)
    if time_end<=0.0:
        time_end=None
    clip = clip.subclip(time_start,time_end)
    
    
    filename = os.path.basename(df_path).split('.')[0]
    output_file = os.path.join( outpath, filename)+'_trim.mp4'
    clip.write_videofile(output_file,fps=25)
    
    
    

