import time
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright_stealth import stealth_sync
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

def lastPgae(html):
    soup = BeautifulSoup(html, 'html.parser')
    list1 = soup.find_all('span', class_='ScreenReaderText-sc-8934b9de-0 hjmRnY')
    for i, element in enumerate(list1):
        if 'Go to Page' in element.text:
            Page = i
            break  # Exit the loop once the first occurrence is found

    return int(list1[Page].text.strip().replace('\n', '').split()[-1])

def visitSite(site,pageNumber):

    sitewithpages = f'{site}?page={pageNumber}'
    # print(sitewithpages)
    page.goto(sitewithpages)

    try:
        # Try to click the element
        time.sleep(7)
        page.get_by_text("Before we continue...Press &").click(timeout=7000)
        print("Clicked the element")
    except Exception as e:
        print(f"Element not found or clickable: {e}")
        # Handle the case where the element is not found or clickable
        pass

    time.sleep(1)
    html_content = page.content()

    # file_path = os.path.join(r'F:\Fuego\Weedmaps - Price - Analysis', f'page_{pageNumber}.html')
    # with open(file_path, 'w', encoding='utf-8') as file:
    #     file.write(html_content)

    return html_content


def data(html_content, Location, site):
    ##the website should be : https://weedmaps.com/deliveries/{store}?page={page#}
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.title
    lists = soup.find_all('li', class_='ListingItemContainer-sc-bc60ce4c-2 gaGQcA')
    ITEMLISTING = {
                    'Location': [],
                    'URL': [],
                    'shop': [],
                    'dateExtracted': [],
                    'categories': [],
                    'items': [],
                    'brand': [],
                    'originalPrice': [],
                    'currentPrice': [],
                    'discountedPrice': []

    }
    title = soup.title.text.strip().replace('\n', '')

    for divs in lists:

        shop = title
        Loc = Location
        url = site
        dateExtracted = datetime.now().strftime('%Y-%m-%d')

        category = divs.find('div',
                             class_='Text-sc-42ad1a7e-0 Category-sc-4c64daca-16 imQoHe OkGhV').text.strip().replace(
            '\n', '')
        item = divs.find('div',
                         class_='Text-sc-42ad1a7e-0 Title-sc-4c64daca-8 BaseCardTitle-sc-bc60ce4c-21 dLuYLn gTxfNd GmMbw').text.strip().replace(
            '\n', '')

        #Brand
        if divs.find('div', class_='Text-sc-42ad1a7e-0 BrandNameText-sc-bc60ce4c-20 fdubtO drCIal') is not None:
            brand = divs.find('div',
                              class_='Text-sc-42ad1a7e-0 BrandNameText-sc-bc60ce4c-20 fdubtO drCIal').text.strip().replace(
                '\n', '')
        else:
            brand = ""

        ##Original price
        if  divs.find('div', class_='Text-sc-42ad1a7e-0 PriceText-sc-529f235-1 OriginalPriceText-sc-529f235-2 kefpUT gntSdp fcqczC') is not None:
            originalPrice = divs.find('div',
                              class_='Text-sc-42ad1a7e-0 PriceText-sc-529f235-1 OriginalPriceText-sc-529f235-2 kefpUT gntSdp fcqczC').text.strip().replace(
        '\n', '')
        else:
            originalPrice = ""

        ##currentPrice
        if  divs.find('div', class_='Text-sc-42ad1a7e-0 PriceText-sc-529f235-1 dYLrWB gntSdp') is not None:
            currentPrice = divs.find('div',
                              class_='Text-sc-42ad1a7e-0 PriceText-sc-529f235-1 dYLrWB gntSdp').text.strip().replace(
        '\n', '')
        elif divs.find('div', class_='Text-sc-42ad1a7e-0 PriceText-sc-529f235-1 kbEdqg gntSdp') is not None:

            currentPrice = divs.find('div',
                                     class_='Text-sc-42ad1a7e-0 PriceText-sc-529f235-1 kbEdqg gntSdp').text.strip().replace(
                '\n', '')

        else:
            currentPrice = ""

        ##discounted price
        if  divs.find('div', class_='Text-sc-42ad1a7e-0 PriceText-sc-529f235-1 dYLrWB gyRTCr') is not None:
            discountedPrice = divs.find('div',
                              class_='Text-sc-42ad1a7e-0 PriceText-sc-529f235-1 dYLrWB gyRTCr').text.strip().replace(
        '\n', '')
        else:
            discountedPrice = ""

        ITEMLISTING['Location'].append(Loc)
        ITEMLISTING['URL'].append(url)
        ITEMLISTING['shop'].append(shop)
        ITEMLISTING['dateExtracted'].append(dateExtracted)
        ITEMLISTING['categories'].append(category)
        ITEMLISTING['items'].append(item)
        ITEMLISTING['brand'].append(brand)
        ITEMLISTING['originalPrice'].append(originalPrice)
        ITEMLISTING['currentPrice'].append(currentPrice)
        ITEMLISTING['discountedPrice'].append(discountedPrice)

    return ITEMLISTING


def run(playwright: Playwright, site, first, last, Location) -> None:
    # browser = playwright.firefox.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    stealth_sync(page)
    page.goto(site)


    #for antibot
    try:
        # Try to click the element
        page.get_by_text("Before we continue...Press &").click(timeout=7000)
        print("Clicked the element")
    except Exception as e:
        print(f"Element not found or clickable: {e}")
        # Handle the case where the element is not found or clickable
        pass

    time.sleep(3)

    try:
        page.locator("[data-test-id=\"age-gate-confirm-accept\"]").click(timeout=2000)
    except Exception as e:
        print(f"Age gate confirmation button not found or not clickable: {e}")
        pass  # Proceed if the button is not found or not clickable

    time.sleep(5)

    try:
        page.get_by_test_id("cookie-banner-accept").click(timeout=2000)
    except Exception as e:
        print(f"cookie banner gate confirmation button not found or not clickable: {e}")
        pass  # Proceed if the button is not found or not clickable


    html_content = page.content()

    soup = BeautifulSoup(html_content, 'lxml')
    prettifyHtml = soup.prettify()

    all_data = []



    for i in range(first,last+1):

        htmlcontent = visitSite(site, i)
        page_data = data(htmlcontent, Location, site)
        all_data.append(page_data)

    # Combine all data into a single DataFrame

    combined_data = {
        'Location': [],
        'URL': [],
        'shop': [],
        'dateExtracted': [],
        'categories': [],
        'items': [],
        'brand': [],
        'originalPrice': [],
        'currentPrice': [],
        'discountedPrice': []
    }

    for page_data in all_data:
        for key in combined_data.keys():
            combined_data[key].extend(page_data[key])

    df = pd.DataFrame(combined_data)
    shop = site.split("deliveries/")[1].replace("-", " ")
    df.to_csv(rf'F:\Fuego\Weedmaps - Price - Analysis\update\{shop} {Location} {first}-{last}.csv', index=False)


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    sites = [
                'https://weedmaps.com/deliveries/purple-lotus-31'

             ]
    Location = ['Dublin']

    for site, Loc in zip(sites,Location):
        run(playwright, site, 21, 25, Loc)

