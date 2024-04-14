import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np

model = YOLO('yolov8s.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('vid1.mp4')
my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 

area = [(128, 514), (3, 695), (83, 823), (75, 917), (514, 894), (377, 538)]

count = 0
start_time = cv2.getTickCount() / cv2.getTickFrequency()  # Start time
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    elapsed_time = (cv2.getTickCount() / cv2.getTickFrequency()) - start_time
    if elapsed_time > 5:  # Detect vehicles only for 5 seconds
        break

    count += 1
    if count % 3 != 0:
        continue

    frame = cv2.resize(frame, (520, 950))
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    list1 = []  # Car
    list2 = []  # Motorcycle
    list3 = []  # Rickshaw
    list4 = []  # Bus
    list5 = []  # Truck

    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])

        d = int(row[5])
        c = class_list[d]
        cx = int(x1 + x2) // 2
        cy = int(y1 + y2) // 2

        # Check for car
        if 'car' in c:
            result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
            if result >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                list1.append(cy)

        # Check for motorcycle
        elif 'motorcycle' in c:
            result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
            if result >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                list2.append(cy)

        # Check for rickshaw
        elif 'rickshaw' in c:
            result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
            if result >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                list3.append(cy)

        # Check for bus
        elif 'bus' in c:
            result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
            if result >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                list4.append(cy)

        # Check for truck
        elif 'truck' in c:
            result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
            if result >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                list5.append(cy)

    car_counter = len(list1)
    motorcycle_counter = len(list2)
    rickshaw_counter = len(list3)
    bus_counter = len(list4)
    truck_counter = len(list5)

    cv2.polylines(frame, [np.array(area, np.int32)], True, (255, 0, 0), 2)

    cvzone.putTextRect(frame, f'Car-{car_counter}', (50, 60), 2, 2)
    cvzone.putTextRect(frame, f'Motorcycle-{motorcycle_counter}', (50, 160), 2, 2)
    cvzone.putTextRect(frame, f'Rickshaw-{rickshaw_counter}', (50, 260), 2, 2)
    cvzone.putTextRect(frame, f'Bus-{bus_counter}', (50, 360), 2, 2)
    cvzone.putTextRect(frame, f'Truck-{truck_counter}', (50, 460), 2, 2)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

total_count = car_counter + motorcycle_counter + rickshaw_counter + bus_counter + truck_counter
print(f"Total count of vehicles detected: {total_count}")

cap.release()
cv2.destroyAllWindows()
