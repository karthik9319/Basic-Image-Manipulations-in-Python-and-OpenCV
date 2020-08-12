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
