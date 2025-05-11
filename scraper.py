# Extract images
images = []
for img in soup.find_all('img'):
    src = img.get('src', '')
    if src:
        # Skip images that start with excluded prefixes
        excluded_prefixes = ['kofi', 'BMC', 'Discord']
        if not any(src.startswith(prefix) for prefix in excluded_prefixes):
            images.append(src)

# Extract code blocks 