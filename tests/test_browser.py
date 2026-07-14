from app.browser.browser import Browser

browser = Browser()

html = browser.get_html(
    "https://books.toscrape.com"
)

print(html[:1000])