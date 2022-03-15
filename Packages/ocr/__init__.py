import pytesseract
import cv2

def ocr_processing(image, lang):
    tessdata_dir_config = '--psm 1 -c preserve_interword_spaces=1 --tessdata-dir "./Packages/Tesseract-OCR/tessdata"'
    pytesseract.pytesseract.tesseract_cmd = r'.\Packages\Tesseract-OCR\tesseract'

    src = pytesseract.image_to_string(image, lang=lang, config=tessdata_dir_config)
    return src

def opencv_image_process(image, lang='kor'):
    image = cv2.imread(image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(3,3),0)
    
    # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    cv2.imshow('image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return ocr_processing(gray, lang)