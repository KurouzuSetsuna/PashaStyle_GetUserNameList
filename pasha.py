# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv

with open('h2textlink.csv', 'w+',newline='',encoding='utf-8') as f:
    for i in range(XXXX): # XXXXを好きな数字に
        print('Pasha ID ' + str(i))
        r = requests.get("https://pasha.style/member/users/" + str(i))
        soup_content = BeautifulSoup(r.content, "html.parser")
        
        writer = csv.writer(f, lineterminator='\n')

        for n, subheading in enumerate(soup_content.find_all('h2')):
            sh = subheading.get_text()    

        writer.writerow([i, sh])
        
pass