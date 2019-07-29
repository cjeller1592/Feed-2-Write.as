import requests
import writeas

import xml.etree.ElementTree as ET
import os

### PUT IN VALUES BEFORE STARTING ############################################################################
# The url of your RSS Feed
feed = ''
# The collection alias for your blog the post is to be hosted on -> ex: for https://digitalgyoza.writeas.com, the alias is 'digitalgyoza'
alias = ''
# The slug for the RSS feed post - ex. for https://write.as/cjeller/mypost, the slug is 'mypost'
# This will be used to update the post as the RSS feed updates
slug = ''
# The introductory text for your post. This will be prepended to the list of links.
# For example, you could say: "Here is what I am currently reading right now on the web:"
intro = ''
# And finally what makes it all happen - the authentication token!!!
# The Write.as token you will use to authenticate creating/updating post
token = os.environ.get('TOKEN')


# CODE BEGINS HERE ###########################################################################################

# This takes the XML feed and converts the items into a list of Markdown links for the post
def read(feed):
# Let's see if I can get all the post titles...
# Create a tree from xmlfile

    r = requests.get(feed)

    xmlfile = r.content

    root= ET.fromstring(xmlfile)

 # create empty list for titles
    titleitems = []

# This is how we are going to start iterating through the file
    for item in root.findall('./channel/item'):

# Empty dictionary
        posts = {}

        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://purl.org/rss/1.0/modules/content/}content':
                posts['media'] = child.attrib['url']
            else:
                posts[child.tag] = child.text.encode('utf8')

        # append news dictionary to news items list
        titleitems.append(posts)

    # return news items list
    list = []

    for post in titleitems:
        btitle = post['title']
        blink = post['guid']
        link = blink.decode('utf-8')
        title = btitle.decode('utf-8')

        thing = '[{}]({})\n\n'.format(title, link)

        list.append(thing)

    return list
  
# This takes the list of links and forms it into one string which will become the body of the post
def convert(list):
    res = str("".join(map(str, list)))

    return res

# This updates the XML Feed post
def update():
# Grabs the RSS feed and converts the list of links into a string
    list = read(feed)
    feed_body = convert(list)
    
# Combines the intro with the list to form the body
    body = '{}\n\n{}'.format(intro, feed_body)

    c = writeas.client()
    c.setToken(token)

    p = c.retrieveCPost(alias, slug)
    id = p['id']
    current_body = p['body']
    
# Here is the code in the fxn that updates the post as the RSS feed updates
# But if the RSS feed body and current body are the same, just spit out the post
    if current_body != body:
      c.updatePost(id, body=body)
    
    url = 'https://write.as/{}/{}'.format(alias, slug)

    return url
