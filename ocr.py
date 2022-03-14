import pytesseract
import cv2

def ocr_processing(image):
    pytesseract.pytesseract.tesseract_cmd = r'.\Packages\Tesseract-OCR\tesseract'

    src = pytesseract.image_to_string(image, lang='eng', config='--psm 1 -c preserve_interword_spaces=1')
    print(src)

def opencv_image_process():
    image = cv2.imread('./resources/test/eng_text.png')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # cv2.imshow('image', gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    ocr_processing(gray)

opencv_image_process()