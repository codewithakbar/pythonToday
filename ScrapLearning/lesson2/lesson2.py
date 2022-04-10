import re
import csv
import json
import random
import requests
from time import sleep
from turtle import title
from bs4 import BeautifulSoup


# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"

}

# req = requests.get(url, headers=headers)

# src = req.text
# # print(src)

# with open("index.html", "w", encoding="utf-8-sig") as file:
#     file.write(src)


# with open("index.html", encoding="utf8") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")
# all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")

# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")

#     all_categories_dict[item_text] = item_href  

# with open("all_categories_dict.json", "w", encoding="utf8") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


with open("all_categories_dict.json", encoding="utf8") as file:
    all_categories = json.load(file)


interation_count = int(len(all_categories)) - 1
count = 0
print(f"Vsevo iteratsie: {interation_count}")
for category_name, category_href in all_categories.items():


    rep = [",", " ", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{category_name}.html", "w", encoding="utf8") as file:
        file.write(src)

    with open(f"data/{count}_{category_name}.html", encoding="utf8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    # proverka stranitsi na nalichie tablitsi s productam
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue


    # sobirayem zagalovki tablizi
    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    product = table_head[0].text
    colories = table_head[1].text
    protenies = table_head[2].text
    fats = table_head[3].text
    corbonathydrates = table_head[4].text
    
    with open(f"data/{count}_{category_name}.csv", "w", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                colories,
                protenies,
                fats,
                corbonathydrates
            )
        )

    # sobiraem dannie producda
    protducts_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
    
    product_info = []
    for item in protducts_data:
        protduct_tds = item.find_all("td")

        title = protduct_tds[0].find("a").text
        colories = protduct_tds[1].text    
        protenies = protduct_tds[2].text
        fats = protduct_tds[3].text
        corbonathydrates = protduct_tds[4].text

        product_info.append(
            {
                "Title": title,
                "Calories": colories,
                "Proteins": protenies,
                "Fats": fats,
                "Carbohydrates": corbonathydrates
            }
        )

        with open(f"data/{count}_{category_name}.csv", "a", encoding="utf8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    colories,
                    protenies,
                    fats,
                    corbonathydrates
                )
            )
    with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)


    count += 1
    print(f"# Iteration {count}, {category_name} zapisan...")
    interation_count = interation_count - 1


    if interation_count == 0:
        print(f"Rabota zaqonchina")
        break


    print(f"Ostalsya iteratsie: {interation_count}")
    sleep(random.randrange(2, 4))



