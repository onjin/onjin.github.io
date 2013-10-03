# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

# Configuration, please edit

# Data about this site
BLOG_AUTHOR = "Marek Wywiał"
BLOG_TITLE = "marekwywial"
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "http://marekwywial.name/"
# This is the URL where nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://getnikola.com/"
BLOG_EMAIL = "onjinx@gmail.com"
BLOG_DESCRIPTION = "never is often better than *right* now"

# Nikola is multilingual!
#
# Currently supported languages are:
# en     English
# bg     Bulgarian
# ca     Catalan
# zh_cn  Chinese (Simplified)
# hr     Croatian
# nl     Dutch
# fr     French
# el     Greek [NOT gr!]
# de     German
# it     Italian
# jp     Japanese
# fa     Persian
# pl     Polish
# pt_br  Portuguese (Brasil)
# ru     Russian
# es     Spanish
# tr_tr  Turkish (Turkey)
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (p.e. look at the modules at: ./nikola/data/themes/default/messages/fr.py).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
    #"pl": "pl",
}

# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/index.html', 'Home', 'icon-home'),
        ('/archive.html', 'Archives', 'icon-folder-open-alt'),
        ('/categories/index.html', 'Tags', 'icon-tags'),
        ('/rss.xml', 'RSS', 'icon-rss'),
        ('http://marekwywial.name', 'About me', 'icon-user'),
        ('https://twitter.com/onjin', 'My Twitter', 'icon-twitter'),
        ('https://github.com/onjin', 'My Github', 'icon-github'),
    )
}

# Below this point, everything is optional

# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and opcionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.
#

POSTS = (
    ("posts/*.wp", "posts", "post.tmpl"),
)
PAGES = (
    ("stories/*.wp", "stories", "story.tmpl"),
)

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of "source" "relative destination".
# Default is:
# FILES_FOLDERS = {'files': '' }
# Which means copy 'files' into 'output'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is html and just copies it
COMPILERS = {
    "rest": ('.txt', '.rst'),
    "markdown": ('.md', '.mdown', '.markdown', '.wp'),
    "textile": ('.textile',),
    "txt2tags": ('.t2t',),
    "bbcode": ('.bb',),
    "wiki": ('.wiki',),
    "ipynb": ('.ipynb',),
    "html": ('.html', '.htm'),
    # Pandoc detects the input from the source filename
    # but is disabled by default as it would conflict
    # with many of the others.
    # "pandoc": ('.rst', '.md', '.txt'),
}

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# If this is set to True, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# If set to False, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# HIDE_UNTRANSLATED_POSTS = False

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
# TAG_PATH = "categories"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = True

# Final location is output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# Final locations are:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Number of posts in RSS feeds
# FEED_LENGTH = 10

