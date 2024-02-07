from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://islamqa.info/en/categories/very-important/120/answers/46505/islam-erases-the-sins-that-came-before-it"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

title = soup.find(class_="title is-4 is-size-5-touch")
question = soup.find(class_="single_fatwa__question text-justified")
answer = soup.find(class_="single_fatwa__answer")

data = [[title.text, question.text, answer.text]]
df = pd.DataFrame(data, columns=["title", "question", "answer"])
print(df)
df.to_csv("Assignment #05.csv", index=False)
print("ok")