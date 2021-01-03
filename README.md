# Simple Tesseract Python OCR

[![GitHub Release][github_release_badge]][github_release_link]
[![License][license-image]][license-url]

A simple tesseract python OCR done as a project for ASU 2020 for computer vision course.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install the requirements using the following:

```sh
pip install -r requirements.txt
```

or if you are using python venv:

```sh
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

duplicate the ```.env.example``` and rename it to ```.env``` and fill in the ```tesseract_path```.

### Running the code

you can get the list of paramters using the following:

```sh
python -m ocr --help
```

```sh
usage: __main__.py [-h] -i IMAGE [-c] [-t TEXT_OUTPUT_FILENAME]
                   [-f IMAGE_OUTPUT_FILENAME] [-v] [--getGrayScaleImage]
                   [--removeNoise] [--applyThresholding]
                   [--applyThresholdingInv] [--getDilatedImage]
                   [--getErodedImage] [--applyOpening] [--applyClosing]
                   [--getCannyResult]

A simple tesseract python script to get text from input image. by default this
list of preprocessing functions is used [getGrayScaleImage, removeNoise,
applyThresholdingInv, getDilatedImage]

optional arguments:
  -h, --help            show this help message and exit
  -i IMAGE, --image IMAGE
                        path to input image
  -c, --show-final-image
                        show the final image with an overlay of the text
                        recognised. (default: False)
  -t TEXT_OUTPUT_FILENAME, --text-output-filename TEXT_OUTPUT_FILENAME
                        file name to put the text output in. (default:
                        output.txt)
  -f IMAGE_OUTPUT_FILENAME, --image-output-filename IMAGE_OUTPUT_FILENAME
                        filename to output the final image in. (default:
                        output.png)
  -v, --verbose         Show intermediate images. (default: False)
  --getGrayScaleImage   (PreProcessing) adds getGrayScaleImage to
                        preprocessing. order is important.
  --removeNoise         (PreProcessing) adds removeNoise to preprocessing.
                        order is important.
  --applyThresholding   (PreProcessing) adds applyThresholding to
                        preprocessing. order is important.
  --applyThresholdingInv
                        (PreProcessing) adds applyThresholdingInv to
                        preprocessing. order is important.
  --getDilatedImage     (PreProcessing) adds getDilatedImage to preprocessing.
                        order is important.
  --getErodedImage      (PreProcessing) adds getErodedImage to preprocessing.
                        order is important.
  --applyOpening        (PreProcessing) adds applyOpening to preprocessing.
                        order is important.
  --applyClosing        (PreProcessing) adds applyClosing to preprocessing.
                        order is important.
  --getCannyResult      (PreProcessing) adds getCannyResult to preprocessing.
                        order is important.

Source: https://github.com/TheDigitalPhoenixX/Simple-Tesseract-Python-OCR
```

#### Example

```sh
py -m ocr -i "example input\input.jpg" -v
```

input.jpg
![input.png](example%20input/input.jpg)

output.txt

```
This is SAMPLE TEXT
Text is at different regions
```

output.png
![output.png](docs\output.png)

verbose:
![output.png](docs\getGrayScaleImage.png)
![output.png](docs\removeNoise.png)
![output.png](docs\applyThresholdingInv.png)
![output.png](docs\getDilatedImage.png)

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - Code Editor

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository][github-tags].

## Authors

* **Mohamed Said Sallam** - Main Dev - [TheDigitalPhoenixX](https://github.com/TheDigitalPhoenixX)

See also the list of [contributors][github-contributors] who participated in this project and their work in [CONTRIBUTORS.md](CONTRIBUTORS.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [README.md Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)

[license-image]: https://img.shields.io/badge/License-MIT-brightgreen.svg
[license-url]: https://opensource.org/licenses/MIT

[github_release_badge]: https://img.shields.io/github/v/release/TheDigitalPhoenixX/Simple-Tesseract-Python-OCR.svg?style=flat&include_prereleases
[github_release_link]: https://github.com/TheDigitalPhoenixX/Simple-Tesseract-Python-OCR/releases

[github-contributors]: https://github.com/TheDigitalPhoenixX/Simple-Tesseract-Python-OCR/contributors
[github-tags]: https://github.com/TheDigitalPhoenixX/Simple-Tesseract-Python-OCR/tags
