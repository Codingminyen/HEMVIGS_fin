(for %%i IN (./files/*.avi) DO @echo file ./files/%%i) >videolist.txt
ffmpeg -safe 0 -f concat -i videolist.txt -c copy -an output.mp4



