
import requests
import json 
import os
import re
import time 
import random

from responses import target

urlo = 'http://joshnicholas.micro.blog/feed.json'
pattern = r'(https://joshnicholas.micro.blog/uploads\/[\/\d\w-]+\.(?:jpg|gif|png|jpeg))'

target_path = '_site/img/'
doners = os.listdir(target_path)

r = requests.get(urlo)
jsony = json.loads(r.text)

posts = os.listdir('micro-scribble')

for post in posts:

    with open(f"micro-scribble/{post}") as f:
        content = f.read()

    links = re.findall(pattern, content, re.IGNORECASE)
    if links:
        for link in links:
            add = link.split("/")[-1]
            # if add not in doners:
            print(link)
            f = open(f"{target_path}/{add}",'wb')

            f.write(requests.get(link).content)

            time.sleep(random.random() * 1)

            new_stem = "!['Scribble image']({{ 'img/" + add + "' | url }} )"
            print(new_stem)
            # content = content.replace(link, new_stem)
            content = re.sub('\<img .+ alt=""\s\/\>',  new_stem, content)   

            with open(f"micro-scribble/{post}", 'w') as f:
                f.write(content)