# Slug the Tag URL easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [
    (u'blog/2008/09/02/lint-dla-php/index.html',
     u'/blog/posts/blog20080902lint-dla-php.html'),
    (u'blog/2008/10/19/mud-astral-dominion/index.html',
     u'/blog/posts/blog20081019mud-astral-dominion.html'),
    (u'blog/2005/12/19/murphy-ma-racje-niestety/index.html',
     u'/blog/posts/blog20051219murphy-ma-racje-niestety.html'),
    (u'blog/2005/07/18/download/index.html',
     u'/blog/posts/blog20050718download.html'),
    (u'blog/2007/03/14/dreamhost-dodatkowy-adres-ip/index.html',
     u'/blog/posts/blog20070314dreamhost-dodatkowy-adres-ip.html'),
    (u'blog/2005/12/23/swinteczne-chwile/index.html',
     u'/blog/posts/blog20051223swinteczne-chwile.html'),
    (u'blog/2010/08/11/vim-snippetsemu-i-liquibase/index.html',
     u'/blog/posts/blog20100811vim-snippetsemu-i-liquibase.html'),
    (u'blog/2005/10/05/msnbetter-thangoogle-2/index.html',
     u'/blog/posts/blog20051005msnbetter-thangoogle-2.html'),
    (u'blog/2005/07/07/css-jaki-jest/index.html', u'/blog/posts/blog20050707css-jaki-jest.html'), (u'blog/2005/12/07/google-i-polityka/index.html', u'/blog/posts/blog20051207google-i-polityka.html'), (u'blog/2012/04/27/extend-lvm2-filesystem/index.html', u'/blog/posts/blog20120427extend-lvm2-filesystem.html'), (u'blog/2007/10/24/achmed-martwy-terrorysta/index.html', u'/blog/posts/blog20071024achmed-martwy-terrorysta.html'), (u'blog/2006/02/23/wlasna-strona-startowa/index.html', u'/blog/posts/blog20060223wlasna-strona-startowa.html'), (u'blog/2007/04/05/goly-i-wesoly/index.html', u'/blog/posts/blog20070405goly-i-wesoly.html'), (u'blog/2006/01/12/psi-010/index.html', u'/blog/posts/blog20060112psi-010.html'), (u'blog/etomite/index.html', u'/blog/stories/blogetomite.html'), (u'blog/2007/02/23/jamendo-gra/index.html', u'/blog/posts/blog20070223jamendo-gra.html'), (u'blog/2007/01/07/automatyzacja-pracy-z-svn-svnauto/index.html', u'/blog/posts/blog20070107automatyzacja-pracy-z-svn-svnauto.html'), (u'blog/2007/04/01/sprzatanie-internetu/index.html', u'/blog/posts/blog20070401sprzatanie-internetu.html'), (u'blog/2005/11/17/pozegnanie-z-docem/index.html', u'/blog/posts/blog20051117pozegnanie-z-docem.html'), (u'blog/2009/10/21/public-google-wave-test/index.html', u'/blog/posts/blog20091021public-google-wave-test.html'), (u'blog/2005/11/08/pixele-na-sprzedarz/index.html', u'/blog/posts/blog20051108pixele-na-sprzedarz.html'), (u'blog/2007/01/17/iphone-w-akcji/index.html', u'/blog/posts/blog20070117iphone-w-akcji.html'), (u'blog/2006/06/09/firefox-google-synchronizacja/index.html', u'/blog/posts/blog20060609firefox-google-synchronizacja.html'), (u'blog/2007/10/21/wyniki-wyborow-sondaz/index.html', u'/blog/posts/blog20071021wyniki-wyborow-sondaz.html'), (u'blog/2006/01/11/masakazu-imanari/index.html', u'/blog/posts/blog20060111masakazu-imanari.html'), (u'blog/index.html', u'/blog/posts/blog.html'), (u'blog/2006/02/09/skracanie-formularzy-java-script/index.html', u'/blog/posts/blog20060209skracanie-formularzy-java-script.html'), (u'blog/2007/10/25/rosnie-prezent-na-gmailu/index.html', u'/blog/posts/blog20071025rosnie-prezent-na-gmailu.html'), (u'blog/2006/07/28/google-code-free-hosting/index.html', u'/blog/posts/blog20060728google-code-free-hosting.html'), (u'blog/2005/09/07/security-days/index.html', u'/blog/posts/blog20050907security-days.html'), (u'blog/2007/03/15/jabber-google-firefox-itp/index.html', u'/blog/posts/blog20070315jabber-google-firefox-itp.html'), (u'blog/2010/01/03/przydatne-narzedzia-do-monitoringu-obciazenia-serwera/index.html', u'/blog/posts/blog20100103przydatne-narzedzia-do-monitoringu-obciazenia-serwera.html'), (u'blog/2006/02/02/ciekawe-gadzety/index.html', u'/blog/posts/blog20060202ciekawe-gadzety.html'), (u'blog/2012/07/30/quiet-please-disable-audio-bell-in-gvim/index.html', u'/blog/posts/blog20120730quiet-please-disable-audio-bell-in-gvim.html'), (u'blog/2005/07/29/dzien-administratora/index.html', u'/blog/posts/blog20050729dzien-administratora.html'), (u'blog/2011/03/19/grooveshark-currentsong-txt-gajim-status/index.html', u'/blog/posts/blog20110319grooveshark-currentsong-txt-gajim-status.html'), (u'blog/2007/03/20/beryl-vs-vista/index.html', u'/blog/posts/blog20070320beryl-vs-vista.html'), (u'blog/2008/01/27/nowe-google-maps/index.html', u'/blog/posts/blog20080127nowe-google-maps.html'), (u'blog/2009/01/12/git-svn-i-puste-katalogi/index.html', u'/blog/posts/blog20090112git-svn-i-puste-katalogi.html'), (u'blog/2007/08/27/jak-prawidlowo-przydzielic-obowiazki-nowym-pracownikom/index.html', u'/blog/posts/blog20070827jak-prawidlowo-przydzielic-obowiazki-nowym-pracownikom.html'), (u'blog/2006/08/09/prototype-cheat-sheet/index.html', u'/blog/posts/blog20060809prototype-cheat-sheet.html'), (u'blog/2006/01/23/proces-tworzenia-strony-internetowej/index.html', u'/blog/posts/blog20060123proces-tworzenia-strony-internetowej.html'), (u'blog/2009/02/26/homepl-django-pierwsza-potyczka/index.html', u'/blog/posts/blog20090226homepl-django-pierwsza-potyczka.html'), (u'blog/2006/01/12/aktualizacja/index.html', u'/blog/posts/blog20060112aktualizacja.html'), (u'blog/2008/10/01/lekkie-gnome-openbox-zamiast-metacity/index.html', u'/blog/posts/blog20081001lekkie-gnome-openbox-zamiast-metacity.html'), (u'blog/2006/10/19/linux-flash-player-9/index.html', u'/blog/posts/blog20061019linux-flash-player-9.html'), (u'blog/2009/06/05/mutt-firefox-by-urlview/index.html', u'/blog/posts/blog20090605mutt-firefox-by-urlview.html'), (u'blog/2008/10/01/git-cheatsheet/index.html', u'/blog/posts/blog20081001git-cheatsheet.html'), (u'blog/2006/01/10/sortowanie-tabel/index.html', u'/blog/posts/blog20060110sortowanie-tabel.html'), (u'blog/2008/08/24/netbeans-65-php5-symfony-xdebug/index.html', u'/blog/posts/blog20080824netbeans-65-php5-symfony-xdebug.html'), (u'blog/2012/07/05/rescan-scsi-bus-no-reboot/index.html', u'/blog/posts/blog20120705rescan-scsi-bus-no-reboot.html'), (u'blog/2005/11/10/is-ms-windows-ready-for-the-desktop/index.html', u'/blog/posts/blog20051110is-ms-windows-ready-for-the-desktop.html'), (u'blog/2006/11/03/aardvark-i-firefox20/index.html', u'/blog/posts/blog20061103aardvark-i-firefox20.html'), (u'blog/2005/11/03/psi-010-test3/index.html', u'/blog/posts/blog20051103psi-010-test3.html'), (u'blog/2006/03/30/teoria-wzglednosci/index.html', u'/blog/posts/blog20060330teoria-wzglednosci.html'), (u'blog/2008/08/29/virtualbox-brakujacy-vboxdrv-kernel-ubuntu/index.html', u'/blog/posts/blog20080829virtualbox-brakujacy-vboxdrv-kernel-ubuntu.html'), (u'blog/2005/09/07/jabber-roster/index.html', u'/blog/posts/blog20050907jabber-roster.html'), (u'blog/2005/10/11/osodziae-sobie-ycie/index.html', u'/blog/posts/blog20051011osodziae-sobie-ycie.html'), (u'blog/2013/08/13/python-soap-server-flask-wsdl-generation/index.html', u'/blog/posts/blog20130813python-soap-server-flask-wsdl-generation.html'), (u'blog/2005/07/08/msnbetter-thangoogle/index.html', u'/blog/posts/blog20050708msnbetter-thangoogle.html'), (u'blog/2005/11/25/to_nie_jestbe/index.html', u'/blog/posts/blog20051125to_nie_jestbe.html'), (u'blog/2009/06/21/fuse-ftp-mount-curlftpfs/index.html', u'/blog/posts/blog20090621fuse-ftp-mount-curlftpfs.html'), (u'blog/2009/10/19/awesome2-wm-mousekey-bindings/index.html', u'/blog/posts/blog20091019awesome2-wm-mousekey-bindings.html'), (u'blog/2006/12/21/aardvark-20/index.html', u'/blog/posts/blog20061221aardvark-20.html'), (u'blog/2009/08/10/memo-mysql-incorrect-file-format-dla-tabeli/index.html', u'/blog/posts/blog20090810memo-mysql-incorrect-file-format-dla-tabeli.html'), (u'blog/2013/09/18/fast-sentry-instance-using-docker/index.html', u'/blog/posts/blog20130918fast-sentry-instance-using-docker.html'), (u'blog/2006/06/28/zrozumiec-czyjas-droge/index.html', u'/blog/posts/blog20060628zrozumiec-czyjas-droge.html'), (u'blog/2006/09/28/muzyka-sluchanie-promocja/index.html', u'/blog/posts/blog20060928muzyka-sluchanie-promocja.html'), (u'blog/2005/12/29/psi-jingle/index.html', u'/blog/posts/blog20051229psi-jingle.html'), (u'blog/2005/12/01/i-co-ty-na-to/index.html', u'/blog/posts/blog20051201i-co-ty-na-to.html'), (u'blog/2007/10/29/remember-the-milk-google-gears/index.html', u'/blog/posts/blog20071029remember-the-milk-google-gears.html'), (u'blog/2007/03/12/dreamhost-szybciej/index.html', u'/blog/posts/blog20070312dreamhost-szybciej.html'), (u'blog/2006/05/11/urban-ninja/index.html', u'/blog/posts/blog20060511urban-ninja.html'), (u'blog/2009/05/12/porzadki-na-dysku-czyli-mv-ln-mount-i-bind/index.html', u'/blog/posts/blog20090512porzadki-na-dysku-czyli-mv-ln-mount-i-bind.html'), (u'blog/2007/07/07/macromedia-flash-problem/index.html', u'/blog/posts/blog20070707macromedia-flash-problem.html'), (u'blog/2005/11/02/css-reboot/index.html', u'/blog/posts/blog20051102css-reboot.html'), (u'blog/2006/01/20/troche-smiechu-na-weekend/index.html', u'/blog/posts/blog20060120troche-smiechu-na-weekend.html'), (u'blog/2009/06/22/ftpmount-v110-github/index.html', u'/blog/posts/blog20090622ftpmount-v110-github.html'), (u'blog/2010/05/04/git-php-syntax-check-pre-commit/index.html', u'/blog/posts/blog20100504git-php-syntax-check-pre-commit.html'), (u'blog/2009/05/26/google-apps-gmail-i-mutt/index.html', u'/blog/posts/blog20090526google-apps-gmail-i-mutt.html'), (u'blog/2008/07/10/gwiezdne-wojny-by-telnet/index.html', u'/blog/posts/blog20080710gwiezdne-wojny-by-telnet.html'), (u'blog/2006/05/25/ruy-narujima/index.html', u'/blog/posts/blog20060525ruy-narujima.html'), (u'blog/2005/11/04/linux-standard-base/index.html', u'/blog/posts/blog20051104linux-standard-base.html'), (u'blog/2006/03/22/tworzenie-strony-internetowej/index.html', u'/blog/posts/blog20060322tworzenie-strony-internetowej.html'), (u'blog/2008/03/20/ahmed-powraca/index.html', u'/blog/posts/blog20080320ahmed-powraca.html'), (u'blog/2006/01/18/google-talk/index.html', u'/blog/posts/blog20060118google-talk.html'), (u'blog/2010/07/29/best-vim-plugins/index.html', u'/blog/posts/blog20100729best-vim-plugins.html'), (u'blog/2005/12/08/swinteczne-szalenstwo/index.html', u'/blog/posts/blog20051208swinteczne-szalenstwo.html'), (u'blog/2006/07/31/gentoo-dbf2csv-ebuild/index.html', u'/blog/posts/blog20060731gentoo-dbf2csv-ebuild.html'), (u'blog/2011/10/11/useful-collection-of-cheat-sheet-desktop-wallpaper-for-web-designers/index.html', u'/blog/posts/blog20111011useful-collection-of-cheat-sheet-desktop-wallpaper-for-web-designers.html'), (u'blog/2012/03/14/vim-vundle-plugin-manager-programming/index.html', u'/blog/posts/blog20120314vim-vundle-plugin-manager-programming.html'), (u'blog/2006/06/06/darmowe-mp3-od-sony-bmg/index.html', u'/blog/posts/blog20060606darmowe-mp3-od-sony-bmg.html'), (u'blog/2006/04/07/media-2006/index.html', u'/blog/posts/blog20060407media-2006.html'), (u'blog/2009/05/11/git-pre-commit-hook-symfony-php/index.html', u'/blog/posts/blog20090511git-pre-commit-hook-symfony-php.html'), (u'blog/2005/11/15/canvas-i-firefox-15/index.html', u'/blog/posts/blog20051115canvas-i-firefox-15.html'), (u'blog/2005/12/06/przyspieszyn-firefoxa-fasterfox/index.html', u'/blog/posts/blog20051206przyspieszyn-firefoxa-fasterfox.html'), (u'blog/2010/04/26/devhelp-django-1-1/index.html', u'/blog/posts/blog20100426devhelp-django-1-1.html'), (u'blog/2006/04/04/konsola-jak-w-quake/index.html', u'/blog/posts/blog20060404konsola-jak-w-quake.html'), (u'blog/2009/06/25/ftpmount-v120/index.html', u'/blog/posts/blog20090625ftpmount-v120.html'), (u'blog/2006/02/10/slownik-wyrazow-obcych/index.html', u'/blog/posts/blog20060210slownik-wyrazow-obcych.html'), (u'blog/2007/03/12/picasa-web-albums-puchnie/index.html', u'/blog/posts/blog20070312picasa-web-albums-puchnie.html'), (u'blog/firefox/index.html', u'/blog/stories/blogfirefox.html'), (u'blog/2006/05/23/vim-cheat-sheet/index.html', u'/blog/posts/blog20060523vim-cheat-sheet.html'), (u'blog/2005/10/28/cssreboot/index.html', u'/blog/posts/blog20051028cssreboot.html'), (u'blog/2006/01/04/psi-010-test4/index.html', u'/blog/posts/blog20060104psi-010-test4.html'), (u'blog/2005/11/18/robomatic-x11/index.html', u'/blog/posts/blog20051118robomatic-x11.html'), (u'blog/2006/05/23/cheat-sheets/index.html', u'/blog/posts/blog20060523cheat-sheets.html'), (u'blog/2005/11/16/badanianet/index.html', u'/blog/posts/blog20051116badanianet.html'), (u'blog/2005/11/25/skype-koledzy/index.html', u'/blog/posts/blog20051125skype-koledzy.html'), (u'blog/2007/10/30/gwiazdy-tancza-na-lodzie-umbrella/index.html', u'/blog/posts/blog20071030gwiazdy-tancza-na-lodzie-umbrella.html')]

# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav output/* joe@my.site:/srv/www/site"
# And then do a backup, or ping pingomatic.
# To do manual deployment, set it to []
# DEPLOY_COMMANDS = []
DEPLOY_COMMANDS = [
    "git add .",
    #"git commit -am 'Update'",
    "git push origin website",
    "git subtree split --prefix output -b master",
    "git push -f origin master:master",
    "git branch -D master",
]

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, there are no filters.
#
# Many filters are shipped with Nikola.  A list is available in the manual:
# <http://getnikola.com/handbook.html#post-processing-filters>
# FILTERS = {
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Create a gzipped copy of each generated file. Cheap server-side optimization.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None

# #############################################################################
# Image Gallery Options
# #############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
# GALLERY_PATH = "galleries"
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes
# INDEXES_TITLE = ""  # If this is empty, the default is BLOG_TITLE
# INDEXES_PAGES = ""  # If this is empty, the default is 'old posts page %d'
# translated

# Name of the theme to use.
THEME = "bootstrap3"
THEME = "blogtxt"
THEME = "zen"

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni
# monokai murphy native pastie perldoc rrt tango trac vim vs
# CODE_COLOR_SCHEME = 'default'

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# date format used to display post dates.
# (str used by datetime.datetime.strftime)
# DATE_FORMAT = '%Y-%m-%d %H:%M'

