# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:28:28 2022

@author: Lutz
"""

from os import listdir
import os
import cv2
import time
print('input directory')
video_directory=input()
video_directory=str(video_directory)
onlyfiles = [f for f in listdir(video_directory) if f.endswith('.mpg') ]

print('Input Trial duration')
trial_duration=input()
trial_duration=int(trial_duration)

frame_list=[]
fps_list=[]
for i in onlyfiles:
    file=video_directory + i
    start = time.time()
    videoCapture=cv2.VideoCapture(file)
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    end_time= round(frames)/round(fps)
    start_time=end_time-trial_duration
    file_name_input=i
    file_name_output=i[:-4]+'_trimmed'+'.mp4'
    terminal_input='ffmpeg -ss ' + str(start_time) +' -i ' + i + ' -c:v libx264 ' + file_name_output 
    os.system(terminal_input)
    stop = time.time()
    duration = stop-start
    print(fps)
    print(frames)
    print('It took ' + str(duration) + ' sec to trimm the video' + i)
    del videoCapture
