from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated

app = FastAPI()

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.post("/text", response_class=HTMLResponse)
async def new_text(text: Annotated[str, Form()]):
    print(text)
    return """
    <div>
        Some response fragment
    </div>
    """


app.mount("/", StaticFiles(directory="public", html= True), name="public")

