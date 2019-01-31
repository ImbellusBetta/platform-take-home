/**
 * Tests the Geocode Container
 */
const puppeteer = require('puppeteer');

test('Test Geocode', async () => {
	let browser = await puppeteer.launch({
		headless: false
	});
	let page = await browser.newPage();

	await page.goto('http://localhost:3000/geocode');
	await page.waitForSelector('.address');
	await page.type('.address', '1 Jackson St, Petone, Lower Hutt, NZ');
	await page.click('.addressCard .submit');
	await page.waitForSelector('.addressCard .alert.alert-primary');
	const result = await page.$eval('.addressCard .alert', el => el.innerText);
	expect(result.substring(0, 6)).toBe('Result');

	browser.close();
}, 16000);

test('Test Reverse Geocode', async () => {
	let browser = await puppeteer.launch({
		headless: false
	});
	let page = await browser.newPage();

	await page.goto('http://localhost:3000/geocode');
	await page.waitForSelector('.address');
	await page.type('.latitude', '-41.2225081');
	await page.type('.longitude', '174.869802');
	await page.click('.locationCard .submit');
	await page.waitForSelector('.locationCard .alert.alert-primary');
	const result = await page.$eval('.locationCard .alert', el => el.innerText);
	expect(result.substring(0, 6)).toBe('Result');

	browser.close();
}, 16000);
