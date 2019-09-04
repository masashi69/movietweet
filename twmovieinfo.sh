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
TITLE=$(echo "$movieinfo" | grep Title | awk '{c="";for(i=3;i<=NF;i++) c=c $i" " ;print c}'| sed -e 's/ $//')

TWEET="""\
${DATE}に「${TITLE}」を視聴しました。

その他Infomation
---
${INFO}
---
"""

python posttw.py "${TWEET}"
