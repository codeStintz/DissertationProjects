# Importing 'OpenCV2' which is python library for computer vision
# Import all functions from the two other files created
from FaceFinding import *
from FaceTracking import *

import datetime 

#Establishes connection with the drone & displays battery
drone.connect()
print(drone.get_battery())
 
#Turns the camera on and drone takes off to a certain height
drone.streamon()
drone.takeoff()
drone.send_rc_control(0,0,15,0)


# While loop is used to repeatedly loop and run this this piece of code until
# instructed to stop by the user
while True:
    #Handles drone video output
    picture = drone.get_frame_read().frame
    picture = cv2.resize(picture, (width, height))
    
    #Uses functions made in other files
    picture, data = locate(picture)
    Error = tracking(data, width, controller, error1)

    # Displays the video stream through opencv
    cv2.imshow("Output", picture)

    #Drone will take pictures when user is within certain range
    Area = data[1]
    if 6200 < Area < 6900:
        cv2.imwrite(f'Images/DetectedFace{datetime.datetime.now()}.jpg', picture)
            
    # If the user presses the 'l' button, the drone will land
    key = cv2.waitKey(1) & 0xff
    if key == ord('l'):
        drone.land()
        drone.streamoff()
        break








 

 
 