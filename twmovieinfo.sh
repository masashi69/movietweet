#!/bin/bash

# タイトルにスペースを含む場合がある
movieinfo=$(movies -d $@)

if [ $? == 1 ] ; then
    echo "タイトルが見つかりません。終了します。"
    exit 1
fi

DATE=$(date +%F)
INFO=$(echo "$movieinfo" | cut -d ' ' -f 2- | grep -Pe '^Y|^G|^Di|^Ac|^Pr')
# sedで行末スペース削除
TITLE=$(echo "$movieinfo" | grep Title | awk '{c="";for(i=3;i<=NF;i++) c=c $i" " ;print c}'| sed -e 's/ $//'| head -n1)

TWEET="""\
${DATE}に「${TITLE}」を視聴しました。

Infomation
---
${INFO}
---
"""

echo "${TWEET}"
strings=$(echo "${TWEET}" | wc -c)
echo "${strings}文字"

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

