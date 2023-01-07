from bs4 import BeautifulSoup

import json, csv, time, random

##__прочитали и сохранили HTML в переменный src
with open("7_Кондитерские_изделия.html", "r") as file:
    src = file.read()

##__передали в BeautifulSoup src и добавили обработчик lxml
soup = BeautifulSoup(src, "lxml")
# print(soup)

##__ мы нашли класс таблицы и нашли внутри thead а внутри нашли tr и внутри нашли th с помощью find_all
##__ find_all мы указываем find_all когда нужно вытащить сразу все схожие значения и обернуть в [список]
# title_table = soup.find(class_="mzr-tc-group-table").find("thead").find("tr").find_all("th")
# print(title_table)

# title = []
# for item in title_table:
#     title.append(item.text)


# with open("title.csv", "w", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         title
#     )

row_table = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
row_product = []

for item in row_table:
    product_info_item = item.find_all("td")

    product_name = product_info_item[0].text
    product_calories = product_info_item[1].text
    product_proteins = product_info_item[2].text
    product_fats = product_info_item[3].text
    product_carbohydrates = product_info_item[4].text
    
    with open(f"title.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        writer.writerow(
                (
                    product_name,
                    product_calories,
                    product_proteins,
                    product_fats,
                    product_carbohydrates,
                )
            )

