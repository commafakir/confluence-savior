from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated
import os

app = FastAPI()

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/confluence", response_class=HTMLResponse)
async def docs():
    files = os.listdir("./docs")
    tags = map(lambda a: f"<li hx-target=\"#opened-doc\" hx-get=\"/document/{a}\">{a}</li>", files)
    return f"""
        <ul>{"".join(tags)}</ul>
    """
@app.get("/document/{doc}", response_class=HTMLResponse)
async def docs(doc):
    with open(f"./docs/{doc}", "r") as file:
        data = file.read()
    return f"""
        <div>{data}</div>
    """


@app.post("/text", response_class=HTMLResponse)
async def new_text(text: Annotated[str, Form()]):
    print(text)
    return f"""
    <div>
        You said: {text}

        I approve your message!
    </div>
    """


app.mount("/", StaticFiles(directory="public", html= True), name="public")

