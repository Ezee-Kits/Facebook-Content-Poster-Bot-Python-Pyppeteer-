import time
import asyncio
import pyperclip

from func import css_click_center,xpath_click_center



async def Facebook_Bot(page):
    await page.bringToFront()
    await xpath_click_center(page, '//span[contains(text(), "What\'s on your mind")]')

    file_input = await page.waitForSelector('input[type="file"]', {'visible': False})
    await asyncio.sleep(1.5)
    img = r'C:\Users\HP\Pictures\front cover.PNG'    #### PUT YOUR IMAGE PATH HERE
    await file_input.uploadFile(*img) 
    await asyncio.sleep(2)


    fb_box = await page.waitForXPath('//div[@role="textbox" and @contenteditable="true"]')
    await fb_box.click()
    await asyncio.sleep(1)
    await fb_box.click()
    await asyncio.sleep(1)



    text_content = f"""

    #### WRITE YOUR CONTENTS/TEXTS HERE

    """


    pyperclip.copy(text_content)
    await asyncio.sleep(1)
    await fb_box.click()
    await page.keyboard.down('Control')
    await page.keyboard.press('V')
    await page.keyboard.up('Control')
    await asyncio.sleep(2)

    try:
        next_btn = await page.waitForXPath('//div[@role="button" and @aria-label="Next"]')
        await next_btn.click()
    except:
        post_btn = await page.waitForXPath('//div[@aria-label="Post" and @role="button"]')
        await post_btn.click()

    await asyncio.sleep(2)
    await xpath_click_center(page, '//div[@aria-label="Post" and @role="button"]')
    await asyncio.sleep(3)



 