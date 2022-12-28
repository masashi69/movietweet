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


### 公開年指定

* --yearで公開年を指定

##### 引数無し

```sh
$ bash twmovieinfo.sh start-up
2022-05-05に「Start-Up」を視聴しました。
 
Infomation
---
Year: 2020\u2013
Genre: Comedy, Drama, Romance
Director: N/A
Actors: Bae Suzy, Nam Joo-hyuk, Kim Seon-Ho
---
 
投稿しますか?: [y/n]
```

##### 引数あり

```sh
$ bash twmovieinfo.sh start-up --year 2019
2022-05-05に「Start-Up」を視聴しました。
 
Infomation
---
Year: 2019
Genre: Action, Comedy, Drama
Director: Jeong-Yeol Choi
Actors: Ma Dong-seok, Jeong Min Park, Jung Hae-In
Production: N/A
---
 
投稿しますか?: [y/n]
```

### ツイート内容の取得

```sh
$ python gettw.py | head
2022/12/25 22:55:21 Old School
2022/12/25 09:35:17 The Batman
2022/12/18 21:11:57 Charlie's Angels
2022/12/17 23:36:10 The Ruthless
2022/12/11 22:56:49 The Whole Nine Yards
2022/12/10 23:21:26 Kiss the Girls
2022/12/09 22:58:47 Paul Blart: Mall Cop 2
2022/12/03 23:40:44 Project Power
2022/11/27 22:04:41 Budapest
2022/11/23 22:49:27 The Gentlemen
```

### ツイート内容の取得 (投稿年指定)

```sh
$ python gettw.py --year=2021 | head
2021/12/30 00:23:25 The Wolf of Wall Street
2021/12/26 22:41:32 The Tourist
2021/12/26 00:44:12 Saturday Night Fever
2021/12/19 22:28:11 Showtime
2021/12/12 21:48:05 Running with the Devil
2021/12/12 09:41:46 The Informer
2021/12/04 22:26:00 Office Christmas Party
2021/11/27 21:56:23 Believer
2021/11/23 23:00:05 Central Intelligence
2021/11/21 22:03:05 R.I.P.D.
```

