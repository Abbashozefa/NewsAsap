from flask import Flask,render_template,request

import requests
app=Flask(__name__)


@app.route("/")
def welcome():
    
    url = 'https://newsapi.org/v2/everything?q=Latest+News&sortBy=popularity&apiKey=e21c28ebd4ff471e970182ebc9da81fd'
    latest_news = requests.get(url).json()
    a = latest_news['articles']
    desc =[]
    title =[]
    img =[]
    for i in range(len(a)):
          f = a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
    return render_template('index.html',mylist = zip(title, desc, img))

@app.route("/news",methods=['POST'])
def news():
    news=str(request.form['topic'])
    url = 'https://newsapi.org/v2/everything?q='+news+'&sortBy=popularity&apiKey=e21c28ebd4ff471e970182ebc9da81fd'
    latest_news = requests.get(url).json()
    a = latest_news['articles']
    desc =[]
    title =[]
    img =[]
    for i in range(len(a)):
          f = a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
    
    
    return render_template('index.html',mylist = zip(title, desc, img))


if __name__  == "__main__":
    app.run(host='0.0.0.0',port=4000)
