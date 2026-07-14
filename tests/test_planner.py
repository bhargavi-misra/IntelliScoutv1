from app.agent.planner import Planner
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

compressed_dom = compressor.compress(html)

planner = Planner()

plan = planner.create_plan(
    "Extract the title, price and availability of every book.",
    compressed_dom
)

print(plan)