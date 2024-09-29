# from selenium import webdriver
#
# from selenium.webdriver import Keys  #Библиотека, которая позволяет вводить данные на сайт с клавиатуры
# from selenium.webdriver.common.by import By #Библиотека с поиском элементов на сайте
#
# import time  # С помощью time мы можем делать задержки в программе
# import random #for 3part hatnotes
#
# #Если мы работаем с Chrome
# browser = webdriver.Chrome()
# #Если мы работаем с Firefox
# # browser = webdriver.Firefox()
#
# # browser.get("https://en.wikipedia.org/wiki/Document_Object_Model") #В кавычках указываем URL сайта, на который нам нужно зайти
# # browser.save_screenshot("dom.png") #В кавычках указываем название, которое присвоится скриншоту
# # time.sleep(5)  #Задержка в 10 секунд
# # # browser.quit() #Закрываем браузер
# #
# # browser.get("https://ru.wikipedia.org/wiki/Selenium")
# # browser.save_screenshot("selenium.png")
# # time.sleep(3)
# # browser.refresh()
#
# # browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
# #Проверяем по заголовку, тот ли сайт открылся
# # assert "Википедия" in browser.title
# # # time.sleep(5)
# # #Находим окно поиска
# # search_box = browser.find_element(By.ID, "searchInput")
# # #Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
# # search_box.send_keys("Солнечная система")
# # #Добавляем не только введение текста, но и его отправку
# # search_box.send_keys(Keys.RETURN)
# # time.sleep(5)
# #
# # a = browser.find_element(By.LINK_TEXT, "Солнечная система")
# #
# # # find_element находит первый попавшийся элемент, подходящий под условия поиска.
# # # find_elements находит несколько элементов.
# #
# # #Добавляем клик на элемент
# # a.click()
#
# # работа с контентом. переход по ссылкам Программа выдает рандомные статьи о солнечной системе из Википедии.
# browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")
# paragraphs = browser.find_elements(By.TAG_NAME, "p")
# # #Для перебора параграфов пишем цикл
# # for paragraph in paragraphs:
# #     print(paragraph.text)
# #     input()
#
# hatnotes = []
# for element in browser.find_elements(By.TAG_NAME, "div"):
# #Чтобы искать атрибут класса
#     cl = element.get_attribute("class")
#     if cl == "hatnote navigation-not-searchable":
#         hatnotes.append(element)
#
# print(hatnotes)
# hatnote = random.choice(hatnotes)
#
# #Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
# link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
# browser.get(link)