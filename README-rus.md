<div><a href="https://github.com/akkrn/parser_reviews/blob/main/README.md" ><img alt="ru" src="https://img.shields.io/badge/version-on%20english-white"/></a></div>

<details open><summary><h2>📚 Описание</h2></summary>

Данный проект предназначен для автоматического сбора всех отзывов на интересующий фильм с сайта Кинопоиск. Для обхода капчи в ручном режиме подключен Selenium. Для поиска фильма необходимо знать его ID
</details>

<details><summary><h2>🛠️ Стэк технологий</h2></summary>
<img src="https://img.shields.io/badge/Python-%2314354c.svg?logo=Python&logoColor=white&style=flat" alt="Python" /> <img src="https://img.shields.io/badge/Selenium-%23009639.svg?style=flat&logo=selenium&logoColor=white" alt="Selenium" />


</details>
<details><summary><h2>🏗️ Развертывание</h2></summary>


Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:akkrn/parser_reviews.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```


Запустить проект:

```
python3 main.py 
```

Ввести ID интересующего вас фильма

</details>

