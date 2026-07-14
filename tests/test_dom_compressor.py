from app.parser.dom_compressor import DOMCompressor

html = """
<body>

<div class="container">

    <article class="product_pod">

        <h3>
            <a href="#">
                A Light in the Attic
            </a>
        </h3>

        <p class="price_color">
            £51.77
        </p>

        <p class="instock availability">
            In stock
        </p>

    </article>

</div>

</body>
"""

compressor = DOMCompressor()

print(compressor.compress(html))