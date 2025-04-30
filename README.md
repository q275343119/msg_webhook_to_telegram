# Telegram Webhook 服务

简体中文 | [English](./README_EN.md)

这是一个基于 FastAPI 的 Webhook 服务，用于接收 HTTP 请求并将消息转发到 Telegram。该服务提供了安全的 API 接口，支持通过 webhook 方式发送消息到指定的 Telegram 用户。

## 功能特点

- 基于 FastAPI 构建，提供高性能的异步 API
- 支持安全密钥验证，确保 API 调用的安全性
- 简单易用的 RESTful API 接口
- 可配置的服务器端口
- 完善的错误处理机制

## 环境要求

- Python 3.8+
- [Poetry](https://python-poetry.org/) 包管理器

## 安装步骤

1. 克隆项目到本地：
```bash
git clone https://github.com/q275343119/msg_webhook_to_telegram.git
cd msg_webhook_to_telegram
```

2. 安装 Poetry（如果尚未安装）：
```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# Linux/macOS
curl -sSL https://install.python-poetry.org | python3 -
```

3. 安装项目依赖：
```bash
poetry install
```

4. 配置环境变量：
   - 复制 `.env.example` 文件为 `.env`
   - 编辑 `.env` 文件，填入必要的配置信息：
     ```
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
     SECRET_KEY=your_secret_key_here
     PORT=8000
     ```

## 配置说明

### 环境变量

- `TELEGRAM_BOT_TOKEN`: Telegram Bot 的 token，从 @BotFather 获取
- `SECRET_KEY`: Webhook 请求的安全密钥，用于验证请求的合法性
- `PORT`: 服务运行的端口号，默认为 8000

### 获取 Telegram Bot Token

1. 在 Telegram 中搜索并联系 @BotFather
2. 发送 `/newbot` 命令
3. 按照提示设置机器人名称和用户名
4. 获取并保存生成的 token

## 使用方法

1. 启动服务：
```bash
poetry run python main.py
```

2. 发送消息到指定用户：
```bash
curl -X POST "http://localhost:8000/webhook" \
     -H "Content-Type: application/json" \
     -d '{
           "secret_key": "your_secret_key",
           "msg": "Hello, World!",
           "user_id": "123456789"
         }'
```

### API 接口说明

- **接口地址**: `/webhook`
- **请求方法**: POST
- **请求体**:
  ```json
  {
    "secret_key": "string",  // 安全密钥
    "msg": "string",        // 要发送的消息内容
    "user_id": "string"     // Telegram 用户 ID
  }
  ```
- **响应**:
  ```json
  {
    "status": "success",
    "message": "Message sent successfully"
  }
  ```

## 错误处理

服务会返回以下可能的错误状态码：

- `403`: 无效的安全密钥
- `500`: 服务器内部错误（如发送消息失败）

## 安全建议

1. 使用足够复杂的安全密钥（SECRET_KEY）
2. 确保 `.env` 文件不被提交到版本控制系统
3. 在生产环境中使用 HTTPS
4. 定期更换安全密钥

## 许可证

本项目采用 MIT 许可证，详情请参见 [LICENSE](LICENSE) 文件。

