import cv2
import pytesseract

import ocr.utility as utility

TESSERACT_CONFIG = "-l eng --oem 1 --psm 6"

OUTPUT_PATH = 'output/'

OVERLAY_BORDER_COLOR = (0, 255, 0)
OVERLAY_BORDER_THICKNESS = 2
OVERLAY_TEXT_COLOR = (0, 0, 255)
OVERLAY_TEXT_FONT = cv2.FONT_HERSHEY_SIMPLEX
OVERLAY_TEXT_SCALE = 0.85
OVERLAY_TEXT_X_SHIFT = 0
OVERLAY_TEXT_Y_SHIFT = -10
OVERLAY_TEXT_THICKNESS = 2


def preprocessImage(image, isVerbose):
    grayscale = utility.getGrayScaleImage(image)
    noNoise = utility.removeNoise(grayscale)
    threshold = utility.applyThresholdingInv(noNoise)
    dilated = utility.getDilatedImage(threshold)

    if isVerbose:
        cv2.imshow("grayscale", grayscale)
        cv2.imshow("noNoise", noNoise)
        cv2.imshow("threshold", threshold)
        cv2.imshow("dilated", dilated)

    return dilated


def main(imgPath, textOutputFileName, imageOutputFileName, showFinalImage, isVerbose):

    image = cv2.imread(imgPath)

    if isVerbose:
        cv2.imshow("The Image Loaded", image)

    preprocessed = preprocessImage(image, isVerbose)

    contours, _ = cv2.findContours(preprocessed, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_NONE)
    output = []

    imageWithOverlay = image.copy()

    contours.reverse()
    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)

        text = pytesseract.image_to_string(
            image[y:y + height, x:x + width], config=TESSERACT_CONFIG)

        text = "".join(
            [char if ord(char) < 128 else "" for char in text]).strip()

        cv2.rectangle(imageWithOverlay, (x, y),
                      (x + width, y + height), OVERLAY_BORDER_COLOR, OVERLAY_BORDER_THICKNESS)

        cv2.putText(imageWithOverlay, text, (x + OVERLAY_TEXT_X_SHIFT, y + OVERLAY_TEXT_Y_SHIFT),
                    OVERLAY_TEXT_FONT, OVERLAY_TEXT_SCALE, OVERLAY_TEXT_COLOR, OVERLAY_TEXT_THICKNESS)

        output.append(text)

    if showFinalImage or isVerbose:
        cv2.imshow("With Overlay", imageWithOverlay)

    with open(OUTPUT_PATH + textOutputFileName, 'w') as outputFile:
        outputFile.write('\n'.join(output))

    cv2.imwrite(OUTPUT_PATH + imageOutputFileName, imageWithOverlay)

    cv2.waitKey(0)
