import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('pic.png')
text = tess.image_to_string(img)

print(text)