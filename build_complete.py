import sys
import os

from sections.styles import CSS_CONTENT
from sections.html_screens import SCREENS_CONTENT
from sections.dialogs import DIALOGS_CONTENT
from sections.scripts import SCRIPTS_CONTENT

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Badminton Cup — Pro Tournament Suite & Admin Platform</title>
<meta name="description" content="Pro Badminton Tournament Suite with live umpire scoring, BWF rules, draft machine, group & knockout brackets, stats, authentication, and global admin dashboard.">
<meta name="theme-color" content="#0d1f2d">
<link rel="manifest" href="manifest.json">
<link rel="icon" type="image/svg+xml" href="icons/icon.svg">

<!-- Modern Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

<!-- Canvas Confetti CDN -->
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

{CSS_CONTENT.strip()}
</head>
<body>

{SCREENS_CONTENT.strip()}

{DIALOGS_CONTENT.strip()}

{SCRIPTS_CONTENT.strip()}

</body>
</html>
"""

output_path = '/Users/rashed/badminton-cup/index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(HTML_TEMPLATE)

print(f"Successfully generated {output_path} ({len(HTML_TEMPLATE)} bytes)")
