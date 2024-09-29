from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера (в данном случае используется Chrome)
driver = webdriver.Chrome()

# Получение первоначального запроса от пользователя
initial_query = input("Введите поисковый запрос: ")

# Переход на страницу Википедии с первоначальным запросом
wiki_url = f"https://ru.wikipedia.org/wiki/{initial_query}"
driver.get(wiki_url)

while True:
    # Ожидание загрузки страницы
    wait = WebDriverWait(driver, 10)
    paragraph_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p")))

    # Вывод параграфов текущей статьи
    for i, paragraph in enumerate(paragraph_elements, start=1):
        print(f"{i}. {paragraph.text}")

    # Предложение пользователю вариантов действий
    choice = input("Выберите действие (1 - листать параграфы, 2 - перейти на связанную страницу, 3 - выйти): ")

    if choice == "1":
        continue
    elif choice == "2":
        # Получение списка ссылок на связанные страницы
        link_elements = driver.find_elements(By.CSS_SELECTOR, "a")
        related_links = [link.get_attribute("href") for link in link_elements if link.text]

        # Вывод списка связанных страниц
        for i, link in enumerate(related_links, start=1):
            print(f"{i}. {link}")

        # Выбор связанной страницы
        link_choice = int(input("Выберите номер связанной страницы: "))
        driver.get(related_links[link_choice - 1])
    elif choice == "3":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")

# Закрытие веб-драйвера
driver.quit()
