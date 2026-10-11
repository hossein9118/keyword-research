# Persian Keyword Research & SERP Clustering Pipeline

A Python pipeline that turns a single **Persian seed keyword** into a **content plan**: it expands the seed into hundreds of long-tail search terms, scrapes Google's top-10 results for each, groups keywords that share the same search intent, and outputs a list of articles to write — with the words each article title should contain.

> Built in 2023 for real SEO projects in the Persian-language market, where most commercial keyword tools have poor coverage.

## Why

Commercial tools like Ahrefs or Semrush have thin data for Persian queries. Google itself knows best which queries belong together: if two keywords return mostly the same top-10 URLs, one page can rank for both. This pipeline uses that signal to cluster keywords by **SERP overlap** instead of by text similarity.

## How it works

```
seed keyword
   │
   ▼
[1] Expand ──► Google Autocomplete, seed + each Persian letter (prefix & suffix),
   │           optional 2-letter depth  → searchterms.csv
   ▼
[2] Expand again ──► repeat expansion on every result, with checkpointing
   │                 → searchterms2.csv
   ▼
[3] Scrape SERPs ──► top-10 URLs and titles for each keyword, with
   │                 block detection & back-off  → links.csv, titles.csv
   ▼
[4] Similarity matrix ──► pairwise overlap of top-10 URLs, tiered rules
   │                      (full top-10, top-2, top-4, top-5 + same #1 result)
   │                      → similars.parquet
   ▼
[5] Rank ──► sort keywords by how many others they cluster with
   │
   ▼
[6] Build content plan ──► greedy clustering into articles; for each article,
                           extract words common across competitors' titles
                           → articles.csv
```

| Step | Script | Output |
|---|---|---|
| 1 | `legacy/step-1.py` | Autocomplete expansion of the seed keyword |
| 2 | `legacy/step-2.py` | Second-level expansion (resumable) |
| 3 | `legacy/step-3.py` | Google SERP scraping — top-10 links & titles |
| 4 | `legacy/step-4.py` | Keyword × keyword SERP-similarity matrix |
| 5 | `legacy/step-5.py` | Sort by cluster size |
| 6 | `legacy/step-6.py` | Article clusters + suggested title words |

## Usage

```bash
pip install pandas beautifulsoup4 lxml requests pyarrow
cd legacy
python step-1.py   # prompts for seed keyword and depth (1 or 2)
python step-2.py
python step-3.py
python step-4.py
python step-5.py
python step-6.py   # → articles.csv
```

Each step reads the previous step's output from the working directory.

## Notes & limitations

- This is the **legacy** version, written as sequential scripts; a refactor into a single CLI with config is planned.
- Scraping Google directly is rate-limited; step 3 detects the block page and backs off, but large runs are slow. For production use, a SERP API is recommended.
- The similarity matrix is O(n²) in the number of keywords.

## Tech

`Python` · `pandas` · `BeautifulSoup` · `requests` · `Parquet`

---
Made by [Hossein Hosseini](https://www.linkedin.com/in/hossein-hosseini/) — Growth & SEO.
