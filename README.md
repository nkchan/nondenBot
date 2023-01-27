# nondenBot
## 概要
大学を卒業して意識して会う場を作りたいなぁということで定期的に「あそばん？」ってお誘いしてくれるbotを作りました。それでお互いの近況報告したり云々できるといいねぇ。

暇な人が集まって遊ぼーぜくらいのノリで集まるきっかけ作りです。社会人になって半年、いくらご時世があれだったとはいえ、連絡すらあんまりとってなかった感あるのできっかけ作りとして作った！

ガルパンはこの限りではない。映画が公開される情報があったらさっさと予定抑えたいねぇ。

メインは関東にいる人用になってしまってる感はあるけど、福岡勢もみんなとの会話のきっかけにしたり、福岡組で集まったりするきっかけになればと思ってる。あとは、帰省タイミングの調整にも使えるからね。

## 定期実行される job

```
functions:
  tokyo-cron:
    handler: handler.tokyo_cron
    events:
    - schedule: cron(0 20 20 1-12/1 ? *)
  year-end:
    handler: handler.year_end
    events:
    - schedule: cron(0 20 20 12 ? *)
  obon:
    handler: handler.obon
    events:
    - schedule: cron(0 20 10 8 ? *)

```

- 関東組定期開催 → 偶数月　第一土曜日(奇数月の 20 日に通知)
- お盆 → 毎年 8月10日に通知
- お正月 → 毎年 12月20日に通知

時間は全項目共通で 20 時です。(きっと)お仕事終わりに通知が来るくらいに設定しました。お盆とかお正月の10日前くらいにだーっと調整する感じにしてるけどご意見あればぜひ！！！(PRでもええんやで)

## 開発前の事前準備
Python のパッケージ管理ツールとして [poetry](https://python-poetry.org/docs/) をインストールしてください。

## 使い方
[こういう](https://developers.line.biz/ja/docs/messaging-api/getting-started/)ところを見てチャンネルなどなどを作成する。Messaging API を使っております。

```
$ git clone git@github.com:nkchan/nondenBot.git
$ cd nondenBot
$ poetry install
```

これで開発して Pull-Request をお願いします。あと PR は lint 通らないとだめにしています。

```console
$ poetry run pysen run format
```

でフォーマッタを実行して修正するなどしてください。

## 技術的な話
- Python3
- [Serverless](https://www.serverless.com/)
- AWS Lambda
- AWS S3
- (間接的に)EventBridge

FaaS でサクッとやってます。

## ToDo
- LINE の投稿に失敗したら SMS が飛んでくる
- みんなの知ってる美味しいお店教えてくれる

## お願い
エラーハンドリングなどなどしてない、雑なコードなので機能追加、リファクタの PR お待ちしてますー。
