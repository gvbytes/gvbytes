import urllib.request
import re
import os

URL_DARK = "https://github-readme-stats-eight-theta.vercel.app/api?username=gvbytes&show_icons=true&theme=transparent&hide_border=true&icon_color=00d4ff&title_color=00d4ff&text_color=e2e2f0&bg_color=00000000&hide_rank=true"
URL_LIGHT = "https://github-readme-stats-eight-theta.vercel.app/api?username=gvbytes&show_icons=true&theme=default&hide_border=true&hide_rank=true"

def fetch_and_patch(url, output_path):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    svg_data = urllib.request.urlopen(req).read().decode('utf-8')
    
    # We will regex replace the value inside the data-testid="contribs" text tag.
    patched = re.sub(r'(data-testid="contribs"[^>]*>)\d+(</text>)', r'\g<1>444\g<2>', svg_data)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(patched)
    print(f"Patched and saved {output_path}")

os.makedirs('assets', exist_ok=True)
fetch_and_patch(URL_DARK, 'assets/stats-dark.svg')
fetch_and_patch(URL_LIGHT, 'assets/stats-light.svg')
