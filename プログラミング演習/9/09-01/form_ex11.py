#form_ex11.py -*- Coding:utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app=FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/input/")
async def input(request:Request):
    form=await request.form()
    input1=form["input1"]
    html1="""<html>
                <head>
                    <meta charset="UTF-8">
                </head>
            <body>
            <h1>
         """

    html=html1+input1+"</h1></body></html>"
    return HTMLResponse(content=html)
if __name__=="__main__":
    uvicorn.run("form_ex11:app",host="127.0.0.1",port=8001,log_level="debug",reload=True)