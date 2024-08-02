# -*- coding: utf-8 -*-
"""Regex sooup package."""

import re
from urllib.request import urlopen
import click

URL = "http://olympus.realpython.org/profiles/dionysus"
with urlopen(URL) as page:
    html = page.read().decode("utf-8")

PATTERN = "<title.*?>.*?</title.*?>"
match_results = re.search(PATTERN, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)


def print_results():
    """
    Prints the title extracted from the results.

    This function prints the extracted title.
    """

    click.echo(f"***Regex results from {URL}***")
    click.echo(f"title: {title}")
