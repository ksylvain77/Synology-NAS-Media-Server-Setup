import os
import json
import requests
from urllib.parse import urlparse
from pathlib import Path

# Input and output JSON files
INPUT_JSON = 'plex_hw_transcoding_guides.json'
OUTPUT_JSON = 'plex_hw_transcoding_guides_with_images.json'

# Section name for organizing images
SECTION_NAME = 'plex_hw_transcoding'

def setup_section_directory():
    """Create the section directory if it doesn't exist"""
    section_dir = Path('images') / SECTION_NAME
    section_dir.mkdir(parents=True, exist_ok=True)
    return section_dir

def should_exclude_image(url):
    """Check if the image should be excluded based on its URL"""
    excluded_patterns = ['kofi', 'bmc', 'discord']
    return any(pattern in url.lower() for pattern in excluded_patterns)

def download_image(url, section_dir):
    """Download an image and return its local path"""
    if should_exclude_image(url):
        print(f"Skipping excluded image: {os.path.basename(url)}")
        return None
        
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Get filename from URL
        filename = os.path.basename(urlparse(url).path)
        local_path = section_dir / filename
        
        # Save the image
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"Downloaded: {url} -> {local_path}")
        return str(local_path)
        
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return None

def main():
    # Create section directory
    section_dir = setup_section_directory()
    
    # Load articles from JSON
    with open(INPUT_JSON, 'r') as f:
        articles = json.load(f)
    
    # Process each article
    for article in articles:
        # Download images and update paths
        if 'images' in article:
            local_images = []
            for img in article['images']:
                if isinstance(img, dict) and 'url' in img:
                    url = img['url']
                else:
                    url = img
                local_path = download_image(url, section_dir)
                if local_path:
                    local_images.append(local_path)
            article['local_images'] = local_images
    
    # Save updated articles to new JSON file
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(articles, f, indent=2)
    
    print(f"Updated JSON with local image paths saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    main() 