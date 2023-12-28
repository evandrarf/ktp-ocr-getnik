import cv2
import pytesseract

def read_nik(ktp_path):  
    img = cv2.imread(ktp_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    ## (2) Threshold
    th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)

    ## (3) Detect
    result = pytesseract.image_to_string((threshed), lang="ind")

    ## (5) Normalize
    for word in result.split("\n"):
        if '?' in word:
            word = word.replace('?', '')
        #normalize NIK
        if "NIK" in word:
            nik_char = word.split()[-1]
            if len(nik_char) == 16:
                return nik_char  