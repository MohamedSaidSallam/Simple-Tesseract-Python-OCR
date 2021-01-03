import argparse

import ocr.utility as utility
from ocr.ocr import main

availablePreProcessing = [
    utility.getGrayScaleImage,
    utility.removeNoise,
    utility.applyThresholding,
    utility.applyThresholdingInv,
    utility.getDilatedImage,
    utility.getErodedImage,
    utility.applyOpening,
    utility.applyClosing,
    utility.getCannyResult
]

preprocessingDefault = [utility.getGrayScaleImage, utility.removeNoise,
                        utility.applyThresholdingInv, utility.getDilatedImage]
preprocessingDefaultText = ', '.join(
    [func.__name__ for func in preprocessingDefault])

parser = argparse.ArgumentParser(
    description=f'A simple tesseract python script to get text from input image. by default this list of preprocessing functions is used [{preprocessingDefaultText}]',
    epilog='Source: https://github.com/TheDigitalPhoenixX/Simple-Tesseract-Python-OCR'
)
parser.add_argument("-i", "--image", type=str, required=True,
                    help="path to input image")
parser.add_argument("-c", "--show-final-image", action='store_true',
                    help="show the final image with an overlay of the text recognised. (default: %(default)s)")
parser.add_argument("-t", "--text-output-filename", type=str, default='output.txt',
                    help="file name to put the text output in. (default: %(default)s)")
parser.add_argument("-f", "--image-output-filename", type=str, default='output.png',
                    help="filename to output the final image in. (default: %(default)s)")
parser.add_argument("-v", "--verbose", action='store_true',
                    help="Show intermediate images. (default: %(default)s)")

for func in availablePreProcessing:
    parser.add_argument(f"--{func.__name__}", dest='preprocessing', action='append_const', const=func,
                        help=f"(PreProcessing) adds {func.__name__} to preprocessing. order is important.")


args = parser.parse_args()

main(
    imgPath=args.image,
    textOutputFileName=args.text_output_filename,
    imageOutputFileName=args.image_output_filename,
    showFinalImage=args.show_final_image,
    isVerbose=args.verbose,
    preprocessing=args.preprocessing if args.preprocessing else preprocessingDefault,
)
