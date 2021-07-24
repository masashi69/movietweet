#!/bin/bash

# タイトルにスペースを含む場合がある
movieinfo=$(python getinfo.py $@)

if [ $? == 1 ] ; then
    echo "タイトルが見つかりません。終了します。"
    exit 1
fi

DATE=$(date +%F)
INFO=$(echo "$movieinfo" | grep -Pe '^Year|^Genre|^Director|^Actors|^Production')
TITLE=$(echo "$movieinfo" | grep -Po "Title: \K.+")

SUMMARY="""\
${DATE}に「${TITLE}」を視聴しました。

Infomation
---
${INFO}
---
"""

# 投稿上限の280byte以上を切り捨て
TWEET=$(echo "${SUMMARY}" | head -c 280)

echo "${SUMMARY}"
echo -n "投稿しますか?: [y/n]"
read CONFIRM
# デフォルトはNo
case $CONFIRM in
    [Yy]*)
        python posttw.py "${TWEET}"
        echo "投稿を完了しました。"
    ;;
    *)
        echo "スクリプトを終了します。"
        exit 0
    ;;
esac

