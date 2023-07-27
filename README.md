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


# Face_track module description <br>

These tools are for head pose estimators.  
- 'face_track'
	Crop the face of subject from the raw video. <br>
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

# 6DRepNet module <br>	
- `6DRepNet-master`  
	- `run_multi.exe`:
		Process every videos in `video` folder, and generate Euler angle data of the subject's facing angle.

# Generate data
- df_loc.py:
	This is used for remove the unwanted raw, mainly for synchronizing video and real sensor data.
- elan_multi.exe:
	Driver for "elan.py". This exe file can process multiple files of real sensor data at once to generate the file that suitable for elan software.
	Standardization included.

- run_6dprocess_multi.exe: # Generate gyro data from euler data
	Driver for "6D_process.py". This exe file transforms the Euler angle data from 6DRepNet to Gyroscope data.
	Standardization, axis swapping to meet the real sensor data, and low pass filter (2.5Hz)included.

- run_elan_6D_multi.exe:   # Process gyro data to fit Software Elan requirement.
	Driver for "elan_6D.py". This exe file can process multiple files of generated sensor data at once to generate the file that is suitable for elan software.
	Standardization included.

- clipping.py: 
	This code is applied to clip the video file.

Folders

- *_elan: data for elan software

- *_label: data with label

- 6d_imu: generated gyro data

- raw_imu: raw imu data without going through any process.






