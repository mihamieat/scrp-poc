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
    click.echo(f"Found name: {find_text(html, 'Name: ')}")
    click.echo(f"Found favourite coulour: {find_text(html, 'Favorite Color:')}")


def find_text(raw_html, text_to_find):
    """
    Finds and extracts text content from HTML.

    Args:
        html (str): The HTML content to search within.
        text_to_find (str): The text to locate within the HTML.

    Returns:
        str: The extracted text content stripped of leading and trailing whitespace characters.
    """

    text_index = raw_html.find(text_to_find)
    start_index = text_index + len(text_to_find)
    next_html_tag_offset = raw_html[start_index:].find("</")
    end_index = start_index + next_html_tag_offset
    raw_text = raw_html[start_index:end_index]
    return raw_text.strip(" \r\n\t")
