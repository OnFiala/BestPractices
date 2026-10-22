"""Resolve language alternatives per page for both HTML metadata and the menu."""

import posixpath


def on_page_context(context, page, config, nav):
    current = "" if config.theme["language"] == "en" else config.theme["language"] + "/"
    for alternate in config.extra["alternate"]:
        locale = "" if alternate["lang"] == "en" else alternate["lang"] + "/"
        alternate["link"] = "https://onfiala.github.io/BestPractices/" + locale + page.url
        alternate["local"] = posixpath.relpath(locale + page.url or ".",
                                               current + page.url or ".") + "/"
    return context
