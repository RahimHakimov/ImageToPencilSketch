import cv2

image = cv2.imread(input("Image location: "))

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original image", cv2.resize(image, (image.shape[1]//4, image.shape[0]//4)))

cv2.imshow("Gray image", cv2.resize(gray_image, (image.shape[1]//4, image.shape[0]//4)))

cv2.waitKey(0)
