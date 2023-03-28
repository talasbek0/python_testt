import requests

from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as file:
     src = file.read()
print(src)
soup = BeautifulSoup(src, "lxml")

page_h1 = soup.find("h1")
print(page_h1.text)

for item in page_all_h1:
    print(item.text)         не выведется

user_name = soup.find("div", class="user__name")
print(user__name.text.strip())

user_name = soup.find("div", {"class" : "user_name","id":"dopolnitelnyi"}).find("span")
print(user__name.text.strip())

find_all_spans_in_user__info = soup.find(
     class_="user__info").find_all("span")
print(find_all_spans_in_user__info)

for item in find_all_spans_in_user__info:
     print(item.text)

social_link = soup.find(class_="social__networks").find("ul").find_all("a")
print(social_link)

all_a = soup.find_all("a")
print(all_a)

for item in all_a:
     item_url = item.text
     item_url = item.get("href")
     print(item_url)

next_elemen = soup.find(class_="post__title").next_element\
     .next_element.text
print(next_elemen)


links = soup.find(class_="some__links").find_all("a")
print(links)

for link in links:
     link_href_attr = link.get("href")
     link_data_attr = link.get("data-attr")
     print(link_data_attr)
     print(link_data_attr)

find_by_text = soup.find("a", text="Одежда для взрослых")
print(find_by_text.text)

find_a_by_text = soup.find("a", text=re.compile("Одежда"))
print(find_a_by_text)

finnd_compile_registr =  soup.find_all(text=re.compile("([Оо]дежда)"))
print(finnd_compile_registr)


