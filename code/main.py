import cv2
import vehicle_counting
import time
from vehicle_detector import VehicleDetector
import run_lights
import Jetson.GPIO as GPIO

vd = VehicleDetector()


#cam_id_1=0
#cam_id_1='/dev/video0'
cam_id_1='/dev/v4l/by-id/usb-046d_C270_HD_WEBCAM_200901010001-video-index0'
cam_id_2='/dev/v4l/by-id/usb-046d_0825_7F865050-video-index0'
cam_id_3='/dev/v4l/by-id/usb-046d_0825_62386050-video-index0'
cam_id_4='/dev/v4l/by-id/usb-046d_0825_0F796050-video-index0'

cam_id_list = [cam_id_1, cam_id_2, cam_id_3, cam_id_4]

Vcam_id_1=0
Vcam_id_2=1
Vcam_id_3=2
Vcam_id_4=3

location= 'ACPI(_SB_)#ACPI(PCI0)#ACPI(XHC_)#ACPI(RHUB)#ACPI(HS02)#USBMI(0)'
#cap1 = cv2.VideoCapture(location)  # capture the id
#cap1 = cv2.VideoCapture(cam_id_1)
#cap2 = cv2.VideoCapture(cam_id_2)  # capture the id  >>"serial://2114LZ51PG49"
#cap3 = cv2.VideoCapture(Vcam_id_3)  # capture the id
#cap4 = cv2.VideoCapture(Vcam_id_4)  # capture the id



traffic_light_list = []


while True:

    run_lights.initialize()
    i = 0
    for cam_id in cam_id_list:
        cap = cv2.VideoCapture(cam_id)
        v_num= vehicle_counting.v_count(cap,vd) #pass the id for each cam
        light_data=[i,v_num]
        traffic_light_list.append(light_data)
        #print("V_Number %s = %s", str(i), str(v_num))
        print(f"V_Number {str(i)} = {str(v_num)}")
        i += 1
        light_data = []
        cap = None #if "cap = None" causes error, try "cap = []", else: call me :)

   # time.sleep(1)

#    v_num2= vehicle_counting.v_count(cap2,vd)
#    light2_data = [Vcam_id_2, v_num2]
#    traffic_light_list.append(light2_data)

   # print("V_Number 2 = ",v_num2)


    '''
    v_num3= vehicle_counting.v_count(cap3,vd)
    light3_data = [Vcam_id_3, v_num3]
    traffic_light_list.append(light3_data)

    print("V_Number 3 = ",v_num3)


    v_num4= vehicle_counting.v_count(cap4,vd)
    light4_data = [Vcam_id_4, v_num4]
    traffic_light_list.append(light4_data)

    print("V_Number 4 = ",v_num4)


    '''

    #v_numbers=[v_num1,v_num2]

    #sorted_numbers=sorted(v_numbers)

    sorted_list = sorted(traffic_light_list, key=lambda x: x[1],reverse=True)  #sort based on v_num's


    #run lights based on v_numbers & id

    '''
            if (light_data == sorted_list[0]):
            run_lights.greenlight(light_data[0])
        else:
            run_lights.redlight(light_data[0])

    '''

    for light_data in sorted_list:

        print (light_data)

        run_lights.light(light_data[0],light_data[1]) #Vcam_id,v_num


    time.sleep(1)
    traffic_light_list = []
    #sleep(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        GPIO.cleanup()
        break
