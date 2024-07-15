#prg08-3.py
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import random

ans=random.randint(0,100)
app = FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/")
async def index(request:Request):
    param={'request':request}
    return templates.TemplateResponse("question.html",param)

@app.post("/answer",response_class=HTMLResponse)
async def answer(request:Request):
    form=await request.form()
    question=form['question']
    param={'request':request}

    html_1="""<html>
                <charset="utf-8">
                <body>"""
    html_2="""

                </body>
            </html>"""
    Back="""<a href="javascript:history.back();">戻る</a>"""

    if int(question)>ans:
        MoreSmall="""
                <p>もっと小さい</p>
                """
        html=html_1+MoreSmall+Back+html_2

    elif int(question)<ans:
        MoreBig="""
                <p>もっと大きい</p>
                """
        html=html_1+MoreBig+Back+html_2
    else:
        Right="""<p>正解</p>"""
        html=html_1+Right+Back+html_2

    return html

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8001,log_level="debug")