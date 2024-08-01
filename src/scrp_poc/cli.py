# -*- coding: utf-8 -*-
"""Command line interface entrypoint"""
import click
from .text_extractor import print_page


@click.command
def main():
    """
    A command line interface for the scraper app.

    This function serves as the entry point for the CLI, \
echoing a message and calling the print_page function.
    """
    click.echo("My scraper app.")
    print_page()
