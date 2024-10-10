# from bs4 import BeautifulSoup
# import requests
# import pprint

# PS03
# # ///////////ПАРСИНГ ЦИТАТ////////////////
# # Отличие функции find и find all:
# # Find all — ищет все значения с заданным тегом и классом
# # Find — ищет первое с заданным тегом и классом
#
# url = "http://quotes.toscrape.com/"
# response = requests.get(url)
# html = response.text
#
# soup = BeautifulSoup(html, "html.parser")
#
# #Создадим отдельную переменную text, куда будут сохраняться все цитаты
# text = soup.find_all("span", class_="text")
# print(text)
#
# #Создадим отдельную переменную author, куда будут сохраняться все авторы
# author = soup.find_all("small", class_="author")
# print(author)
#
# #С помощью функции range(len) определим общее количество цитат
# for i in range(len(text)):
# #Присвоим номер каждой цитате так, чтобы нумерация шла с 1
#     print(f"Цитата номер - {i + 1}")
# #Выводим саму цитату, указывая её id
#     print(text[i].text)
# #Выводим автора цитаты
#     # print(f"Автор цитаты - {author[i].text}")
#     print(f"Автор цитаты - {author[i].text}\n")

# ///////////ПАРСИНГ ССЫЛОК////////////////
# # Отправляем гет-запрос (кроме динамического JS контента и защищенных от веб-скраппинга):
#
# # url = "http://quotes.toscrape.com/"
# # response = requests.get(url)
# # html = response.text
# #
# # soup = BeautifulSoup(html, "html.parser") #сюда нужно будет передавать HTML-код страницы
# # "html.parser" — это один из трёх видов парсера. Это встроенный парсер, остальные требуют отдельной установки. Парсеры отличаются по эффективности, по скорости работы, по их обработке ошибок на сайте.
#
# # Находим информацию с сайта:
# # links = soup.find_all("a")
# # for link in links:
# #     print(link)
#
# links = soup.find_all("a")
# for link in links:
#     print(link.get('href'))


# /////////////////////3. Отправка данных.PS02
# url = "https://jsonplaceholder.typicode.com/posts"
#
# data = {'title': 'foo', 'body': 'bar', 'userId': 1}
#
# response = requests.post(url, json=data)
#
#
# print(f"Status code: {response.status_code}")
# print(f"ответ - {response.json}")
# ////////////////////////
# params = {
#     "q": "python"
# }
# response = requests.get("https://randomfox.ca/floof", params=params)
# # response = requests.get("https://www.google.com")
#
# print(response)
# print(response.status_code)
# print(response.ok)

# if response.ok:
#     print('pос успешно выполнен')
# else:
#     print('произошла ошибка')

# print(response.text)
# print(response.content)
# response_json = response.json()
# pprint.pprint(response_json)
# print(f"количество репозиториев с использованием питона: {response_json['total_count']}")
