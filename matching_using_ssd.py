import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import time

def show_image(img,c):
    bg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(bg)

    face = cv2.imread('crop.jpeg')
    face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)

    plt.imshow(face)
    height, width, channels = face.shape
    methods = ['cv2.TM_CCORR_NORMED']
    for x in methods:
        bg_copy = bg.copy()
        method = eval(x)
        result = cv2.matchTemplate(bg_copy,face,method)

        min_va, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc 
        top_right = (top_left[0]+width,top_left[1])
        bottom_right = (top_left[0]+width,top_left[1]+height)
        bottom_left = (top_left[0],top_left[1]+height)
    
        cropped_contour= bg[top_left[1]:top_left[1]+height, top_left[0]:top_left[0]+width]
        image_name= "output_shape_number_" + str(c+1) + ".jpg"
        path = 'images1/Lighting_Condition2_images/pink_65_side'
        name = os.path.join(path , image_name)
        cv2.imwrite(name, cropped_contour)
        readimage= cv2.imread(name)
        hsv_img = cv2.cvtColor(readimage, cv2.COLOR_BGR2HSV)
        #cv2.imshow('Image', readimage)
        cv2.imshow('Image', hsv_img)
        brightness_avg = hsv_img[...,2].mean()
        cv2.waitKey(0)
    return brightness_avg

images_list = []
directory = 'images1/Lighting_Condition2_images/pink_65_side'
count = 0
referenceTime = time.time() + 14400 - 1657670000
startTime = time.monotonic()
with open('LED_top_view/Lighting_2_FSR_data/pink_65_side_intensity.csv', 'w') as csvfile:

    for filename in os.listdir(directory):
        #print(filename)
        if os.path.isfile(directory + '/' + filename):

            bg = cv2.imread(directory + '/' + filename)
            #print(bg)
            new_filename = filename.replace('.png', '', 1)
            current_brightness = show_image(bg, count)
            incrementTime = round(time.monotonic()-startTime,1)
            currentTime = referenceTime + incrementTime
            csvfile.write("{},{}\n".format(current_brightness,new_filename))
            count += 1
            images_list.append(bg)

