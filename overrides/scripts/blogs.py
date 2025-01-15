def on_page_context(context, page, config, nav):
    # if page.meta.get("template") != "category.html": return 

    context["posts"] = config["plugins"]["material/blog"].blog.posts
    return context
