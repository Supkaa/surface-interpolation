import os
import shutil
from typing import Union
import uuid
from fastapi import FastAPI, UploadFile, File, Form
from starlette.responses import HTMLResponse

from main1 import InterpApp
import webbrowser

app = FastAPI()


@app.get("/")
def read_root():
    content = """
    <body>
        <form action="/data" enctype="multipart/form-data" method="post">
            <input required name="file" type="file">
            <label for="lines">Кол-во слоёв</label>
            <input required id="lines" type="number" name="lines" min="15" max="50">
            <input type="submit">
        </form>
    </body>
        """
    return HTMLResponse(content=content)


@app.post("/data")
def image(file: UploadFile = File(...), lines: int = Form()):
    filename = str(uuid.uuid4().hex) + '.xls'
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    os.chmod(filename, 777)
    print(lines)
    inter = InterpApp(method='cubic', lines=lines, url=filename)
    return HTMLResponse(content=inter.printPlot())

    # return {"filename": file.filename}

# brows = ['mozilla',
#          'firefox',
#          'netscape',
#          'opera',
#          'windows-default',
#          'macosx',
#          'safari',
#          'google-chrome',
#          'chrome',
#          'chromium',
#          'chromium-browser']

# for i in range(len(brows)):
#     try:
#         webbrowser.get(using=f'{brows[i]}').open_new_tab('127.0.0.1:8000')
#         break
#     except:
#         pass 
