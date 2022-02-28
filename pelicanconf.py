#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'vanomad'
SITENAME = 'vanomad'
SITEURL = 'https://vanomad.com'
SITESUBTITLE = 'a photo journal of my days living as a nomad'

PATH = 'content'
OUTPUT_PATH = 'docs/'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE = 'fs' # this should defautl to filesystem date when no date is in the .md meta

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = 'feeds/all.atom.xml'

FEED_ALL_RSS ='feeds/rss.xml'

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# IMAGE_PROCESS = {
#     "article-image": ["scale_in 300 300 True"],
#     "500": ["scale_in 500 500 True"],
#     "thumb": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
# }

DISQUS_SITENAME = 'vanomad-com'

THEME = 'THEME-vanomad'  # previously called "jhc-aboutwilson"

# <a class="btn btn-outline-light btn-lg px-4" href="/set-a-home-page-in-pelican-site-generator-instead-of-a-blog.html" rel="bookmark" title="Link to Set a Home Page in Pelican Site Generator instead of a Blog." role="button">Read More</a>
