# %%
import requests
from bs4 import BeautifulSoup as bs 
import dateparser
import os

# %%

for page in range(1,5):
    start = f'https://www.theguardian.com/profile/josh-nicholas?page={page}'
    r = requests.get(start)

    soup = bs(r.text, 'html.parser')

    finder = soup.find_all(class_='fc-item__content')

    for story in finder:
        heado = story.h3.text.replace("Datablog", '').strip()
        if ":" in heado:
            heado = heado.replace(":", " -")
        urlo = story.a['href']
        slug = urlo.split("/")[-1]
        if ("Covid live" not in heado) & ("Coronavirus live" not in heado) & ("news live" not in heado) & (f"{slug}.md" not in os.listdir('journalism/')):
            datter = story.find(class_='fc-item__timestamp')['datetime']

            datto = dateparser.parse(datter).strftime("%Y-%m-%d")

            r2 = requests.get(urlo)

            soup2 = bs(r2.text, 'html.parser')

            ps = soup2.find_all('p')
            ps = [x for x in ps if len(x.text) > 5][2:5]

            stringo = ''

            for p in ps:
                stringo += "<p>"
                stringo += p.text.strip()
                stringo += "</p><br><br>"
                stringo += "\n\n"
            
            stringo += f'<p>Read more <a href="{urlo}">here</a>.</p>'

            

            print(heado)
            # print(urlo)
            # print(slug)
            print(datto)
            print(stringo)

            with open(f'journalism/{slug}.md', 'w') as f:

                html = f"""---
title: {heado}
date: {datto}
---

{stringo}"""
                f.write(html)


# %%