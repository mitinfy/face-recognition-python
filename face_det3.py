import cv2 #pip install opencv-python
# Load the cascade
face_cascade = cv2.CascadeClassifier('face_detector.xml') #68000 lines of algorithm
# Read the input image
img = cv2.imread('test2.jpg')
# Detect faces
faces = face_cascade.detectMultiScale(img, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0),6) #BGR (0,0,0)... (255, 255, 255)

#show on screen begins
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Export the result
cv2.imwrite("face_detected.png", img) 
print('Successfully saved')
