

import pytesseract
from pdf2image import convert_from_path
from patient_parser import PatientParser
POPPLER_PATH = r"C:\poppler\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import uuid
import os


def extractor_for_pdf_docs(file_path, file_name):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''
    #step-1 - extracting text from pdf file.

    if len(pages) > 0:
        page = pages[0]
        text = pytesseract.image_to_string(page, lang='deu') #here you can switch the languages.
        document_text = "\n" + text

        extracted_files = "C:/Users/SomeetSingh/Desktop/medical_OCR/backend/src/extracted_for_multi/" +   str(file_name)  + ".txt"




        with open(extracted_files, "w") as f:
            f.write(document_text)
            f.close
        
        # with open(file_path, "wb") as f:
        # f.write(content)
        # f.close()






    # if file_format == 'prescription':
    #     parsed = PrescriptionParser(document_text)
    #     pp = parsed.parse()

    #     print("prescription class ---------- Done")
    #     return pp

    #     #now we need to create parser for prescription class. we use parser for extracting text to parser them into list.
    #     pass
    # if file_format == "patient":
    #     parsed = PatientParser(document_text)
    #     pp = parsed.combined_dict()
    #     print("patient class -------------- Done")
    #     return pp        
        
    #     #now we need to create parser for patient class. we use parser for extracting text to parserthem into list.
    #     pass

    
