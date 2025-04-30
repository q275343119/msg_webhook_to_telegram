from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from telegram import Bot
import asyncio

# 加载环境变量
load_dotenv()

# 创建FastAPI应用
app = FastAPI(title="Telegram WebHook Service")

# 获取环境变量
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SECRET_KEY = os.getenv("SECRET_KEY")
PORT = int(os.getenv("PORT", "8000"))  # 默认端口为 8000

# 创建Telegram Bot实例
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# 请求模型
class WebhookRequest(BaseModel):
    secret_key: str
    msg: str
    user_id: str

# 验证secret_key的依赖函数
async def verify_secret_key(request: WebhookRequest):
    if request.secret_key != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid secret key")
    return request

@app.post("/webhook")
async def webhook(request: WebhookRequest = Depends(verify_secret_key)):
    try:
        # 发送消息到Telegram
        await bot.send_message(
            chat_id=request.user_id,
            text=request.msg
        )
        return {"status": "success", "message": "Message sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT) 