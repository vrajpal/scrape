"""Use beatiful soup to parse a page"""
from bs4 import BeautifulSoup

def soup_the_page(page):
    """
    Parses the content of a given page using BeautifulSoup with the 'lxml' parser.

    Args:
        page (requests.Response): The page response object containing the content to be parsed.

    Returns:
        BeautifulSoup: A BeautifulSoup object representing the parsed HTML content.
    """
    return BeautifulSoup(page.content, 'lxml')
