from bs4 import BeautifulSoup

def soupThePage(page): 
    return BeautifulSoup(page.content, 'lxml')
