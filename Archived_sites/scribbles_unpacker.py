import json
import datetime
import dateparser
import re
import requests

import urllib
import textwrap 


f = open('josh-nicholas.ghost.2022-01-25-06-36-38.json')

### INITIAL EXPLORE

# data = json.load(f)['db'][0]['data'].keys()

# dict_keys(['custom_theme_settings', 'posts', 'posts_authors', 'posts_meta', 'posts_tags', 'roles', 'roles_users', 'settings', 'tags', 'users'

#### FIND OUT THE TAG NAMES AND IDS

# data = json.load(f)['db'][0]['data']['tags']
#
# for tag in data:
#     print(tag['name'], tag['id'])
# photos 5f01823bca9ec500397fb0ed
# scribbles 5f01823bca9ec500397fb0ee
# words 5f01823bca9ec500397fb0f1
# charts 5f0d50052ecadf0039ac5ec1
# micro 5f9cbf85516ae20039263ceb

pattern = r'(__GHOST_URL__\/content\/[\/\d\w-]+\.(?:jpg|gif|png|jpeg))'

def post_extractor(fillo, tag_name, tag_id):
    data = json.load(fillo)['db'][0]['data']

    posts_tags = data['posts_tags']

    inter = []

    ## Grab the post ids for every id in with the right tag id
    for post in posts_tags:
        # print(post.keys())
        if post['tag_id'] == tag_id:
    #
            inter.append(post['post_id'])
    #
    posts = data['posts']

    ### Grab the post for each post matching a post id from the tag
    for post in posts:
        # dict_keys(['id', 'uuid', 'title', 'slug', 'mobiledoc', 'html', 'comment_id',
        #  'plaintext', 'feature_image', 'featured', 'type', 'status', 'locale',
        #  'visibility', 'author_id', 'created_at', 'updated_at', 'published_at', 'custom_excerpt',
        #   'codeinjection_head', 'codeinjection_foot', 'custom_template', 'canonical_url', 'email_recipient_filter'])

        if post['id'] in inter:
            if post['visibility'] == 'public':
                slug = post['slug']

                if "--" in slug:
                    slug = slug.split("--")[0]

                title = post['title']
                print(title)
                datto = post['published_at']
                # datto = datetime.datetime.strptime(datto, "%Y-%x")
                # datto = datetime.datetime.strftime(datto, "%Y-%m-%d")

                datto = dateparser.parse(datto)
                datto = datto.strftime('%Y-%m-%d')

                plain = post['plaintext']

                html = post['html']

                html = "<center>" + html


                links = re.findall(pattern, html)
                links = [x.replace("__GHOST_URL__", "https://joshnicholas.com") for x in links]

                html = html.replace("__GHOST_URL__", "https://joshnicholas.com")

                print(links)
                print(plain)

                # print(links)

                # html = '<center>'
                html = ''

                for link in links[-1:]:

                    add = link.split("/")[-1]
                    html += f"!['{title}']("  + "{{ '/img/" + '{linker}'.format(linker=add) + """' | url }} )"""
                    # html += "\n"
                    # html += "<br>"
                    # html += "\n"
                    # print(link)
                    # add = link.split("/")[-1]

                    # html = html.replace(link, f"/img/{add}")
                    # html = html.replace(link, f"\{{ '/img/{add}' | url }}")

                    # new_pattern = r"""<figure[\s\d\w="-]+><img src="\/img\/{linker}"[\s\d\w="-\/]+><\/figure>""".format(linker=add)
                    # print(html)
                    # print(new_pattern)
                    # html = html.replace(new_pattern, f"""![The San Juan Mountains are beautiful!]({{ '{add}' | url }} "San Juan Mountains")""")
                    # html = re.sub(new_pattern, f"""![The San Juan Mountains are beautiful!]({{ '{add}' | url }} "San Juan Mountains")""", html)
                    # print(type(html))

                    # title_search = re.search(new_pattern, html, re.IGNORECASE)

                    # if title_search:
                    #     title = title_search.group(1)
                    #     if title:
                    #         print(title)

                    # f = open(f"/Users/josh_nicholas/personal_git/blog/img/{add}",'wb')
                    f = open(f"_site/img/{add}",'wb')

                    # f.write(urllib.urlopen(link).read())
                    f.write(requests.get(link).content)
                    f.close()
                    # print(add)
                    # urllib.request.urlretrieve(link,f"/Users/josh_nicholas/personal_git/images/{add}")
                html += '\n<br>\n'
                if plain is not None:
                    html += plain
                html = textwrap.dedent(html)
                html = html.lstrip()

                print(html)

                # html += "</center>"
                # print(links)
                # html = html.replace("__GHOST_URL__", "https://joshnicholas.com")
                # html = html.replace(link, f"{{ '/img/{add}' | url }}")
                counter = 1
                with open(f'_site/scribbles/{slug}.md', 'w') as f:

                    stringo = f"""---
title: {title}
date: {datto}
---

{html}"""

                    f.write(stringo)
                counter += 1


post_extractor(f, "scribbles", "5f01823bca9ec500397fb0ee")

# data = json.load(f)['db'][0]['data']['posts_tags']
#
# for post in data:
#     if post['tag_id'] == '5f01823bca9ec500397fb0ed':
#         # print(post['title'])
#         print(post)
    # print(post.keys())
    # print(post['slug'])
    # if post['title'] == "New drawing book":
    #     html = post['html']
    #     html = html.replace("__GHOST_URL__", "https://joshnicholas.com")
        # print(html)
        # print(post.keys())

# print(data['posts_tags'])

# print(data)