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

# Grab the full HTML from the page at the URL
URL2 = "http://olympus.realpython.org/profiles"
with urlopen(URL2) as page2:
    html2 = page2.read().decode("utf-8")
soup2 = BeautifulSoup(html2, "html.parser")
hyperlinks = soup2.find_all("a")
hrefs = [a["href"] for a in hyperlinks]
links = [URL2 + href for href in hrefs]


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
    click.echo("\n".join(links))