# FAVICONS contains (name, file, size) tuples.
# Used for create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# For creating favicons, take a look at:
# http://www.netmagazine.com/features/create-perfect-favicon
# FAVICONS = {
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# }

# Show only teasers in the index pages? Defaults to False.
# INDEX_TEASERS = False

# A HTML fragment with the Read more... link.
# The following tags exist and are replaced for you:
# {link}        A link to the full post page.
# {read_more}   The string “Read more” in the current language.
# {{            A literal { (U+007B LEFT CURLY BRACKET)
# }}            A literal } (U+007D RIGHT CURLY BRACKET)
# READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'

# A HTML fragment describing the license, for the sidebar.
LICENSE = ""
# I recommend using the Creative Commons' wizard:
# http://creativecommons.org/choose/
LICENSE = """
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">
<img alt="Creative Commons License" style="border-width:0"
    src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />
This work is licensed under a <a rel="license"
href="http://creativecommons.org/licenses/by/3.0/deed.en_US">
Creative Commons Attribution 3.0 Unported License</a>.
"""

# A small copyright notice for the page footer (in HTML).
# Default is ''
CONTENT_FOOTER = '''Contents &copy; {date}         <a href="mailto:{email}">
{author}</a> - Powered by         <a href="http://getnikola.com">Nikola</a>
{license}'''
CONTENT_FOOTER = CONTENT_FOOTER.format(email=BLOG_EMAIL,
                                       author=BLOG_AUTHOR,
                                       date=time.gmtime().tm_year,
                                       license=LICENSE)

