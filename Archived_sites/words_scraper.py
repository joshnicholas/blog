import json
import datetime
import dateparser
import re
import requests

import urllib
import textwrap 


# f = open('josh-nicholas.ghost.2022-01-25-06-36-38.json')

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
                title = title.replace("'", '')
                datto = post['published_at']

                datto = dateparser.parse(datto)
                datto = datto.strftime('%Y-%m-%d')

                html = post['html']

                html = html.replace("__GHOST_URL__", "https://joshnicholas.com")

                html = textwrap.dedent(html)
                html = html.lstrip()

                print("\n\n")
                print(html)
                print("\n\n")

                with open(f'_site/words/{slug}.md', 'w') as f:

                    stringo = f"""---
title: {title}
date: {datto}
---

{html}"""

                    f.write(stringo)




post_extractor(f, "words", "5f01823bca9ec500397fb0f1")