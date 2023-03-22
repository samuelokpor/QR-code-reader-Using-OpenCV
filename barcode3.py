import cv2
import numpy as np
from pyzbar.pyzbar import decode
import gxipy as gx


device_manager = gx.DeviceManager()
dev_num, dev_info_list = device_manager.update_device_list()

if dev_num == 0:
    print("No device found")
    exit()

cam = device_manager.open_device_by_index(1)
if cam is None:
    print("No U3V device found")
    exit()

cam.stream_on()
with open('myDataFIle.txt') as f:
    myDataList = f.read().splitlines()

while True:

    try:
        
        # Get a frame from the camera
        img  = cam.data_stream[0].get_image()
        if img is None:
            continue

        # Convert the frame to a numpy array
        img = img.convert("RGB")
        img = img.get_numpy_array()
        

        # Detect barcodes in the image
        barcodes = decode(img)

        # Process each detected barcode
        for barcode in barcodes:
            myData = barcode.data.decode('utf-8')
            print(myData)

            # Check if the barcode data is in the list
            if myData in myDataList:
                myOutput = 'OK'
                myColor = (0, 255, 0)
            else:
                myOutput = 'NG'
                myColor = (0, 0, 255)

            # Draw the barcode on the image
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (0, 255, 0), 5)
            pts2 = barcode.rect
            cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, myColor, 3)
            cv2.putText(img, myData, (pts2[0], pts2[2]), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, myColor, 2)

        # Display the image
        cv2.imshow('Result', img)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except KeyboardInterrupt:
        break

cam.close_device()
cv2.destroyAllWindows()
    

