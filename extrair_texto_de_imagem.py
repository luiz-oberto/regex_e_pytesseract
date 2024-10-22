from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'caminho do tesseract caso não esteja configurado no PATH'
# Load the image
img_path = 'caminho da imagem'
img = Image.open(img_path)

# Extract text from image using pytesseract
text = pytesseract.image_to_string(img)

# Salvar o texto em um arquivo de anotações
with open('caminho para onde o texto da imagem será extraido', 'w', encoding='utf-8') as file:
    file.write(text)

# Display the extracted text
print(text)
