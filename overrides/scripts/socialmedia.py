from textwrap import dedent
from typing import Any
import urllib.parse
import re
from mkdocs.structure.pages import Page
from mkdocs.config.defaults import MkDocsConfig

x_intent = "https://twitter.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"
include = re.compile(r"blog/(?!(archive|category|tags)).+")


def on_page_markdown(markdown: str, **kwargs: Any):
    page: Page = kwargs["page"]
    config: MkDocsConfig = kwargs["config"]
    if not include.match(page.url) or page.url.endswith("blog"):
        return markdown
    print(f"URL: {page.title}")

    page_url = page.url
    if config.site_url:
        page_url = config.site_url + page_url
    page_title = urllib.parse.quote(str(page.title) + "\n")

    return markdown + dedent(
        f"""
    [Share on :simple-x:]({x_intent}?text={page_title}&url={page_url}){{ .md-link }}
    [Share on :simple-facebook:]({fb_sharer}?u={page_url}){{ .md-link }}
    """
    )
