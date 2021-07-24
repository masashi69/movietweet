### 概要

Twitter APIを利用した映画情報投稿ツールです。

いつ(投稿日限定)、何の映画を見たかが投稿されます。

使用前に下記が必要です。

* TwitterAPIトークン、キー
  - https://developer.twitter.com/

### 使い方

* 仮想環境作成

```sh
# python3 -m venv tweetpy
# source tweetpy/bin/activate
```

```sh
# Git clone https://github.com/masashi69/movietweet.git
# cd movietweet
# pip install -r request.txt
```

* トークン、キーの設定
```
# vim configure.py
```

configure.py

```
CK = 'Your Customer API Key'
CS = 'Your Customer API Sercret Key'
AT = 'Your Access Token'
AS = 'Your Access Token Secret'
```

* ツイート
```sh
# bash twmovieinfo.sh pulp fiction
```

* tweet内容

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">2019-08-24に「Pulp Fiction」を視聴しました。<br><br>その他Infomation<br>---<br>Year: 1994<br>Genre: Crime, Drama<br>Director: Quentin Tarantino<br>Actors: Tim Roth, Amanda Plummer, Laura Lovelace, John Travolta<br>Production: Miramax Films<br>---</p>&mdash; masashi (@palomax69) <a href="https://twitter.com/palomax69/status/1165166653006467072?ref_src=twsrc%5Etfw">August 24, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

* ツイート内容の取得

```sh
# python gettw.py
2019-12-22 00:18:49 American Honey
2019-12-14 22:48:18 The Founder
2019-12-07 23:07:18 The Mule
2019-11-30 23:08:27 Atomic Blonde
2019-11-23 23:33:41 The Intouchables
2019-11-16 23:48:43 Burnt
```


