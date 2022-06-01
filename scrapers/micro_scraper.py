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


    # print(post.keys())



    titlo = stem.replace('-', ' ').title()    
    datter = post['date_published']
    datto = dateparser.parse(datter).strftime("%Y-%m-%d")

    content = post['content_html']
    content = re.sub(r"[^\x00-\x7F]+",'', content)
    content = re.sub(r"\s{2,}",'', content)
    content = content.strip()
    # print(content)

    out_path = 'micro'

    if 'tags' in post.keys():
        if 'Scribbles' in post['tags']:
        
            print(post['tags'])

            out_path = 'micro-scribble'

    if f"{stem}.md" not in os.listdir(f'{out_path}/'):

        with open(f'{out_path}/{stem}.md', 'w') as f:

            html = f"""---
title: {titlo}
date: {datto}
---

{content}
<br>
<center><small>Cross posted from my <a href='http://micro.blog/joshnicholas'>micro blog</a></small></center>
<br>
"""
            f.write(html)
    # except Exception as e:
    #     print(e)
    #     print(urlo)
    #     import sys
    #     print(f"Line: {sys.exc_info()[-1].tb_lineno}")
    #     continue