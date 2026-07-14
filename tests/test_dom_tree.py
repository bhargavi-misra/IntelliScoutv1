from app.browser.browser import Browser
from app.parser.dom_cleaner import DOMCleaner
from app.parser.dom_tree import DOMTree

browser = Browser()
cleaner = DOMCleaner()
tree = DOMTree()

html = browser.get_html("https://books.toscrape.com")

clean = cleaner.clean(html)

print(tree.simplify(clean))