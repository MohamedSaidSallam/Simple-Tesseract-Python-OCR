import cv2
import numpy as np

DEFAULT_MEDIAN_BLUR_KSIZE = 3
DEFAULT_CANNY_THRESHIKD_1 = 100
DEFAULT_CANNY_THRESHIKD_2 = 200
DEFAULT_DILATE_KERNAL = np.ones((18, 18), np.uint8)
DEFAULT_ERODE_KERNAL = np.ones((18, 18), np.uint8)
DEFAULT_OPEN_KERNAL = np.ones((5, 5), np.uint8)
DEFAULT_CLOSE_KERNAL = np.ones((5, 5), np.uint8)


def getGrayScaleImage(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def removeNoise(image):
    return cv2.medianBlur(image, DEFAULT_MEDIAN_BLUR_KSIZE)


def applyThresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)[1]


def applyThresholdingInv(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]


def getDilatedImage(image):
    return cv2.dilate(image, DEFAULT_DILATE_KERNAL, iterations=1)


def getErodedImage(image):
    return cv2.erode(image, DEFAULT_ERODE_KERNAL, iterations=1)


def applyOpening(image):
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, DEFAULT_OPEN_KERNAL)


def applyClosing(image):
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, DEFAULT_CLOSE_KERNAL)


def getCannyResult(image):
    return cv2.Canny(image, DEFAULT_CANNY_THRESHIKD_1, DEFAULT_CANNY_THRESHIKD_2)
