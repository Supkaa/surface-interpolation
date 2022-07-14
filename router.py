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
            <label for="method">Вид интерполяции</label>
            <select required id="method" name="method">
                <option>Кубический</option>
                <option>Линейный</option>
                <option>Ближайшего соседа</option>
            </select>
            <input type="submit">
        </form>
    </body>
        """
    return HTMLResponse(content=content)


@app.post("/data")
def image(file: UploadFile = File(...), lines: int = Form(), method: str = Form()):
    filename = str(uuid.uuid4().hex) + '.xls'
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    os.chmod(filename, 777)
    print(lines)
    match method:
        case 'Ближайшего соседа':
            methodc = 'nearest'
        case 'Линейный':
            methodc = 'linear'
        case 'Кубический':
            methodc = 'cubic'
    inter = InterpApp(method=methodc, lines=lines, url=filename)
    return HTMLResponse(content=inter.printPlot())

    # return {"filename": file.filename}
