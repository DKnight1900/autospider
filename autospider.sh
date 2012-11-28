#!/bin/sh

scrapyproject=$1				# 爬虫工程
spidername=$2					# 爬虫代码所在的 py 文件名

scrapy startproject $scrapyproject

cd $scrapyproject
cp  ../template/config.ini ./
cp ../template/README.org ./
sed -i 's/defaulthome/'$1'/' config.ini # 替换 home 目录名称


cd $scrapyproject
cp -r ../../template/template/db/ ./
cp -r ../../template/template/url/ ./
cp -r ../../template/template/utils/ ./

# 修改 utils/RandomUa.py 中 ua.txt 的路径
sed -i 's/defaulthome/'$1'/' utils/RandomUa.py

cd spiders/
cp ../../../template/template/spiders/spider.py ./
mv spider.py $spidername
sed -i 's/defaultcrawler/'$scrapyproject'/' $spidername
