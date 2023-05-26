
<div><a href="https://github.com/akkrn/parser_reviews/blob/main/README-rus.md" ><img alt="ru" src="https://img.shields.io/badge/%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F-%D0%BD%D0%B0%20%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC-white"/></a></div>
<details open><summary><h2>📚 Description</h2></summary>
This project is designed to automatically collect all reviews on the film of interest from the site Kinopoisk. To bypass the captcha in manual mode, Selenium is connected. To search for a movie, you need to know its ID
  
</details>

<details><summary><h2>🛠️ Tech Stack</h2></summary>

<img src="https://img.shields.io/badge/Python-%2314354c.svg?logo=Python&logoColor=white&style=flat" alt="Python" /> <img src="https://img.shields.io/badge/Selenium-%23009639.svg?style=flat&logo=selenium&logoColor=white" alt="Selenium" />


</details>
<details><summary><h2>🏗️ Installation</h2></summary>

Clone the repository and go to it on the command line:

```
git clone git@github.com:akkrn/parser_reviews.git
```

Create and activate a virtual environment:

```
python3 -m venv venv
```

* If you have Linux/macOS

    ```
    source venv/bin/activate
    ```

* If you have windows

    ```
    source venv/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Install dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```


Run the project:

```
python3 main.py 
```

Enter the ID of the movie you are interested in

</details>
