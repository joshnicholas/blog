import requests
import json
import dateparser
import os
import re
import time
import random

urlo = 'http://joshnicholas.micro.blog/feed.json'
pattern = r'(https://joshnicholas.micro.blog/uploads\/[\/\d\w-]+\.(?:jpg|gif|png|jpeg))'
target_path = '_site/img/'

done1 = os.listdir('micro-scribble')
done2 = os.listdir('micro')
already_done = done1 + done2
already_done = [x.replace('.md', '') for x in already_done]
already_done = [x.replace('.json', '') for x in already_done]

print(already_done)

r = requests.get(urlo)
jsony = json.loads(r.text)

for post in jsony['items']:
    new_stem = ''

    linko = post['id']
    stem = linko.split('/')[-1].replace(".html", '')
    # print(linko)

    datter = re.findall(r"\/\d{4}\/\d{2}\/\d{2}", linko)[0]

    datto = dateparser.parse(datter)
    datto = datto.strftime('%Y-%m-%d')

    # if datto > "2020-01-01":
    #     print(datto)

    if (stem not in already_done) & (datto > "2022-01-01"):

        content = post['content_html']

        print(post.keys())
        titlo = stem.replace('-', ' ').title()
        datter = post['date_published']
        datto = dateparser.parse(datter).strftime("%Y-%m-%d")

        content = re.sub(r"[^\x00-\x7F]+",'', content)
        content = re.sub(r"\s{2,}",'', content)
        content = content.strip()



        out_path = 'micro'

        if 'tags' in post.keys():
            if 'Scribbles' in post['tags']:

                print(post['tags'])

                out_path = 'micro-scribble'

                links = re.findall(pattern, content, re.IGNORECASE)
                if links:
                    for link in links:
                        add = link.split("/")[-1]
                        # if add not in doners:
                        print(link)
                        f = open(f"{target_path}/{add}",'wb')

                        f.write(requests.get(link).content)

                        time.sleep(random.random() * 1)

                        if len(new_stem) > 1:
                            new_stem += "\n"
                            new_stem += "<br>"
                            new_stem += "\n"
                        new_stem += "!['Scribble image']({{ '/img/" + add + "' | url }} )"

                        print(new_stem)
                        content = content.replace(link, '')
                        content = re.sub('\<img .+ alt=""\s\/\>',  '', content)
                        content = re.sub('\<img .+ alt=""\>',  '', content)
                        
                        # content = re.sub('\<img .+ alt=""\s\/\>',  new_stem, content)
                        print(content)



        if f"{stem}.md" not in os.listdir(f'{out_path}/'):

            with open(f'{out_path}/{stem}.md', 'w') as f:

                html = f"""---
title: {titlo}
date: {datto}
---
{new_stem}
<br>
{content}
<br>
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
