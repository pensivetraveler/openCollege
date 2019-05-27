from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('+gOCQRywr0b5e1Ti6YdIjvNCf6akgCcNWAb7YSuhWz0FXbc5QIIfpDmtnolRjBqGxX3AgQ4/qfG8EwlYRkGByoaKbmFwl+98eur8NLkr5wm04LZh3Nrc/SJy22SGGkZrL34P0CF3ykHUkXxbJpXjlQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5e8fd6c20078c2089cd7329180876fb4')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/healthCheck')
def health_check():
    return 'ok'


@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == '__main__':
    app.run()
