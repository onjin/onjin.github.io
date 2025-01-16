---
title: "google apps (gmail) i mutt"
date: 2009-05-26T10:31:04
tags: ["linux","tools"]
---
<html><body><p>Znalezione na sieci i przystosowane do google apps:</p>
<pre>

set imap_user = "user@domena.pl"

set imap_pass = "password"



set smtp_url = "smtp://users\\@domena.pl@smtp.gmail.com:587/"

set smtp_pass = "password"

set from = "user@domena.pl"

set realname = "My ql user"



set folder = "imaps://imap.gmail.com:993"

set spoolfile = "+INBOX"

set postponed="+[Google Mail]/Drafts"



set header_cache=~/.mutt/cache/headers

set message_cachedir=~/.mutt/cache/bodies

set certificate_file=~/.mutt/certificates



set move = no

</pre></body></html>
