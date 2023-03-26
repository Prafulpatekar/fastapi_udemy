from fastapi import APIRouter,File,UploadFile
from fastapi.responses import FileResponse

# Standard Library
import os
import shutil

router = APIRouter(
    prefix='/file',
    tags=['files']
)

PATH = f"{os.getcwd()}\\media\\"

@router.post('/send')
def send_file(file:bytes=File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {
        "lines":lines
    }

@router.post('/uploadFile')
def upload_file(uploadFile:UploadFile=File(...)):
    # path = PATH + uploadFile.filename
    path = f"media/{uploadFile.filename}"
    print(path)
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(uploadFile.file,buffer)
    return {
        "filename":path,
        "type":uploadFile.content_type
    }

@router.get('/download/{fileName}',response_class=FileResponse)
def download_file(fileName:str):
    path = f"media/{fileName}"
    return path