# To use comments, you can choose between different third party comment
# systems, one of "disqus", "livefyre", "intensedebate", "moot",
#                 "googleplus" or "facebook"
COMMENT_SYSTEM = "disqus"
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = "marekwywial"

# Create index.html for story folders?
# STORY_INDEX = False
# Enable comments on story pages?
COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
# Default = False
# STRIP_INDEXES = False

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
# SITEMAP_INCLUDE_FILELESS_DIRS = True

# Instead of putting files in <slug>.html, put them in
# <slug>/index.html. Also enables STRIP_INDEXES
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata
# PRETTY_URLS = False

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False
# If True, schedules post to today if possible, even if scheduled hour is over
# SCHEDULE_FORCE_TODAY = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
#MATHJAX_CONFIG = """
#<script type="text/x-mathjax-config">
#MathJax.Hub.Config({
#    tex2jax: {
#        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ]
#    },
#    displayAlign: 'left', // Change this to 'center' to center equations.
#    "HTML-CSS": {
#        styles: {'.MathJax_Display': {"margin": 0}}
#    }
#});
#</script>
#"""

# What MarkDown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty.
SOCIAL_BUTTONS_CODE = """
<!-- Social buttons -->
<div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style
addthis_default_style addthis_label_style addthis_32x32_style">
<a class="addthis_button_more">Share</a>
<ul><li><a class="addthis_button_facebook"></a>
<li><a class="addthis_button_google_plusone_share"></a>
<li><a class="addthis_button_linkedin"></a>
<li><a class="addthis_button_twitter"></a>
</ul>
</div>
<script type="text/javascript"
src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798">
</script>
<!-- End of social buttons -->
"""

