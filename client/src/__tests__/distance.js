const puppeteer = require('puppeteer');

test('Test Distance', async () => {
	let browser = await puppeteer.launch({
		headless: false
	});
	let page = await browser.newPage();

	await page.goto('http://localhost:3000/distance');
	await page.waitForSelector('.location1 .latitude');
	await page.type('.location1 .latitude', '0');
	await page.type('.location1 .longitude', '0');
	await page.type('.location2 .latitude', '1');
	await page.type('.location2 .longitude', '1');
	await page.click('.submit');
	await page.waitForSelector('.alert.alert-primary');
	const result = await page.$eval('.alert', el => el.innerText);
	expect(result.substring(0, 6)).toBe('Result');

	browser.close();
}, 16000);