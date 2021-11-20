import os

from requirements.linebot import LineBotApi
from requirements.linebot.models import TextSendMessage
# from requirements.linebot.exceptions import LineBotApiError


def post_line(text):
    line_bot_api = LineBotApi(os.environ["CHANNEL_ACCESS_TOKEN"])
    line_bot_api.push_message(os.environ["GROUPID"],
                              TextSendMessage(text=text))


def tokyo_cron(event, context):
    text = "偶数月の第一土曜はみんなでわいわい！！！！！(*´ω｀*)"
    post_line(text)


def year_end(event, context):
    text = "ぼちぼちお正月が近いので福岡で飲み会とかします？？"
    post_line(text)


def obon(event, context):
    text = "ぼちぼちお盆が近いので福岡で飲み会とかします？？"
    post_line(text)
