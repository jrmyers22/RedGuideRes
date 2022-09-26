# Sample
# https://dataquestio.github.io/web-scraping-pages/simple.html
#
# https://www.opentable.com/s?dateTime=2022-09-30T19%3A30%3A00&covers=2&latitude=40.80973&longitude=-73.981298&term=batard%20nyc

# dateTime = 2022-09-30T19:30:00
# covers = 2
# term = batard nyc
#
#
# https://www.opentable.com/r/batard-new-york?&p=2&sd=2022-09-30T19%3A00%3A00
# p=2
# sd=2022-09-30T19:30:00


import requests

headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    }
page = requests.get("https://www.opentable.com/r/batard-new-york?&p=2&sd=2022-09-30T19%3A00%3A00", headers=headers, timeout=5)
# print(page.content)

f = open("page_contents2.txt", "a")
f.write(str(page.content))
f.close()
print("Successfully wrote content")


# from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
