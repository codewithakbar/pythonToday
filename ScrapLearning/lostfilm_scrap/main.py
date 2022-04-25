import json
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4972.0 Safari/537.36"
}

def collect_data():

    ofset = 0
    batch_size = 1180
    for i in range(ofset, ofset + batch_size):
        url = f"https://www.lostfilm.tv/new/page_{i}"

        # print(url)
        response = requests.get(
            url=url,
            headers=headers
        )

        ofset += batch_size


        







