# Manga-Update-Checker
Uses selenium and python to check for manga updates. Future plans to add UI using kivy, currently works as standalone python file.
Requires docker and selenium.

## How to Start
### To Clone Repository
`git clone https://github.com/kevinxiao27/Manga-Update-Checker`

### Set Up
Installing selenium
`pip install selenium`
Installing and running containerized Chrome with docker
`docker pull selenium/standalone-chrome`
`docker run --rm -d -p 4444:4444 --shm-size=2g selenium/standalone-chrome`

### Available Scripts
`python scrapper.py`
Runs Manga Scrapper
