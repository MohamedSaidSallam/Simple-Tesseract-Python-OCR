import cv2
import pytesseract


TESSERACT_CONFIG = "-l eng --oem 1 --psm 6"

OUTPUT_PATH = 'output/'


def main(imgPath, outputFileName):

    image = cv2.imread(imgPath)

    output = pytesseract.image_to_string(image, config=TESSERACT_CONFIG)

    output = "".join([c if ord(c) < 128 else "" for c in output]).strip()

    with open(OUTPUT_PATH + outputFileName, 'w') as outputFile:
        outputFile.write(output)
