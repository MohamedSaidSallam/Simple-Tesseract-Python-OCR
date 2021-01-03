import cv2
import pytesseract

import ocr.utility as utility

TESSERACT_CONFIG = "-l eng --oem 1 --psm 6"

OUTPUT_PATH = 'output/'


def preprocessImage(image):
    grayscale = utility.getGrayScaleImage(image)
    cv2.imshow("grayscale", grayscale)
    noNoise = utility.removeNoise(grayscale)
    cv2.imshow("noNoise", noNoise)
    threshold = utility.applyThresholding(noNoise)
    cv2.imshow("threshold", threshold)
    eroded = utility.getErodedImage(threshold)
    cv2.imshow("eroded", eroded)
    return eroded


def main(imgPath, outputFileName):

    image = cv2.imread(imgPath)

    cv2.imshow("The Image Loaded", image)

    preprocessed = preprocessImage(image)

    contours, _ = cv2.findContours(preprocessed, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_NONE)
    output = []

    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)

        text = pytesseract.image_to_string(
            preprocessed[y:y + height, x:x + width], config=TESSERACT_CONFIG)

        text = "".join(
            [char if ord(char) < 128 else "" for char in text]).strip()

        output.append(text)

    with open(OUTPUT_PATH + outputFileName, 'w') as outputFile:
        outputFile.write('\n'.join(output))

    cv2.waitKey(0)
