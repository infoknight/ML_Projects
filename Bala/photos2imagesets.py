#!/usr/bin/env python3
#Script to read the Photo directories, split them each into Training_Set and Test_Set and save them accordingly

import os
import shutil

# Read the photos from the specified path
#dirIn = input("Enter the Path to Image Folders : ")
#dirPath = "photos/" + dirIn                     #Path where the Photos are Saved in respective directories
dirPath = "photos/"                              #Path where the Photos are Saved in respective directories
list_photodirs = os.listdir(dirPath)                   #List the Photo Directories
print("[+] List of Photo Directoreis Found : %s" %list_photodirs)

#Create the Required Folders for Storing the Segregated Training & Test Images
for photo_dir in list_photodirs:
    # creating folders to store Training & Test sets
    images4trg = "image_sets/training_set/" + photo_dir + "/"
    images4test = "image_sets/test_set/" + photo_dir + "/"

    ##Creating folder for Training Set
    if not os.path.exists(images4trg):
        try:
            os.makedirs(images4trg)
            print("[*] Creating Folder to Store Training Set : %s" %images4trg)

        # if not created then raise error
        except OSError:
            print ("[-] Error: Creating directory %s" %images4trg)
    
    ##Creating folder for Test Set
    if not os.path.exists(images4test):
        try:
            os.makedirs(images4test)
            print("[*] Creating Folder to Store Test Set : %s" %images4test)

        # if not created then raise error
        except OSError:
            print ("[-] Error: Creating directory %s" %images4test)

#Read the Photo Directories One-by-One and Split Photos to Training & Test Sets
#for photo_dir in list_photodirs:
    photo_dir = dirPath + photo_dir + "/"
    num_of_photos = len(os.listdir(photo_dir))          #Count the total number of photos in all the directories

    #Training : 80% ; Test : 20%
    for_trgsets = round(num_of_photos * 0.8)
    for_testsets = round(num_of_photos * 0.2)
    print("[*] Total Photos : %d" %num_of_photos)
    print("[*] 0.8 of Trg Set : %d" %for_trgsets)
    print("[*] 0.2 of Test Set : %d" %for_testsets)

    # Defining folders to store Training & Test sets
    #images4trg = "image_sets/training_set/" + photo_dir + "/"
    #images4test = "image_sets/test_set/" + photo_dir + "/"

    count = 0
    total_images_trgset = 0
    total_images_testset = 0

    for img in os.listdir(photo_dir):                   #Read the Images from the directories
        if count < for_trgsets:                        #Copy the Images to Training Set if the %count is less than Training Set %
            src = photo_dir + img
            try:
                shutil.copy(src, images4trg)
                #print("Copying Images to Training Set.....")
                total_images_trgset = count + 1
            except:
                print("Error")
        else:
            src = photo_dir + img
            try:
                shutil.copy(src, images4test)
                #print("Copying Images to Test Set....")
                total_images_testset = count - total_images_trgset + 1
            except:
                print("Error")
        count = count + 1                              #Increment the Count to segregate the Training & Test set
    
    print("[+] Number of Images Copied to Training Set : %d" %total_images_trgset)
    print("[+] Number of Images Copied to Test Set : %d" %total_images_testset)

    count = 0
    total_images_trgset = 0
    total_images_testset = 0


