import os

file_name = "serverless.yml"

with open(file_name, encoding="cp932") as f:
    data_lines = f.read()

CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
GROUPID = os.environ["GROUPID"]
# 文字列置換
data_lines = data_lines.replace("LINE_CHANNEL_ACCESS_TOKEN",CHANNEL_ACCESS_TOKEN)
data_lines = data_lines.replace("LINE_GROUPID",GROUPID)

# 同じファイル名で保存
with open(file_name, mode="w", encoding="cp932") as f:
    f.write(data_lines)
