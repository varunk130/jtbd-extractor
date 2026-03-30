const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 1200, deviceScaleFactor: 2 });
  
  const filePath = path.join(__dirname, 'jtbd-overview.html');
  await page.goto(`file:///${filePath.replace(/\\/g, '/')}`, { waitUntil: 'networkidle0' });
  
  // Wait for fonts and animations
  await new Promise(r => setTimeout(r, 2000));
  
  // Clip to hero + pipeline + 3 job cards
  const clipHeight = await page.evaluate(() => {
    const jobs = document.querySelector('.jobs-grid');
    const rect = jobs.getBoundingClientRect();
    return rect.bottom + 48; // add padding
  });
  
  await page.screenshot({
    path: path.join(__dirname, 'assets', 'jtbd-overview.png'),
    clip: { x: 0, y: 0, width: 1400, height: clipHeight },
    type: 'png'
  });
  
  console.log(`Screenshot saved (${clipHeight}px tall)`);
  await browser.close();
})();
