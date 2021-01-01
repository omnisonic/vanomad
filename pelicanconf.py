#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'VaNomad'
SITENAME = 'VaNomad'
SITEURL = 'https://vanomad.com'

PATH = 'content'
OUTPUT_PATH = 'docs/'
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

IMAGE_PROCESS = {
    "article-image": ["scale_in 300 300 True"],
    "500": ["scale_in 500 500 True"],
    "thumb": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
}

DISQUS_SITENAME = 'vanomad-com'