
from fastapi import FastAPI, UploadFile,File
import uuid
import uvicorn
import os
from extractor_for_pdf_docs import extractor_for_pdf_docs


app = FastAPI()


@app.post("/extract_from_doc")
def extract_from_document(file : UploadFile = File(...)):
    file_path = "C:/Users/SomeetSingh/Desktop/medical_OCR/backend/src/uploads/" + str(uuid.uuid1()) + ".pdf"
    content = file.file.read()

    with open(file_path, "wb") as f:
        f.write(content)
        f.close()
    directory_path = "C:/Users/SomeetSingh/Desktop/medical_OCR/backend/src/uploads/"
    # os.chdir(r"C:\Users\SomeetSingh\Desktop\medical_OCR\backend\src\uploads")
    file_no = 0
    for file in os.listdir(r"C:\Users\SomeetSingh\Desktop\medical_OCR\backend\src\uploads"):
        file_no +=1


        if file.endswith(".pdf"):
            
            file_to_ocr = f"{directory_path}/{file}"

            file_name = file.split(".")
            file_name = file_name[]

            extractor_for_pdf_docs(file_path=file_to_ocr, file_name=file_name)

            

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port=8000)
    