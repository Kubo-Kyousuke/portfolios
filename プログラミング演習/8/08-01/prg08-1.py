#prg08-1.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app=FastAPI()
@app.get("/",response_class=HTMLResponse)
async def root():
    return"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>こんにちは</title>    
            </head>
            <body>
                <font color="fff00">
                <h1>Hello,World!</h1>
                <p>24G2040 久保 亨介</p><br>
                <a href="https://google.co.jp">google</a>
                <script>
                    alert("Hello world!");
                </script>
            </body>
        </html>"""

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",post=8001)