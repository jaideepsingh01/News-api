import requests
import tkinter as tk


def getNews():
    api_key="52dcb4aac106437cbcd52c65e3ddae65"
    url=" https://newsapi.org/v2/top-headlines?country=nz&apiKey=52dcb4aac106437cbcd52c65e3ddae65"
    news=requests.get(url).json()

    articles=news["articles"]

    my_articles=[]
    my_news=""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news= my_news+ str(i+1)+ ". "+ my_articles[i]+ "\n"

    label.config(text=my_news)

canvas=tk.Tk()
canvas.geometry("1200x600")
canvas.title("News App")

button=tk.Button(canvas, font=24, text="Reload", command=getNews)
button.pack(pady=20)

label=tk.Label(canvas,font=18,justify="left")
label.pack(pady=20)

getNews()

canvas.mainloop()
