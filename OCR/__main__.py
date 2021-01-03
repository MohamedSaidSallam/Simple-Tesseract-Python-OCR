import argparse

import ocr.utility as utility
from ocr.ocr import main

parser = argparse.ArgumentParser(
    description='A simple tesseract python script to get text from input image.',
    epilog='Source: https://github.com/TheDigitalPhoenixX/Simple-Tesseract-Python-OCR'
)
parser.add_argument("-i", "--image", type=str, required=True,
                    help="path to input image")
parser.add_argument("-c", "--show-final-image", type=bool, default=False,
                    help="show the final image with an overlay of the text recognised. (default: %(default)s)")
parser.add_argument("-t", "--text-output-filename", type=str, default='output.txt',
                    help="file name to put the text output in. (default: %(default)s)")
parser.add_argument("-f", "--image-output-filename", type=str, default='output.png',
                    help="filename to output the final image in. (default: %(default)s)")
parser.add_argument("-v", "--verbose", action='store_true',
                    help="Show intermediate images. (default: %(default)s)")

args = parser.parse_args()

main(
    imgPath=args.image,
    textOutputFileName=args.text_output_filename,
    imageOutputFileName=args.image_output_filename,
    showFinalImage=args.show_final_image,
    isVerbose=args.verbose,
)
