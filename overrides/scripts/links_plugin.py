"""
Put your related links into page metadata to get under TOC
---
links:
    - https://some.page.com/
    - /some/url
    - ../some/file.md
---

You can set custom titles by using dictionaries
---
links:
    - url: https://some.page.com/
      title: Custom title
---

And you can change/split the sections (default section title is `Links`)
---
links:
    - url: https://some.page.com/
      title: Custom title
      section: External link
---
"""

from itertools import groupby
import string
from typing import Any, NotRequired, TypedDict, cast
import re
from dataclasses import asdict, dataclass


from material.plugins.blog.structure import Page
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.nav import Navigation


@dataclass
class Link:
    title: str
    url: str
    section: str


class LinkDefinition(TypedDict):
    url: str
    title: NotRequired[str]
    section: NotRequired[str]


LINKS: dict[str, list[Link]] = {}

SIDEBAR_TEMPLATE = string.Template(
    """
<nav class="md-nav md-nav--secondary" aria-label="links" style="margin-top: 1em;">
    <label class="md-nav__title" for="__links">
        <span class="md-nav__icon md-icon"></span>
        $section
    </label>
    <ul class="md-nav__list" data-md-component="links" data-md-scrollfix>
    $links
    </ul>
</nav>
"""
)

LINK_TEMPLATE = string.Template(
    """
<li class="md-nav__item md-nav--secondary">
    <a href="$url" class="md-nav__link">
        <span class="md-ellipsis">
            $title
        </span>
    </a>
</li>
"""
)

DEFAULT_SECTION = "Links"


def on_page_context(
    context: dict[str, Any], page: Page, config: MkDocsConfig, nav: Navigation
):
    # if page.meta.get("template") != "category.html": return

    if "links" in page.meta:
        posts = config["plugins"]["material/blog"].blog.posts
        if not posts:
            print("no posts")
            return context
        links: list[Link] = []
        for link in page.meta["links"]:
            if isinstance(link, str):
                title = link
                url = link
                section = DEFAULT_SECTION
            elif isinstance(link, dict):
                link = cast(LinkDefinition, link)
                url = link["url"]
                title = link.get("title", url)
                section = link.get("section", DEFAULT_SECTION)
            else:
                print(f"Unsupported link configuration: {link}")
                continue
            if url.startswith("http"):
                pass  # external link
            elif url.startswith("/"):
                pass  # absolute link
            else:
                if url.endswith(".md"):
                    search = url[:-3]
                else:
                    search = url
                found = [p for p in posts if p.file.name == search]
                if not found:
                    print(f"unresolved link {search}")
                    continue
                url = found[0].abs_url
                title = found[0].title

            links.append(Link(title=title, url=url, section=section))
        LINKS[page.url] = links
    return context


def on_post_page(output_content: str, page: Page, config: MkDocsConfig) -> str:
    TOC = '(.*)(<nav class="md-nav md-nav--secondary" aria-label=".*?">.*?</nav>)(.*)'
    data = re.match(TOC, output_content, re.DOTALL)
    if data and page.url in LINKS:
        sidebars: list[str] = []
        for section, section_links in groupby(
            sorted(LINKS[page.url], key=lambda x: x.section), lambda x: x.section
        ):
            sidebar = ""
            for link in section_links:
                sidebar += LINK_TEMPLATE.substitute(asdict(link))
            sidebar = SIDEBAR_TEMPLATE.substitute(
                {"links": sidebar, "section": section}
            )
            sidebars.append(sidebar)
        return f"{data.group(1)}{data.group(2)}{''.join(sidebars)}{data.group(3)}"

    return output_content
