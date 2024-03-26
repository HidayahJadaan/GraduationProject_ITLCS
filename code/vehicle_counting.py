import cv2
import glob
from vehicle_detector import VehicleDetector


def v_count(cap,vd):



    while True:
        _, img = cap.read()

        # height,width,channels=img.shape >The current dimention is width:640 / height:480

        new_width=90
        aspect_ratio=img.shape[1]/img.shape[0]
        new_height=int(new_width/aspect_ratio)
        resized_img=cv2.resize(img,(new_width,new_height))

        '''
        crop_width=128
        crop_height=128
        start_x=(resized_img.shape[1]-crop_width)
        start_y=(resized_img[0]-crop_height)
        cropped_img=resized_img[start_y:start_y+crop_height,start_x:start_x+crop_width]
        '''
        
        # cv2.imwrite("./img.jpg", img)

        # Load Veichle Detector


        # Load images from a folder
        # images_folder = glob.glob("images/*.jpg")

        vehicles_folder_count = 0

        # Loop through all the images
        # for img_path in images_folder:
        # print("Img path", img_path)
        # img = cv2.imread(img_path)

        vehicle_boxes = vd.detect_vehicles(resized_img)
        vehicle_count = len(vehicle_boxes)

        # Update total count
        vehicles_folder_count += vehicle_count

        for box in vehicle_boxes:
            x, y, w, h = box

            cv2.rectangle(resized_img, (x, y), (x + w, y + h), (25, 0, 180), 3)

            cv2.putText(resized_img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

        #imgResize = cv2.resize(img, (500, 500))
        cv2.imshow("Cars", resized_img)

        print("Total current count", vehicles_folder_count)

        
        break


    return vehicles_folder_count
