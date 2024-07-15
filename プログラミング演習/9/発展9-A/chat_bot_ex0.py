# chat_bot_ex0.py -*- Coding: utf-8 -*-
import uvicorn
import os
import shutil
import uuid
import datetime
import random
from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import PlainTextResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("first_chat.html", {
        "name": 'chat bot',
        "request": request
    })
@app.post("/chat_bot/")
async def chat(request: Request):
    form = await request.form()
    your_name = form['your_name']
    your_msg = form['your_msg']
    if (your_msg=='first'):
        chatbot_msg = "はじめまして．こんにちは"
        my_uuid = str(uuid.uuid4()) #UUIDを乱数で作る
        # ファイルを作る
        msg_file_path = os.path.join(".","files",my_uuid+".txt")
        msg_file = open(msg_file_path,"w",encoding='UTF-8')
        msg_file.write('{"chat_bot"'+':"'+chatbot_msg+'"},\n')
        msg_file.close()
        
    elif (your_msg=="バイバイ" or your_msg=="さようなら" or your_msg=="おわり" or your_msg=="終了"):
        chatbot_msg="チャットを終了します。"
        my_uuid = form['my_uuid']
        msg_file_path = os.path.join(".","files",my_uuid+".txt")
        msg_file = open(msg_file_path,"a",encoding='UTF-8')
        msg_file.write('{"'+your_name+'":"'+your_msg+'"},\n')
        msg_file.write('{"chat_bot"'+':"'+chatbot_msg+'"},\n')
        msg_file.close()
        return templates.TemplateResponse("tearminate_chat.html", {"your_name": your_name, "your_msg":your_msg,"name": 'chat_bot', "message":chatbot_msg,"my_uuid":my_uuid,"request":request})

    elif (your_msg=="今日の日付" or your_msg=="今日は何日ですか"):
        # ファイルを開く
        my_uuid = form['my_uuid']
        msg_file_path = os.path.join(".","files",my_uuid+".txt")
        msg_file = open(msg_file_path,"a",encoding='UTF-8')
        msg_file.write('{"'+your_name+'":"'+your_msg+'"},\n')
        t = datetime.timedelta(hours=9)
        JST = datetime.timezone(t, 'JST')
        now=datetime.datetime.now(JST)
        date=now.strftime("%Y年%m月%d日")
        chatbot_msg ="今日の日付は"+date+"です。"
        msg_file.write('{"chat_bot"'+':"'+chatbot_msg+'"},\n')
        msg_file.close()

    elif (your_msg=="元気ですか" or your_msg=="元気?"):
        # ファイルを開く
        my_uuid = form['my_uuid']
        msg_file_path = os.path.join(".","files",my_uuid+".txt")
        msg_file = open(msg_file_path,"a",encoding='UTF-8')
        msg_file.write('{"'+your_name+'":"'+your_msg+'"},\n')
        x=int(random.randint(0,2))
        if x==1:
            chatbot_msg ="元気です。"    
        else:
            chatbot_msg ="風邪気味です。"
        msg_file.write('{"chat_bot"'+':"'+chatbot_msg+'"},\n')
        msg_file.close()
        
    elif (your_msg=="新習志野キャンパス"):
        # ファイルを開く
        my_uuid = form['my_uuid']
        msg_file_path = os.path.join(".","files",my_uuid+".txt")
        msg_file = open(msg_file_path,"a",encoding='UTF-8')
        msg_file.write('{"'+your_name+'":"'+your_msg+'"},\n')
        chatbot_msg ="新習志野キャンパス    〒275-0023 千葉県習志野市芝園2-1-1"
        msg_file.write('{"chat_bot"'+':"'+chatbot_msg+'"},\n')
        msg_file.close()

    elif (your_msg=="津田沼キャンパス"):
        # ファイルを開く
        my_uuid = form['my_uuid']
        msg_file_path = os.path.join(".","files",my_uuid+".txt")
        msg_file = open(msg_file_path,"a",encoding='UTF-8')
        msg_file.write('{"'+your_name+'":"'+your_msg+'"},\n')
        chatbot_msg ="津田沼キャンパス     〒275-0016 千葉県習志野市津田沼2-17-1"
        msg_file.write('{"chat_bot"'+':"'+chatbot_msg+'"},\n')
        msg_file.close()

    elif (your_msg=="スカイツリーキャンパス"):
        # ファイルを開く
        my_uuid = form['my_uuid']
        msg_file_path = os.path.join(".","files",my_uuid+".txt")
        msg_file = open(msg_file_path,"a",encoding='UTF-8')
        msg_file.write('{"'+your_name+'":"'+your_msg+'"},\n')
        chatbot_msg ="東京スカイツリータウン®キャンパス     〒131-0045 東京都墨田区押上1-1-2 東京スカイツリータウン® 8階"
        msg_file.write('{"chat_bot"'+':"'+chatbot_msg+'"},\n')
        msg_file.close()
        
    elif (your_msg=="使用言語"):
        # ファイルを開く
        my_uuid = form['my_uuid']
        msg_file_path = os.path.join(".","files",my_uuid+".txt")
        msg_file = open(msg_file_path,"a",encoding='UTF-8')
        msg_file.write('{"'+your_name+'":"'+your_msg+'"},\n')
        chatbot_msg ="PythonとHTMLを使って作られています。"
        msg_file.write('{"chat_bot"'+':"'+chatbot_msg+'"},\n')
        msg_file.close()

    elif (your_msg=="パソコンの推奨スペック"):
        # ファイルを開く
        my_uuid = form['my_uuid']
        msg_file_path = os.path.join(".","files",my_uuid+".txt")
        msg_file = open(msg_file_path,"a",encoding='UTF-8')
        msg_file.write('{"'+your_name+'":"'+your_msg+'"},\n')
        chatbot_msg ="""・OS：Windows 11 (Pro、Homeは問わない)

                        ・CPU：Intel Core i5以上

                        ・メインメモリ：16GB以上（予算の許す限り多い方が良い）

                        ・SSD：256GB以上

                        ・Wi-Fiインタフェースを持つこと（学内で利用可能）

                        ・物理キーボードが利用可能なこと（通常、物理キーボードの方がタイピングは速い）"""
        msg_file.write('{"chat_bot"'+':"'+chatbot_msg+'"},\n')
        msg_file.close()

    else:
        my_uuid = form['my_uuid']
        msg_file_path = os.path.join(".","files",my_uuid+".txt")
        msg_file = open(msg_file_path,"a",encoding='UTF-8')
        msg_file.write('{"'+your_name+'":"'+your_msg+'"},\n')
        chatbot_msg ="わかりません。"
        msg_file.write('{"chat_bot"'+':"'+chatbot_msg+'"},\n')
        msg_file.close()

    return templates.TemplateResponse("com_chat.html", {"your_name": your_name, "your_msg":your_msg,"name": 'chat_bot', "message":chatbot_msg,"my_uuid":my_uuid,"request":request})
if __name__ == "__main__":
    uvicorn.run("chat_bot_ex0:app", host="127.0.0.1", port=8001, reload=True, log_level="debug")

