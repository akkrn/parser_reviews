import logging
import sys

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def format_text(text: str) -> str:
    """Форматирование текста отзыва."""
    return text.replace("\n\n", "\n")


def start_parsing(url: str, soup: BeautifulSoup) -> None:
    """Запускает браузер для прохождения капчи и собирает отзывы."""
    driver = webdriver.Chrome()
    while True:
        try:
            driver.get(url)
            html = driver.page_source
            if soup.find("div", {"class": "CheckboxCaptcha"}):
                logging.warning("Обнаружена капча")
                input("Пройдите капчу и нажмите Enter")
            soup = BeautifulSoup(html, "html.parser")
            page = soup.find_all("select", {"class": "navigator_per_page"})
            count = page[-1].text.split()[-1]
            url += f"/ord/date/status/all/perpage/{count}/ "
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            reviews = soup.find_all("span", {"class": "_reachbanner_"})
            if not reviews:
                logging.error(f"Не удалось получить отзывы со страницы {url}")
                raise ValueError("Отсутствуют отзывы на странице")
            if len(reviews) > 0:
                with open("reviews.txt", "w", encoding="utf-8") as file:
                    for review in reviews:
                        text = format_text(review.text)
                        file.write(text + "\n\n")
                break
        except Exception as e:
            logging.error(f"Ошибка: {e}")
        finally:
            driver.quit()


def main() -> None:
    """Получает id фильма и передает их для парсинга"""
    try:
        movie_id = int(input("Введите id фильма, отзывы, которого хотите получить: "))
        if movie_id <= 297:
            raise ValueError("Фильмов с id меньше 297 на Кинопоиске нет")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите положителньое целое число")
        return main()
    url = f"https://www.kinopoisk.ru/film/{movie_id}/reviews"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Какая-то ошибка, возможно такой страницы не существует.", e)
        return main()
    soup = BeautifulSoup(response.content, "html.parser")
    start_parsing(url, soup)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        filename="main.log",
        filemode="w",
        format="%(asctime)s, %(levelname)s, %(message)s, %(name)s, %(lineno)d",
    )
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)
    main()
