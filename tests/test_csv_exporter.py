from app.exporter.csv_exporter import CSVExporter

items = [
    {
        "title": "Book 1",
        "price": "£20",
        "availability": "In stock"
    },
    {
        "title": "Book 2",
        "price": "£30",
        "availability": "Out of stock"
    }
]

exporter = CSVExporter()

path = exporter.export(
    items,
    "books.csv"
)

print(path)