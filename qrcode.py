import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# img = cv2.imread('qr.png')

# decodedObjects = pyzbar.decode(img)
# for obj in decodedObjects:
#     print("Data:", obj.data)

# cv2.namedWindow("QR Image", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("QR Image", img.shape[1], img.shape[0])

# cv2.imshow("QR Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

img = cv2.imread('qr.png')

decodedObjects = pyzbar.decode(img)
for obj in decodedObjects:
    print("Data:", obj.data)

    # draw lines around the QR code
    pts = obj.polygon
    pts = np.array(pts, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (0, 255, 0), 3)

    # display the decoded data on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, obj.data.decode('utf-8'), (pts[0][0][0], pts[0][0][1] - 20), font, 3, (0, 0, 255), 5, cv2.LINE_AA)

cv2.namedWindow("QR Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("QR Image", img.shape[1], img.shape[0])

cv2.imshow("QR Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()