import cv2

image = cv2.imread('jurassic-park-tour-jeep.jpg')
print(image.shape)
cv2.imshow("original", image)
cv2.waitKey(0)

#resizing image to 100 pixels
r = 100.0/ image.shape[1]
dim = (100, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation= cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)

#calculate center and rotate the image 
(h, w) = image.shape[:2]
center = (w/2 , h/2)

m = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, m, (w,h))
cv2.imshow("rotated", rotated)
cv2.waitKey(0)

#cropping image 
cropped = image[70:170, 440:540]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)

#saving cropped image to disk
cv2.imwrite("cropped.jpg", cropped)
print("Done")