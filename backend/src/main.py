from genericpath import exists
from fastapi import FastAPI, UploadFile, Form, File
from numpy import extract
from pydantic import FilePath
from extractor import extractor
import uuid
import uvicorn
import os



app = FastAPI()

@app.post("/extract_from_doc")


def extract_from_document(file_format : str = Form(...) , file : UploadFile = File(...)):
    file_path = "C:/Users/SomeetSingh/Desktop/medical_OCR/backend/src/uploads/" + str(uuid.uuid1()) + ".pdf"
    content = file.file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    data = extractor(file_path, file_format)
    if os.path.exists(file_path):
        os.remove(file_path)
    return data

    

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port=8000)

