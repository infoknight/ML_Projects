#!/usr/bin/env python3
#This script extracts photos from the videos.
#This would be helpful in getting adequate number of photos for trainng the CNN algorithm. 
#It would also be easy for the parents to upload the videos online rather than uploading hundreds of photos.
#
#
#Prerequisities :
#Create a folder in the videos directory and name it uniquely. Multiple videos uploaded of the same child should be saved in the same#directory. Future versions may append a hash to the parent folder.
#Use this script to extract photos from the videos.
#The output of this script will be stored in the images directory inside a folder named as per the previous steps.

# Importing all necessary libraries
import cv2
import os

#**************************************Part-1 : Extract Photos From Videos**********************************************************#
# Read the videos from the specified path
folder_name = input("Please Name Your Folder : ")
video_path = "videos/" + folder_name
print("Video Path : %s" %video_path)

list_videos = os.listdir(video_path)             #List the videos uploaded
print("List of Videos Found : %s" %list_videos)

# creating a folder to store photos
photos_path = "photos/" + folder_name
print("Path to Save Extracted Photos : %s" %photos_path)

if not os.path.exists(photos_path):
    try:
        os.makedirs(photos_path)
        print("Creating Folder to Store Photos : %s" %folder_name)

# if not created then raise error
    except OSError:
        print ("Error: Creating directory %s" %photos_path)

#Sequence Number to be appended to the extracted photos
currentframe = 0

#Iterate through the videos one-by-one
for i in list_videos:
    vid_file = video_path + "/" + i
    print("Analysing Video : %s" %vid_file)
    cam = cv2.VideoCapture(vid_file)

    while(True):

        # reading from frame
        ret,frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = i.split(".")[0]                      #Cut the video file name from the extension
            name = name + str(currentframe) + '.jpg'    #Rename the photos
            print ('Creating...' + name)

            # writing the extracted images after sampling
            if (currentframe % 10) == 0:                #Save only one in 10 images
                full_name = photos_path + "/" + name              #Full name along with the path
                cv2.imwrite(full_name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            currentframe = 0
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()

#**************************************Part-2 : Train CNN Classifier to Classify Photos*********************************************#



#**************************************Part-3 : Create a Trained Model in a New File and Predict the Results************************#
