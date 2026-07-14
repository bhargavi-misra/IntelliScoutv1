from app.agent.extractor import Extractor

html = """
<body>

<div class="container">

    <article class="product_pod">

        <h3>
            <a>A Light in the Attic</a>
        </h3>

        <p class="price_color">£51.77</p>

        <p class="instock availability">In stock</p>

    </article>

    <article class="product_pod">

        <h3>
            <a>Tipping the Velvet</a>
        </h3>

        <p class="price_color">£53.74</p>

        <p class="instock availability">In stock</p>

    </article>

</div>

</body>
"""

plan = {
    "container": "article.product_pod",
    "fields": {
        "title": "h3 a",
        "price": "p.price_color",
        "availability": "p.instock.availability"
    }
}

extractor = Extractor()

items = extractor.extract(html, plan)

print(items)