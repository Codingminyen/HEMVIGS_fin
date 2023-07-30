# HEMVIGS_fin <br>
################################################# <br>
Hello this is MinYen ~ :)))) <br>
Just leave some description of the code here.<br>
################################################# <br>

If you want to use HemViGS, please follow the flow decribed as follow.
1. Apply **Face_track module** in "dicomo tools" to cropped the raw video.
2. Apply **6DRepNet module** in "dicomo tools" to generate Euler angle data of subject's face.
3. Apply **run_6dprocess_multi.exe** in "Tools" to generate gyro data from Euler angle data.
	This also include standardization, axis swapping, and low pass filtering.
	If you want to change anything, please modify the "6D_process.py" file.


# Dicomo_Tools\Face_track module description <br>

These tools are for head pose estimators.  
- 'face_track'
	Crop the face of subject from the raw video. <br>
 	Before start to use this exe, please get the model parameter "sfd_face.pth" from googledrive or contact sensei Arakawa.  
	At dir: Dicomo_Tools\face_track\model\faceDetector\s3fd
	- `run_multi.exe`:
		Start cropping all video datas in `demo` folder.  
		This will generate a folder with the same name of the video file in `results` folder.  
		In the generated folder, there are four sub-folders.  
		- pyavi
		- pycrop
		- pyframes
		- pywork
		I only used files in pycrop. In pycrop, the avi file is the cropped video.  
		
	NOTE: Sometimes facetrack will split single video into different video files.  
	In this case, please use the `concat_run.exe` in the `attach_video` folder.  
	The `concat_run.exe` concatenate videos in the `files` folder into single videos using `ffmpeg` lib. (Please ensure that the name of videos in the `files` folder should be in sequence.)  
	It first generate a `video.txt` which includes the name of each video files in "files" folder, and perform concatenation.

# Dicomo_Tools\6DRepNet module <br>	
- `6DRepNet-master`
	Before start to use this exe, please get the model parameter "6DRepNet_300W_LP_AFLW2000.pth" from googledrive or contact sensei Arakawa.  
	At dir: Dicomo_Tools\6DRepNet-master
	- `run_multi.exe`:
		Process every videos in `video` folder, and generate Euler angle data of the subject's facing angle.

# Tools\Generate gyroscope data
- `clipping.py`: 
	This code is applied to clip the video file.
- `df_loc.py`:
	This is used for remove the unwanted raw, mainly for the synchronization of video and real sensor data.

- `run_6dprocess_multi.exe`: Generate gyro data from euler data
	Driver for `6D_process.py`. This exe file transforms the Euler angle data from 6DRepNet to Gyroscope data.
	Standardization(line 37), axis swapping to meet the real sensor data(line 67), and low pass filter (2.5Hz)(line 47) are included.
	The exe is written in batch file.  
	`--datapath` is the path of the folder directory of input files.  
	`--outputpath` is the place to store output result.  
	Please modify it as you wish. 

You might need to visualize the data in Elan to find how the axis of generated data should be changed to meet your sensor, 
please use the following code to make the data fit elan software's requirement.
https://archive.mpi.nl/tla/elan
- `elan_multi.exe`:
	Driver for `elan.py`. This exe file can process multiple files of "real sensor data" at once to generate the file that suitable for elan software.
	Standardization included.



- `run_elan_6D_multi.exe`:   # Process gyro data to fit Software Elan requirement.
	Driver for "elan_6D.py". This exe file can process multiple files of generated sensor data at once to generate the file that suitable for elan software.
	Standardization included.

Folders in google drive

- `6d_imu`: generated euler data

- `6d_processed`: generated gyroscope data

- `*_elan`: data for elan software

- `*_label`: data with label


- `raw_imu`: raw imu data without going through any process.
# Requirments
I believe it should work only with the environment that meets `requirements_6Drepnet.txt `.   
The code was built originally in Windows.  
However, the `.exe` files are simple batch code for automation and should be easy to be modified.  
I apologize for the inconvenience for users who try to apply it on other systems.  

Face_track- requirements_face_track.txt   
This directly applied the pytorch model published in github by joonson.  
https://github.com/joonson/syncnet_python  
```
torch>=1.4.0
torchvision>=0.5.0
numpy>=1.18.1
scipy>=1.2.1
scenedetect==0.5.1
opencv-contrib-python
python_speech_features
```

6DRepNet- requirements_6Drepnet.txt  
This directly applied the pytorch model published in github by Thorsten Hempel.  
https://github.com/thohemp/6DRepNet  
```
matplotlib >= 3.3.4
numpy >= 1.19.5
opencv-python >= 4.5.5
pandas >= 1.1.5
Pillow >= 8.4.0
scipy >= 1.5.4
torch >= 1.10.1
torchvision >= 0.11.2
```


# Publication
```
@article{minyen2022study,
  title={A study on estimating the accurate head IMU motion from Video},
  author={MinYen, Lu and ChenHao, Chen and others},
  journal={マルチメディア, 分散, 協調とモバイルシンポジウム 2022 論文集},
  volume={2022},
  pages={918--923},
  year={2022}
}
```




