# _*_ coding: utf-8 _*_
# @Time     : 2019/8/29 1:15
# @Author   : Ole211
# @Site     :
# @File     : camera calibration.py
# @Software : PyCharm

import cv2
import os
import numpy as np
import glob
os.chdir('d:\\img\\cal\\test')

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points like (0, 0, 0), (1, 0, 0), (2, 0, 0) ...,(6, 5, 0)
objp = np.zeros((6*7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

# Array to store object points and image points from all the images
objpoints = []
imgpoints = []

images = glob.glob('*.jpg')

for fname in images:
    print(fname)
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)
    print(ret)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
        cv2.imshow('img', img)

        # Calibration
        # So now we have our object points and image points we are ready to go for calibration.
        # For that we use the function, cv2.calibrateCamera(). It return the camera
        # matrix, distortion coeffcients, rotation and translation vectors etc
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

        # Undistortion
        '''
        We have got what we were trying. Now we can take an image and undistort it. OpenCV comes with two methods, 
        we will see both. But before that, we can refine the camera matrix based on a free scaling parameter 
        using cv2.getOptimalNewCameraMatrix(). If the scaling parameter alpha=0, it returns undistorted image with minimum unwanted pixels.
        So it may even remove some pixels at image corners. If alpha=1, all pixels are retained with some extra black images.
        It also returns an image ROI which can be used to crop the result.
        '''
        # Undistortion


        cv2.waitKey(0)
cv2.destroyAllWindows()