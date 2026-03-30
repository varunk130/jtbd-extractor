from playwright.sync_api import sync_playwright
import os

html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'jtbd-overview.html')
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'jtbd-overview.png')
os.makedirs(os.path.dirname(out_path), exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1400, 'height': 1200}, device_scale_factor=2)
    page.goto(f'file:///{html_path.replace(os.sep, "/")}', wait_until='networkidle')
    page.wait_for_timeout(2000)

    # Get bounding box of jobs grid (includes hero + pipeline + 3 cards)
    clip_height = page.evaluate('''() => {
        const jobs = document.querySelector('.jobs-grid');
        const rect = jobs.getBoundingClientRect();
        return rect.bottom + 48;
    }''')

    page.screenshot(
        path=out_path,
        clip={'x': 0, 'y': 0, 'width': 1400, 'height': clip_height},
        type='png'
    )
    print(f'Screenshot saved: {out_path} ({clip_height}px tall)')
    browser.close()
