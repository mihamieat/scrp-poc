# -*- coding: utf-8 -*-
"""Beautiful soup package."""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import click


URL = "http://olympus.realpython.org/profiles/dionysus"
with urlopen(URL) as page:
    html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
image1, image2 = soup.find_all("img")


def print_parser():
    """
    Print parsed content from BeautifulSoup object.

    This function prints the text content of the BeautifulSoup object,
    the names and sources of two images, and the title of the parsed content.

    Args:
        None

    Returns:
        None
    """
    click.echo(soup.get_text())
    click.echo(f"{image1.name} {image2.name}")
    click.echo(f"{image1['src']} {image2['src']}")
    click.echo(f"Title: {soup.title.string}")
