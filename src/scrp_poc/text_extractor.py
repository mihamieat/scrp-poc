# -*- coding: utf-8 -*-
"""Text extractor package."""
from urllib.request import urlopen
import click


URL = "http://olympus.realpython.org/profiles/aphrodite"
with urlopen(URL) as page:
    html_bytes = page.read()
html_str = html_bytes.decode("utf-8")
title_index = html_str.find("<title>")
start_index = title_index + len("<title>")
end_index = html_str.find("</title>")
title_str = html_str[start_index:end_index]


def print_page():
    """
    Prints various extracted page elements.

    This function prints different page elements such as the HTML content, \
title index, start index length, end index, and title string.
    """

    click.echo(f"***Text extractor from {URL}***")
    click.echo(f"#######\npage code:\n#######\n\n{html_str}\n")
    click.echo(f"#######\ntitle index scraped:\n#######\n\n{title_index}\n")
    click.echo(f"#######\nstart index lenght scraped:\n#######\n\n{start_index}\n")
    click.echo(f"#######\nend index scraped:\n#######\n\n{end_index}\n")
    click.echo(f"#######\ntitle:\n#######\n\n{title_str}\n")
