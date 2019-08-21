---
title: "mutt & firefox (by urlview)"
date: 2009-06-05T10:53:55
slug: blog20090605mutt-firefox-by-urlview
url: /posts/blog20090605mutt-firefox-by-urlview.html
tags: ["linux","tools"]
---
<html><body><p>w ubuntu wystarczyło:
</p><pre>

apt-get install urlview

</pre>



w ~/.muttrc dodane makro

<pre>

macro pager \\cb &lt;pipe-entry&gt;urlview&lt;enter&gt; 'Follow links with urlview'

</pre>



orac plik ~/.urlview:

<pre>

REGEXP ((http|https|ftp|gopher):(//)?[^ &lt;&gt;"\\t]*|www\\.[-a-z0-9.]+)[^ .,;\\t&lt;"&gt;\\):]

COMMAND /usr/bin/nohup firefox -remote "openURL("%s", new-tab)" &gt;/dev/null 2&gt;&amp;1 &amp;

</pre>



teraz ctrl+b zbiera linki z treści wiadomości, które otwieramy w wybranej przeglądarce ;)

</body></html>
