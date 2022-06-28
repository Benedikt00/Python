from playwright.sync_api import Playwright, sync_playwright
import asyncio
from bs4 import BeautifulSoup
import time
from time import sleep


file_object = open('test', 'a')

run = True

while run:
        with sync_playwright() as playwright:
                browser = playwright.chromium.launch(headless=False)
                context = browser.new_context()
                # Open new page
                page = context.new_page()

                page.goto("http://192.168.0.4/")

                page.goto("http://192.168.0.4/#/login")
                sleep(8)

                page.locator('text="-- Benutzer auswählen --"', force=True).click()


                page.fill('input[name="password"]', "Einstein123")


                with page.expect_navigation():
                    page.click("button:has-text(\"Login\")")

                sleep(2)


                html = page.content()
                soup = BeautifulSoup(html, 'html.parser')
                var = soup.find("div", {"id": "thumb_power_value"}).text
                print(var)

                time_object = time.localtime()
                local_date = time.strftime("%y %m %d", time_object)


                local_time = time.strftime("%H:%M:%S ", time_object)

                file = open('test', 'a')
                file.write(var + " " +  str(local_time) + " "+ str(local_date) + "\n")

                context.close()
                browser.close()




