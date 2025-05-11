# DrFrankenstein.co.uk Web Scraper

This project scrapes main articles, code snippets, screenshots, and relevant external links (e.g., ProtonVPN) from selected sections of https://drfrankenstein.co.uk/.

## Setup

1. **Clone this repository or copy the files to your folder.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the scraper with:

```bash
python drfrankenstein_scraper.py
```

- The output will be saved to `drfrankenstein_guides.json` in the current directory.
- The script extracts:
  - Main article text
  - Code snippets
  - Image URLs (screenshots flagged)
  - Summaries of relevant external links (e.g., ProtonVPN)

## Notes
- Only the main content area of each relevant page is scraped (no navigation, footers, or ads).
- You can modify the `SECTIONS` list in `drfrankenstein_scraper.py` to target different sections. 