# Hide link to source for the posts?
# HIDE_SOURCELINK = False
# Copy the source files for your pages?
# Setting it to False implies HIDE_SOURCELINK = True
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.
# RSS_LINK = None

# Show only teasers in the RSS feed? Default to True
# RSS_TEASERS = True

# A search form to search this site, for the sidebar. You can use a google
# custom search (http://www.google.com/cse/)
# Or a duckduckgo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
#SEARCH_FORM = """
#<!-- Custom search -->
#<form method="get" id="search" action="http://duckduckgo.com/"
# class="navbar-form pull-left">
#<input type="hidden" name="sites" value="%s"/>
#<input type="hidden" name="k8" value="#444444"/>
#<input type="hidden" name="k9" value="#D51920"/>
#<input type="hidden" name="kt" value="h"/>
#<input type="text" name="q" maxlength="255"
# placeholder="Search&hellip;" class="span2" style="margin-top: 4px;"/>
#<input type="submit" value="DuckDuckGo Search" style="visibility: hidden;" />
#</form>
#<!-- End of custom search -->
#""" % SITE_URL
#
# If you prefer a google search form, here's an example that should just work:
#SEARCH_FORM = """
#<!-- Custom search with google-->
#<form id="search" action="http://google.com/search" method="get"
# class="navbar-form pull-left">
#<input type="hidden" name="q" value="site:%s" />
#<input type="text" name="q" maxlength="255" results="0" placeholder="Search"/>
#</form>
#<!-- End of custom search -->
#""" % SITE_URL

