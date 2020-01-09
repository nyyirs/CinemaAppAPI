<h1 align="center">
  <img src="https://pngimage.net/wp-content/uploads/2018/06/rolo-de-filme-cinema-vector-png-2.png" alt="Cinema" width="200">
  <br>
  Cinema REST API
  <br>
</h1>

<h4 align="center">A simple web scrapping rest api for Cinema App built on top of <a href="https://www.pythonorg/" target="_blank">Python</a>.</h4>

<p align="center">
<img alt="PyPI" src="https://img.shields.io/badge/Django-3.0.1-green">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/djangorestframework?color=Blue&label=DjangoRestFramework">
  <img alt="PyPI" src="https://img.shields.io/badge/BeautifulSoup-4.8.0-blue">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/requests?color=Green&label=Requests">
</p>

# Overview

<p>A Web Service carefully crafted to serve as a backend for a Mobile Application. It relies heavily on web scraping technology to harvest data from a known website and transforms them into readable JSON format.</p>

<p>The REST API is hosted on AWS with the help of Docker images</p>


```bash
# Pull docker image from docker hub
docker pull nyyirs/cinema-rest-api

```

```bash
# Run the docker image
docker run -d -p 8000:8000 cinema-rest-api python /app/manage.py runserver 0.0.0.0:8000

```

# Features

* Extract Movie:
  - Title
  - Poster Image
  - Movie Details Link
  - Date and Time 
  - Hall
  - Language (Original or French Version)
  - 2D or 3D





