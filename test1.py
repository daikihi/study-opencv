import cv2

# load from disk
original_image = cv2.imread('ocr_test/private_sample02.jpg')
# original_image = cv2.imread('test-001.jpeg')

# convert to gray color image from original image
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# display converted image
cv2.imshow('Gray Image', gray_image)

# listen user key pless 
cv2.waitKey(0)

# and then close window
cv2.destroyAllWindows()
