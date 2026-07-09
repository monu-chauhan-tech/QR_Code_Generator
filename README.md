# QR Code Generator

A simple Python application that generates QR codes from text or URLs and saves them as PNG images.

## Features

- Generate QR codes from any text
- Generate QR codes for website URLs
- Save QR codes as PNG images
- Easy to use command-line interface

## Technologies Used

- Python 3
- qrcode library
- Pillow (PIL)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/monu-chauhan-tech/QR_Code_Generator.git
```

2. Install the required library:

```bash
pip install qrcode[pil]
```

## Usage

Run the program:

```bash
python qr_generator.py
```

Enter the text or URL when prompted and provide a file name. The QR code image will be saved in the project folder.

## Example

**Input**

```
Enter text or URL:
https://github.com/monu-chauhan-tech

Enter file name:
github_qr
```

**Output**

```
QR Code saved as github_qr.png
```

## Project Structure

```
QR_Code_Generator/
│── qr_generator.py
│── README.md
```

## Future Improvements

- Add a graphical user interface (GUI)
- Allow users to change QR code colors
- Add support for different image formats
- Generate QR codes with custom logos

## Author

**Monu Chauhan**

B.Tech CSE (Artificial Intelligence & Machine Learning)