# Python Flask http web server

A simple demo of Python used as a web server

## Dependencies

- python 3.4.3
- flask  0.10.1
- pip 9.0.1

## Installation

Install python3 and pip for your distro

https://www.python.org/downloads/
https://pip.pypa.io/en/stable/installing/

Install flask

```bash
    pip install flask
```

## Getting started

Git clone this repo, cd into the new directory
run the app.py file

```bash 
    python3 app.py
     * Running on http://127.0.0.1:5000/
    127.0.0.1 - - [11/Jun/2017 13:43:20] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [11/Jun/2017 13:43:25] "GET /loginView HTTP/1.1" 200 -
    127.0.0.1 - - [11/Jun/2017 13:43:47] "POST /login HTTP/1.1" 200 -
```
Open an internet browser with the url http://127.0.0.1:5000/ and you will see the cli update as you browse