import cv2

def hsv_brightness(image):
    readimage=cv2.imread(image)
    hsv_img = cv2.cvtColor(readimage, cv2.COLOR_BGR2HSV)
    #cv2.imshow('Image', readimage)
    cv2.imwrite('hsv_1.jpg', hsv_img)
    brightness_avg = hsv_img[...,2].mean()
    return brightness_avg
