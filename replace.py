import os

file_name = "serverless.yml"

with open(file_name, encoding="cp932") as f:
    data_lines = f.read()

# 文字列置換
data_lines = data_lines.replace("LINE_CHANNEL_ACCESS_TOKEN",os.environ.get("CHANNEL_ACCESS_TOKEN"))
data_lines = data_lines.replace("LINE_GROUPID",os.environ.get("GROUPID"))

# 同じファイル名で保存
with open(file_name, mode="w", encoding="cp932") as f:
    f.write(data_lines)