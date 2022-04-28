import requests
import json 
import dateparser
import os
import re

urlo = 'http://joshnicholas.micro.blog/feed.json'

r = requests.get(urlo)
jsony = json.loads(r.text)

# print(jsony['items'][0])

for post in jsony['items']:

    linko = post['id']
    stem = linko.split('/')[-1].replace(".html", '')

    if f"{stem}.md" not in os.listdir('micro/'):


        titlo = stem.replace('-', ' ').title()    
        datter = post['date_published']
        datto = dateparser.parse(datter).strftime("%Y-%m-%d")

        content = post['content_html']
        content = re.sub(r"[^\x00-\x7F]+",'', content)
        content = re.sub(r"\s{2,}",'', content)
        content = content.strip()
        # print(content)
        with open(f'micro/{stem}.md', 'w') as f:

            html = f"""---
title: {titlo}
date: {datto}
---

{content}"""
            f.write(html)
    # except Exception as e:
    #     print(e)
    #     print(urlo)
    #     import sys
    #     print(f"Line: {sys.exc_info()[-1].tb_lineno}")
    #     continue