from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



app = FastAPI()


@app.post("/text", response_class=HTMLResponse)
async def new_text(text: Annotated[str, Form()]):
    print(text)
    return """
    <div>
        Some response fragment
    </div>
    """
