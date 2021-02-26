# author: Rahim Hakimov (ramhakimov@niuitmo.ru)
__author__ = "Rahim Hakimov"
__email__ = "ramhakimov@niuitmo.ru"

import cv2  # importing cv2 library

image_name = input("Image name: ")  # input of image name

image = cv2.imread(image_name)  # reading the image

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # creating the GRAY version of our image

blurred_image = 255 - cv2.GaussianBlur(255 - gray_image, (21, 21), 0)  # blurring the inversion of GRAY image

pencil_sketch_image = cv2.divide(gray_image, blurred_image, scale=256.0)  # creating the PENCIL SKETCH of our image

cv2.imwrite("pencil_sketch_" + image_name,
            pencil_sketch_image)  # write the result to file named "pencil_sketch_"+image_name
