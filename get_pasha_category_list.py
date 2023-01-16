# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv

with open('Pasha_Work_Number_list.csv', 'w+',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["応募番号", "ジャンル"])

    for Work_number in range(AAAA, ZZZZ): # AAAA, ZZZZを好きな数字に
        print('Work number ' + str(Work_number))
        res = requests.get("https://pasha.style/works/" + str(Work_number))
        soup_content = BeautifulSoup(res.content, "html.parser")

        elements = soup_content.select(".cnt_box_detail_ttl span")
        writer.writerow([Work_number, elements])

pass