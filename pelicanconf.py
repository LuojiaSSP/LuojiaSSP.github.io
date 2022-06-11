AUTHOR = 'Xiaokang'
SITENAME = 'Spatial Search People'
# SITENAME = 'Spatial Search People'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs/'
PAGE_PATHS = ['pages']


TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True
# The default category to fall back on.
# DEFAULT_CATEGORY = 'Home'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

LINKS = (('Waterlogging Dashboard', 'https://wybert.github.io/showcase/'),
         ('Xiaokang', "https://xiaokang.github.io/"))

SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
        #   ('lastfm', 'http://lastfm.com/user/akounet'),
          ('github', 'https://github.com/LuojiaSSP'),)
# PAGE_ORDER_BY = 'basename'

# MENUITEMS = (
#     ('Home', '/'),
#     ('Research', 'pages/research.html'),
#     ('People', 'people.html'),
#     ('About', 'about.html'),
# )
PAGE_ORDER_BY = 'nav_oder'

GOOGLE_ANALYTICS = 'G-JR11EBFBG6'
