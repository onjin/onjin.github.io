from typing import Any


from material.plugins.blog.structure import Page
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.nav import Navigation


def on_page_context(
    context: dict[str, Any], page: Page, config: MkDocsConfig, nav: Navigation
):
    # if page.meta.get("template") != "category.html": return
    posts = config["plugins"]["material/blog"].blog.posts

    if "links" in page.meta:
        if not posts:
            print("no posts")
            return context
        links = []
        for link in page.meta["links"]:
            if isinstance(link, str):
                title = link
            elif isinstance(link, dict):
                title = link["title"]
                link = link["url"]
            else:
                print(f"Unsupported link configuration: {link}")
                continue
            if link.startswith("http"):
                pass  # external link
            elif link.startswith("/"):
                pass  # absolute link
            else:
                if link.endswith(".md"):
                    search = link[:-3]
                else:
                    search = link
                found = [p for p in posts if p.file.name == search]
                if not found:
                    print(f"unresolved link {search}")
                    continue
                link = found[0].abs_url
                title = found[0].title

            links.append({"title": title, "url": link})
        context["links"] = links
    return context
