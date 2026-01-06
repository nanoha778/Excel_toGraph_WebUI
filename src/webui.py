from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from main import MakeGraph
import os
import uuid
import shutil

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"))

os.makedirs("uploads", exist_ok=True)
os.makedirs("static", exist_ok=True)


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": None
        }
    )


@app.post("/", response_class=HTMLResponse)
def submit(request: Request, action:str | None = Form(None), file: UploadFile = File(None)):
    if action == "upload":
        ext = os.path.splitext(file.filename)[1].lower()
        upload_path = os.path.join("uploads", f"{uuid.uuid4().hex}{ext}")
        with open(upload_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        output_path = os.path.join("static", "result.png")
        
        MakeGraph(upload_path, output_path)

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "image": output_path,
                "error" : None
            }
        )
    if action == "download":
        output_path = os.path.join("static", "result.png")
        return FileResponse(output_path)
        
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": None
        }
    )
