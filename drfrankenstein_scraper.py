import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
import re
import os

QUBITTORRENT_URLS = [
    "https://drfrankenstein.co.uk/qbittorrent-container-manager-on-a-synology-nas/"
]

PROWLARR_FLARESOLVERR_URLS = [
    "https://drfrankenstein.co.uk/prowlarr-and-flaresolverr-in-container-manager-on-a-synology-nas/"
]

PLEX_HW_TRANSCODING_URLS = [
    "https://drfrankenstein.co.uk/plex-in-container-manager-on-a-synology-nas-hardware-transcoding/"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; drfrankenstein-scraper/1.0)"
}

def get_soup(url):
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")

def is_screenshot(img_tag):
    alt = img_tag.get('alt', '').lower()
    src = img_tag.get('src', '').lower()
    return 'screenshot' in alt or 'screenshot' in src or 'screen' in alt or 'screen' in src

def extract_article(url):
    soup = get_soup(url)
    main = None
    possible_content_locations = [
        soup.find('div', class_='post-content'),
        soup.find('div', class_='entry-content'),
        soup.find('article'),
        soup.find('div', class_='content'),
        soup.find('main'),
        soup.find('div', class_=re.compile(r'(content|main|article)', re.I))
    ]
    for location in possible_content_locations:
        if location:
            main = location
            break
    if not main:
        return None
    paragraphs = []
    for p in main.find_all(['p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        text = p.get_text(strip=True)
        if text and not any(x in text.lower() for x in ['comment', 'email', 'website', 'required fields']):
            paragraphs.append(text)
    code_blocks = []
    for code in main.find_all(['pre', 'code']):
        text = code.get_text(strip=True)
        if text:
            code_blocks.append(text)
    images = []
    for img in main.find_all('img'):
        src = img.get('src')
        if src:
            images.append({
                "url": urljoin(url, src),
                "is_screenshot": is_screenshot(img)
            })
    external_links = []
    for a in main.find_all('a', href=True):
        href = a['href']
        if not href.startswith('#') and 'drfrankenstein.co.uk' not in href:
            external_links.append(href)
    return {
        "url": url,
        "paragraphs": paragraphs,
        "code_blocks": code_blocks,
        "images": images,
        "external_links": external_links
    }

def crawl_qubittorrent_guides():
    print("Scraping qBittorrent guide...")
    articles = []
    for url in QUBITTORRENT_URLS:
        print(f"Scraping: {url}")
        article = extract_article(url)
        if article:
            articles.append(article)
        else:
            print(f"Could not extract content from {url}")
    with open('qubittorrent_guides.json', 'w') as f:
        json.dump(articles, f, indent=2)
    print("Scraping complete. Output saved to qubittorrent_guides.json")

def crawl_prowlarr_flaresolverr_guides():
    print("Scraping Prowlarr and FlareSolverr guide...")
    articles = []
    for url in PROWLARR_FLARESOLVERR_URLS:
        print(f"Scraping: {url}")
        article = extract_article(url)
        if article:
            articles.append(article)
        else:
            print(f"Could not extract content from {url}")
    with open('prowlarr_flaresolverr_guides.json', 'w') as f:
        json.dump(articles, f, indent=2)
    print("Scraping complete. Output saved to prowlarr_flaresolverr_guides.json")

def crawl_plex_hw_transcoding_guides():
    print("Scraping Plex hardware transcoding guide...")
    articles = []
    for url in PLEX_HW_TRANSCODING_URLS:
        print(f"Scraping: {url}")
        article = extract_article(url)
        if article:
            articles.append(article)
        else:
            print(f"Could not extract content from {url}")
    with open('plex_hw_transcoding_guides.json', 'w') as f:
        json.dump(articles, f, indent=2)
    print("Scraping complete. Output saved to plex_hw_transcoding_guides.json")

if __name__ == "__main__":
    crawl_qubittorrent_guides()
    crawl_prowlarr_flaresolverr_guides()
    crawl_plex_hw_transcoding_guides() 