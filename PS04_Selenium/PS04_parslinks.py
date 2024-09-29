from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time

# Функция для поиска статей на Википедии
def search_wikipedia(query):
    browser.get("https://ru.wikipedia.org")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "firstHeading"))
        )
    except Exception as e:
        print("Статья не найдена:", e)
        return False
    return True
# Функция для листания параграфов статьи
def print_paragraphs():
    paragraphs = browser.find_elements(By.CSS_SELECTOR, "div.mw-parser-output > p")
    for i, p in enumerate(paragraphs):
        print(f"\nПараграф {i + 1}:\n", p.text)
        if i % 3 == 2: # Показываем по 3 параграфа за раз
            user_input = input("\nНажмите Enter для продолжения или введите 'q', чтобы вернуться к выбору: ")
            if user_input.lower() == 'q':
                break

# Функция для выбора и перехода по внутренним ссылкам
def navigate_to_link():
    links = browser.find_elements(By.CSS_SELECTOR, "div.mw-parser-output a")
    internal_links = []


    for i, link in enumerate(links):
        href = link.get_attribute("href")
        # Проверяем, есть ли атрибут href и начинается ли он с ссылки на Википедию
        if href and href.startswith("https://ru.wikipedia.org/wiki/"):
            internal_links.append((i, link))

    if not internal_links:
        print("Не удалось найти внутренние ссылки на этой странице.")
        return False

    for i, link in internal_links[:10]:  # Показываем первые 10 ссылок
        print(f"{i + 1}. {link.text} ({link.get_attribute('href')})")

    choice = input("\nВведите номер ссылки для перехода или 'q' для выхода: ")
    if choice.isdigit():
        link_index = int(choice) - 1
        if 0 <= link_index < len(internal_links):
            internal_links[link_index][1].click()
            return True
    return False

# Основной цикл программы
def main():
    while True:
        query = input("Введите запрос для поиска на Википедии (или 'q' для выхода): ")
        if query.lower() == 'q':
            break


        if search_wikipedia(query):
            while True:
                print("\nВыберите действие:")
                print("1. Листать параграфы текущей статьи.")
                print("2. Перейти на одну из связанных страниц.")
                print("3. Выйти из программы.")

                choice = input("\nВведите номер действия: ")

                if choice == '1':
                    print_paragraphs()
                elif choice == '2':
                    if not navigate_to_link():
                        print("Некорректный ввод или не удалось найти ссылку.")
                elif choice == '3':
                    print("Выход из программы.")
                    return
                else:
                    print("Некорректный выбор. Попробуйте снова.")
if __name__ == "__main__":
    browser = webdriver.Chrome() # Создаем экземпляр браузера

    try:
        main()
    finally:
        browser.quit()  # Закрываем браузер после завершения программы

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# # Функция для поиска статей на Википедии
# browser = webdriver.Chrome()
# def search_wikipedia(query):
#     browser.get("https://ru.wikipedia.org")
#     search_box = browser.find_element(By.ID, "searchInput")
#     search_box.send_keys(query)
#     search_box.send_keys(Keys.RETURN)
#     try:
#         WebDriverWait(browser, 10).until(
#             EC.presence_of_element_located((By.ID, "firstHeading"))
#         )
#     except Exception as e:
#         print("Статья не найдена:", e)
#         return False
#     return True
#
# # Функция для листания параграфов статьи
# def print_paragraphs():
#     paragraphs = browser.find_elements(By.CSS_SELECTOR, "div.mw-parser-output > p")
#     for i, p in enumerate(paragraphs):
#         print(f"\nПараграф {i + 1}:\n", p.text)
#         if i % 3 == 2: # Показываем по 3 параграфа за раз
#             user_input = input("\nНажмите Enter для продолжения или введите 'q', чтобы вернуться к выбору: ")
#             if user_input.lower() == 'q':
#                 break
#
# # Функция для выбора и перехода по внутренним ссылкам
# def navigate_to_link():
#     links = browser.find_elements(By.CSS_SELECTOR, "div.mw-parser-output a")
#     internal_links = [(i, link) for i, link in enumerate(links) if link.get_attribute("href").startswith("https://ru.wikipedia.org/wiki/")]
#
#     for i, link in internal_links[:10]: # Показываем первые 10 ссылок
#         print(f"{i + 1}. {link.text} ({link.get_attribute('href')})")
#
#     choice = input("\nВведите номер ссылки для перехода или 'q' для выхода: ")
#     if choice.isdigit():
#         link_index = int(choice) - 1
#         if 0 <= link_index < len(internal_links):
#             internal_links[link_index][1].click()
#             return True
#     return False
# # Основной цикл программы
# def main():
#     while True:
#         query = input("Введите запрос для поиска на Википедии (или 'q' для выхода): ")
#         if query.lower() == 'q':
#             break
#
#         if search_wikipedia(query):
#             while True:
#                 print("\nВыберите действие:")
#                 print("1. Листать параграфы текущей статьи.")
#                 print("2. Перейти на одну из связанных страниц.")
#                 print("3. Выйти из программы.")
#
#                 choice = input("\nВведите номер действия: ")
#
#                 if choice == '1':
#                     print_paragraphs()
#                 elif choice == '2':
#                     if not navigate_to_link():
#                         print("Некорректный ввод или не удалось найти ссылку.")
#                 elif choice == '3':
#                     print("Выход из программы.")
#                     return
#                 else:
#                     print("Некорректный выбор. Попробуйте снова.")
#
# if __name__ == "__main__":
#     browser = webdriver.Chrome() # Создаем экземпляр браузера
#
#     try:
#         main()
#     finally:
#         browser.quit() # Закрываем браузер после завершения программы