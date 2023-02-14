from selenium import webdriver
from selenium.webdriver.common.by import By
# docker run --rm -d -p 4444:4444 --shm-size=2g selenium/standalone-chrome

mangaName = input("enter manga name: ").replace(' ','_').lower()
driver = webdriver.Remote('http://localhost:4444/wd/hub', options=webdriver.ChromeOptions())
driver.set_window_size(1280, 1024)
driver.get(f"https://www.mangago.me/read-manga/{mangaName}/")

# driver.find_element(By.partialLinkText("click to show all of the chapters")).click()
driver.find_element(By.XPATH,'//a[contains(@onclick,"showAllChapters()")]').click()
chapterElements = driver.find_elements(By.CLASS_NAME, "chico")
chaptersList = []
for chapter in chapterElements:
    chaptersList.append(chapter.text)
driver.quit()

def chaptersFunc(chaptersList):
    newList = []
    if len(chaptersList) > 5:
        newList = chaptersList[3:]
    elif len(chaptersList) == 4:
        newList = chaptersList[2:]
    else:
        newList = chaptersList[1:]
    return newList

def updateCheck(chaptersList, mangaName):
    # chapterCheck = open(f"{mangaName}","w+")
    # if not chapterCheck.readable():
    #     newChapter = open(f"{mangaName}","x")
    text = open(f"{mangaName}.txt", "a+")
    if text.read() == str(chaptersList):
        print("no updates")
    else:
        chapterFile = open(f"{mangaName}.txt", "w")
        chapterFile.write(str(chaptersList))
        print("new chapters!")

updateCheck(chaptersList, mangaName)
print(chaptersFunc(chaptersList))
