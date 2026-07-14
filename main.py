import app.database.database

from app.manager.scraper_manager import ScraperManager
from app.repositories.book_repository import BookRepository

manager = ScraperManager()

books = manager.run(
    scraper_name="books",
    url="https://books.toscrape.com/"
)

repository = BookRepository()

repository.save_all(books)

print(f"Books in database: {repository.count()}")

print()

for book in repository.get_all()[:5]:
    print(book)