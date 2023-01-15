# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv

with open('PashaID_Name_list.csv', 'w+',newline='',encoding='utf-8') as f:
    for pasha_id in range(XXXX): # XXXXを好きな数字に
        print('Pasha ID ' + str(pasha_id))
        res = requests.get("https://pasha.style/member/users/" + str(pasha_id))
        soup_content = BeautifulSoup(res.content, "html.parser")
        
        writer = csv.writer(f, lineterminator='\n')

        for n, subheading in enumerate(soup_content.find_all('h2')):
            user_name = subheading.get_text()    
            writer.writerow([pasha_id, user_name])
pass