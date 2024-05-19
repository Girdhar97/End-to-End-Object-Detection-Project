import os
import cv2
import time
import uuid  #unique name  unique ID for the images

IMAGE_PATH = "CollectedImages"  #folder name

labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']  # more labels could be added later if needed

number_of_images = 5 # no. of images for one particular label

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)

    #open camera 
    cap = cv2.VideoCapture(0)  # capture variable
    print(f"Collecting images for {label}")
    time.sleep(3)

    for imgnum in range(number_of_images):
        ret,frame = cap.read()
        imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF==ord('q'):  # camera will stop when 'Q' from the keyboard is pressed
            break
    
    cap.release()