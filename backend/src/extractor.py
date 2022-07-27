
from pydoc import doc
import pytesseract
from pdf2image import convert_from_path
from patient_parser import PatientParser
POPPLER_PATH = r"C:\poppler\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from preprocessing import preprocess_image
from main_parser import MedicalDoc
from prescription_parser import PrescriptionParser

file = r"C:\Users\SomeetSingh\Desktop\medical_OCR\backend\resources\patient_details\pd_2.pdf"

def extractor(file_path, file_format):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''
    #step-1 - extracting text from pdf file.
    if len(pages) > 0:
        page = pages[0]
        processed_image = preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng') #here you can switch the languages.
        document_text = "\n" + text
    
    if file_format == 'prescription':
        parsed = PrescriptionParser(document_text)
        pp = parsed.parse()

        print("prescription class ---------- Done")
        return pp

        #now we need to create parser for prescription class. we use parser for extracting text to parser them into list.
        pass
    if file_format == "patient":
        parsed = PatientParser(document_text)
        pp = parsed.combined_dict()
        print("patient class -------------- Done")
        return pp        
        
        #now we need to create parser for patient class. we use parser for extracting text to parserthem into list.
        pass   
if __name__ == "__main__":
    extracted = extractor(file_path=file,file_format='patient')
    