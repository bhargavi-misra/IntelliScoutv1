# IntelliScout

**Extract structured data from any website using plain English — no CSS selectors, no config.**

IntelliScout is an AI-assisted web extraction agent. Give it a URL and describe what you want in natural language (*"product name, price and rating"*, *"internship title, company, location and stipend"*), and it returns clean, structured JSON — exportable to CSV.

Live demo: [intelli-scoutv1.vercel.app](https://intelli-scoutv1.vercel.app)

---

## How it works

Most LLM scrapers send the entire page to the model for every request — slow, expensive, and prone to inventing data that isn't there. IntelliScout splits the job into two distinct stages instead:

```
URL + natural language prompt
        │
        ▼
┌───────────────────┐
│  1. Render         │  Playwright loads the page (headless Chromium),
│     (Browser)      │  waits for network idle, handles JS-rendered content
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  2. Clean          │  Strip scripts, nav, ads, cookie banners,
│     (DOMCleaner)    │  socials, and other boilerplate
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  3. Compress        │  Reduce the cleaned HTML to a compact structural
│     (DOMCompressor) │  skeleton (tags, ids, classes, key attributes,
│                     │  truncated text) to minimize LLM token usage
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  4. Plan (cached)  │  An LLM sees ONLY the compressed skeleton + your
│     (Planner)       │  prompt, and returns a JSON extraction plan:
│                     │  a container selector, per-field selectors, and
│                     │  an optional item limit. It never sees real data.
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  5. Extract         │  A deterministic BeautifulSoup routine applies the
│     (Extractor)     │  plan to the real cleaned HTML to pull actual values
└───────────────────┘
        │
        ▼
   Structured JSON  →  optional CSV export
```

**Why this matters:**
- The LLM is only ever asked to describe *structure* (selectors), never to report *values* — this removes most of the hallucination risk you'd get from asking an LLM to "read off" data directly.
- Extraction plans are **cached to disk**, keyed by a hash of the URL and a normalized version of the prompt. Repeat requests for the same site/intent skip the LLM call entirely, cutting cost and latency.
- Sending a compressed DOM skeleton instead of raw HTML significantly reduces the tokens sent to the model per request.

---

## Features

- **Natural-language extraction** — describe what you want; no selectors or scraping code required
- **JavaScript-rendered site support** via Playwright/Chromium
- **Noise removal** — strips scripts, nav, footers, ads, cookie banners, and social/related-content blocks before the DOM ever reaches the model
- **Plan caching** — avoids redundant LLM calls for repeated (URL, prompt) combinations
- **CSV export** — download extracted results as a spreadsheet-ready file
- **Copy-as-JSON** — copy structured results directly from the UI
- Clean modular backend: browser / parser / agent (planner + extractor) / cache / exporter / LLM client, each independently unit-tested

---

## Tech Stack

**Backend**
- FastAPI (REST API)
- Playwright (headless browser rendering)
- BeautifulSoup4 + lxml (HTML parsing/cleaning/extraction)
- Google Gemini (`google-genai`) for extraction planning
- Disk-based JSON cache for extraction plans
- pytest for unit tests

**Frontend**
- Next.js 16 / React 19
- Tailwind CSS
- Framer Motion (animated background: starfield, moon glow, mascot)

**Deployment**
- Backend: Docker + Railway
- Frontend: Vercel

---

## Project Structure

```
IntelliScoutv1/
├── app/
│   ├── agent/
│   │   ├── engine.py          # Orchestrates the full extraction pipeline
│   │   ├── planner.py         # Builds the LLM prompt, returns a selector plan
│   │   ├── extractor.py       # Applies the plan to HTML with BeautifulSoup
│   │   └── utils.py           # Robust JSON extraction from LLM responses
│   ├── api/
│   │   ├── main.py            # FastAPI app + CORS config
│   │   └── routes/
│   │       └── extraction.py  # POST /extract, POST /extract/csv
│   ├── browser/
│   │   └── browser.py         # Playwright page rendering
│   ├── cache/
│   │   └── planner_cache.py   # Disk-based plan cache (SHA-256 keyed)
│   ├── exporter/
│   │   └── csv_exporter.py    # Writes extracted items to CSV
│   ├── llm/
│   │   ├── base.py            # LLM client interface
│   │   └── openai_client.py   # Gemini client (see Known Issues)
│   ├── models/
│   │   ├── request.py         # Pydantic model for /extract
│   │   └── csv_request.py     # Pydantic model for /extract/csv
│   └── parser/
│       ├── dom_cleaner.py     # Removes noise (scripts, nav, ads, etc.)
│       ├── dom_compressor.py  # Compact structural DOM representation
│       └── dom_tree.py        # Simple tag-tree debug view
├── frontend/                  # Next.js app (UI, mascot, results panel)
├── tests/                     # Unit tests for each backend module
├── Dockerfile
├── railway.json
└── requirements.txt
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- A Google Gemini API key

### Backend

```bash
git clone https://github.com/bhargavi-misra/IntelliScoutv1.git
cd IntelliScoutv1

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
playwright install chromium

# Create a .env file:
echo "OPENAI_API_KEY=your_gemini_api_key_here" > .env
echo "GEMINI_MODEL=models/gemini-flash-latest" >> .env

uvicorn app.api.main:app --reload
```

The API will be available at `http://localhost:8000`.

> **Note:** the environment variable is currently named `OPENAI_API_KEY` for historical reasons, but it must contain a **Google Gemini** API key 

### Frontend

```bash
cd frontend
npm install

# Create .env.local:
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

npm run dev
```

The app will be available at `http://localhost:3000`.

### Running tests

```bash
pytest tests/
```

---

## API Reference

### `POST /extract`

Extract structured data from a URL using a natural-language prompt.

**Request**
```json
{
  "url": "https://example.com/products",
  "prompt": "product name, price and availability"
}
```

**Response**
```json
{
  "items": [
    { "name": "Widget A", "price": "$19.99", "availability": "In stock" },
    { "name": "Widget B", "price": "$24.99", "availability": "Out of stock" }
  ]
}
```

### `POST /extract/csv`

Convert a previously extracted list of items into a downloadable CSV file.

**Request**
```json
{
  "items": [
    { "name": "Widget A", "price": "$19.99" }
  ]
}
```

**Response:** `text/csv` file stream.

---

## Known Issues & Limitations

- **No anti-bot handling:** sites behind Cloudflare, login walls, or aggressive rate limiting are not specifically handled.
- **Single-page extraction only:** no crawling, pagination, or multi-page workflows yet.

---

