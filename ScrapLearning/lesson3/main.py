import json
import requests
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "user-agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }

    # req = requests.get(url, headers)
    # # print(req.text)

    # with open("products.html", "w", encoding="utf-8") as file:
    #     file.write(req.text)

    with open("products.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    articles = soup.find_all(class_="car-block")
    # print(maxsulotlar)


    project_urls = []
    for article in articles:
        project_url = "https://mediapark.uz" + article.find("div", class_="car-block-main").find("a", class_="product_list_img").get("href")
        project_urls.append(project_url)


    projects_data_list = []
    for project_url in project_urls:
        req = requests.get(project_url, headers)
        project_name = project_url.split("/")[-1]

        with open(f"data/{project_name}.html", "w", encoding="utf8") as file:
            file.write(req.text)
        
        with open(f"data/{project_name}.html", encoding="utf8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        project_data = soup.find("div", class_="Catalog-information-right-start")
        # print(project_data)

        try:  
            project_logo = "https://mediapark.uz" + project_data.find("span", class_="catalog-brend-logo").get("style").split("background-image:url(")[-1].split(")")[-2]
                    
        except Exception:
            project_logo = "No project logo "

        try:
            project_name = project_data.find("div", class_="Catalog-information-right-block-left-center-info").find("h4").text
            
        except Exception:
            project_name = "No project name"
        
        try:
            project_short_requemnts = project_data.find("div", class_="add-Catalog-information-right-main2-start-left").find("p").text
            
        except Exception:
            project_short_requemnts = "No project short req"

        try:
            project_order = "https://mediapark.uz" + project_data.find("div", class_="Catalog-information-right-block-right-buttoms").find("a", class_="Catalog-information-buttom-1").get("href")

        except Exception:
            project_order = "No project order"

        projects_data_list.append(
            {
                "Proekt nomi": project_name,
                "Logotip URL manzili": project_logo,
                "Kichkina ma'lumot": project_short_requemnts,
                "Sotib olish URL": project_order
            }
        )
    with open("data/projects_data.json", "a", encoding="utf-8") as file:
        json.dump(projects_data_list, file, indent=4, ensure_ascii=False)

get_data("https://mediapark.uz/products/category/128")