# Also, there is a local search plugin you can use, based on Tipue,
# but it requires setting several options:

SEARCH_FORM = """
<span class="navbar-form pull-left">
<input type="text" id="tipue_search_input">
</span>"""

BODY_END = """
<script type="text/javascript" src="/assets/js/tipuesearch_set.js"></script>
<script type="text/javascript" src="/assets/js/tipuesearch.js"></script>
<script type="text/javascript">
$(document).ready(function() {
  # $('#tipue_search_input').tipuesearch({
      # 'mode': 'json',
      # 'contentLocation': '/assets/js/tipuesearch_content.json',
      # 'showUrl': false
  # });
});
</script>
"""

# EXTRA_HEAD_DATA = """
# <link rel="stylesheet" type="text/css" href="/assets/css/tipuesearch.css">
# <div id="tipue_search_content" style="margin-left: auto; margin-right: auto;
# padding: 20px;"></div>
# """
ENABLED_EXTRAS = ['local_search']
#


# Use content distribution networks for jquery and twitter-bootstrap css and js
# If this is True, jquery is served from the Google CDN and twitter-bootstrap
# is served from the NetDNA CDN
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Extra things you want in the pages HEAD tag. This will be added right
# before </HEAD>
# EXTRA_HEAD_DATA = ""
# Google analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# BODY_END = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Twitter Card summaries / Open Graph.
# Twitter cards make it possible for you to attach media to Tweets
# that link to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit
# https://dev.twitter.com/form/participate-twitter-cards
#
# Uncomment and modify to following lines to match your accounts.
# Specifying the id for either 'site' or 'creator' will be preferred
# over the cleartext username. Specifying an ID is not necessary.
# Displaying images is currently not supported.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards / Open Graph
#     # 'site': '@website',  # twitter nick for the website
#     # 'site:id': 123456,  # Same as site, but the website's Twitter user ID
#                           # instead.
#     # 'creator': '@username',  # Username for the content creator / author.
#     # 'creator:id': 654321,  # Same as creator, but the Twitter user's ID.
# }


# Post's dates are considered in GMT by default, if you want to use
# another timezone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Also, if you want to use a different timezone in some of your posts,
# you can use W3C-DTF Format (ex. 2012-03-30T23:00:00+02:00)
#
TIMEZONE = 'Europe/Warsaw'

# If webassets is installed, bundle JS and CSS to make site loading faster
USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Experimental plugins - use at your own risk.
# They probably need some manual adjustments - please see their respective
# readme.
#ENABLED_EXTRAS = [
#     'planetoid',
#     'ipynb',
#     'local_search',
#     'render_mustache',
#]
ENABLED_EXTRAS = [
    'local_search',
]

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# HYPHENATE = False

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.

GLOBAL_CONTEXT = {}
