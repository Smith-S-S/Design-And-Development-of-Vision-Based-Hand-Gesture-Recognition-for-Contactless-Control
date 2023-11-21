import os
from cvzone.HandTrackingModule import HandDetector

import cv2

import time
import serial

# Define the serial port and baud rate
serial_port = '/dev/cu.usbmodem14201'  # Replace with the actual serial port
baud_rate = 9600

# Initialize the serial connection
ser = serial.Serial(serial_port, baud_rate)

# Define a function to send commands to the Arduino
def send_command(command):
    ser.write(command.encode())
    print(f"Sent command: {command}")
    time.sleep(1)  # Wait for the Arduino to process the command




cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


imgBackground = cv2.imread("/Users/smithss/PycharmProjects/covid_vanding/minnor_project/Background.png")

# importing all the mode images to a list
folderPathModes = "/Users/smithss/PycharmProjects/covid_vanding/minnor_project/Modes"
listImgModesPath = sorted(os.listdir(folderPathModes))
listImgModes = []
for imgModePath in listImgModesPath:
    listImgModes.append(cv2.imread(os.path.join(folderPathModes, imgModePath)))
print(listImgModes)

# importing all the icons to a list
folderPathIcons = "/Users/smithss/PycharmProjects/covid_vanding/minnor_project/Icons"
listImgIconsPath = sorted(os.listdir(folderPathIcons))
listImgIcons = []
for imgIconsPath in listImgIconsPath:
    listImgIcons.append(cv2.imread(os.path.join(folderPathIcons, imgIconsPath)))

modeType = 0  # for changing selection mode
selection = -1
counter = 0
selectionSpeed = 7
detector = HandDetector(detectionCon=0.8, maxHands=1)
modePositions = [(1136, 196), (1000, 384), (1136, 581)]
counterPause = 0
selectionList = [-1, -1, -1]
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2
xx=""
while True:
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # overlaying the webcam feed on the background image
    imgBackground[139:139 + 480, 50:50 + 640] = img
    imgBackground[0:720, 847: 1280] = listImgModes[modeType]
    if hands and counterPause == 0 and modeType < 3:
        # Hand 1
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        print(fingers1)
        if fingers1 == [0, 1, 0, 0, 0]:
            if selection != 1:
                counter = 1
            selection = 1
        elif fingers1 == [0, 1, 1, 0, 0]:
            if selection != 2:
                counter = 1
            selection = 2
        elif fingers1 == [0, 1, 1, 1, 0]:
            if selection != 3:
                counter = 1
            selection = 3
        else:
            selection = -1
            counter = 0
        if counter > 0:
            counter += 1
            print(counter)
            cv2.ellipse(imgBackground, modePositions[selection - 1], (103, 103), 0, 0,
                        counter * selectionSpeed, (0, 255, 0), 20)
            if counter * selectionSpeed > 360:
                selectionList[modeType] = selection
                modeType += 1
                counter = 0
                counterPause = 1
                if modeType==1 and selection==1:
                    xx = "Front"
                elif modeType==1 and  selection==2:
                    xx = "Back"
                elif modeType==1 and selection==3:
                    xx = "Clock Wise"
                elif modeType==2 and selection==1:
                    xx = "Anit-Clock Wise"
                elif modeType==2 and selection==2:
                    xx = "Right"
                elif modeType==2 and selection==3:
                    xx = "Left"
                elif modeType==3 and selection==1:
                    xx = "Front and Back"
                elif modeType==3 and selection==2:
                    xx = "Front and Anti-Clock Wise"
                elif modeType==3 and selection==3:
                    xx = "Front and Clock Wise"
                selection = -1
    # To pause after each selection is made
    if counterPause > 0:
        counterPause += 1
        send_command(xx)
        print(xx)
        # image = cv2.putText(imgBackground, xx, org, font,
        #                     fontScale, color, thickness, cv2.LINE_AA, True)
        if counterPause > 3:
            counterPause = 0
    # Add selection icon at the bottom
    if selectionList[0] != -1:
        imgBackground[636:636 + 65, 133:133 + 65] = listImgIcons[selectionList[0] - 1]
    if selectionList[1] != -1:
        imgBackground[636:636 + 65, 340:340 + 65] = listImgIcons[2+selectionList[1]]
    if selectionList[2] != -1:
        imgBackground[636:636 + 65, 542:542 + 65] = listImgIcons[5+selectionList[2]]
    # Displaying
    # cv2.imshow("Image", img)
    cv2.imshow("Background", imgBackground)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' key to exit
        break
cap.release()
cv2.destroyAllWindows()
