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
            try:
                datter = story.find(class_='fc-item__timestamp')['datetime']

                datto = dateparser.parse(datter).strftime("%Y-%m-%d")
                format_datto = dateparser.parse(datto).strftime("%d %B %Y")

                r2 = requests.get(urlo)

                soup2 = bs(r2.text, 'html.parser')

                # byline = soup2.find(class_="byline").text

                authors = soup2.find_all(attrs={'rel':'author'})
                authors = [x.text for x in authors]

                byline = '  '.join(authors).replace("  ", " and ")

                body = soup2.find(id='maincontent')

                ps = body.find_all('p')
                ps = [x for x in ps if len(x.text) > 5][2:5]
                
                stringo = f"<br><center>by {byline}</center><br>\n\n"

                stringo += f"<center>{format_datto}</center><br><br>\n\n"

                stringo += '<blockquote>'

                for p in ps:
                    stringo += "<p>"
                    stringo += p.text.strip()
                    stringo += "</p><br>"
                    stringo += "\n\n"
                
                stringo += "</blockquote><br>\n\n"
                stringo += f'<center><a href="{urlo}">Read more</a></center>'

                

                print(heado)
                # print(urlo)
                # print(slug)
                print(byline)
                print(datto)
                print(stringo)

                with open(f'journalism/{slug}.md', 'w') as f:

                    html = f"""---
title: {heado}
date: {datto}
---

{stringo}"""
                    f.write(html)
            except Exception as e:
                print(e)
                continue


# %%