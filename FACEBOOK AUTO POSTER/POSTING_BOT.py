import os
import time
import asyncio
import warnings
import pandas as pd
from pyppeteer import launch
from Facebook import Facebook_Bot


warnings.filterwarnings("ignore", category=RuntimeWarning, module="pyppeteer")




async def main():
    browser = await launch({
        'executablePath': r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", # CHANGE THIS PATH IF REQUIRED
        'headless': False,
        'userDataDir': r"C:\Users\HP\Desktop\ChromeProfileClone",  # ENTER YOUR CLONED PROFILE FOLDER HERE
        'args': [
            '--no-sandbox',
            '--disable-infobars',
            '--disable-blink-features=AutomationControlled',
            '--disable-extensions-except',
            '--no-first-run',
            '--no-default-browser-check',
        ]
    })

    
    page = await browser.newPage()


    await page.goto("https://web.facebook.com/", {"timeout": 0,"waitUntil": "networkidle2"})
    await Facebook_Bot(page)


    await browser.close()
asyncio.run(main())


