from app.agent.engine import IntelliScoutEngine


engine = IntelliScoutEngine()

items = engine.extract(
    url="https://books.toscrape.com/",
    prompt="Extract title, price and availability of every book."
)

print("\n========== RESULTS ==========\n")

for item in items:
    print(item)