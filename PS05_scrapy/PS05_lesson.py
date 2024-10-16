# pip install --upgrade pip
# PyCharm есть шаблоны для проектов, но платно. Делаем аналог ручками

# 1. Добавьте путь к Scripts в переменную PATH
# Используйте python -m venv

# pip install scrapy
# scrapy startproject divanpars (Powershell)
# cd C:\Users\el\Documents\2024\Git_PythonProject\pythonProject\PS05_scrapy\divanpars

# 2. Выполните команду scrapy genspider
# Теперь, когда вы находитесь в корневом каталоге проекта, выполните команду для генерации нового паука:

# powershell
# scrapy genspider divannewpars divan.ru

# Объяснение команды:

#     divannewpars — это имя вашего нового паука.
#     divan.ru — это домен, который будет использоваться для настройки атрибутов allowed_domains и start_urls вашего паука.

# 3.     Использование Scrapy Feed Exports
# Когда вы запускаете паука (spider), вы можете сразу задать формат вывода данных, добавив параметр в команду запуска:

#   scrapy crawl divannewpars -o divany.csv

# Это самый простой способ, так как Scrapy уже включает встроенную поддержку экспорта данных в CSV.
#  команда автоматически сохранит все собранные данные в CSV-файл с именем divany.csv.


# Команды в терминале:

#     fetch(’ссылка’) — используется, чтобы загрузить веб-страницу. После использования покажется статус-код;
#     response.css(’h2’) — поиск всех элементов с тегом h2;
#     response.css(’h2.vFBoK’) — поиск элементов по названию класса. Указываем тег, ставим точку, указываем название класса;
#     response.css(’div.LlPhw’) — поиск по тегу. Будет создан целый список;
#     response.css(’div.LlPhw’).get() — выбор только первого элемента из списка;
#     divan = response.css(’div.LlPhw’) — создаём переменную, в которую сохранится список из поиска по тегу;
#     len(divan) — считаем, сколько диванов было найдено по тегу;
#     divan1 = divan[0] — выбираем элемент из списка по его индексу (индексы начинаются с 0);
#     divan1.css(’div’) — получаем все теги div от этого элемента.

