from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

# Function to scrape data
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Scraping logic - use BeautifulSoup to find and extract various types of content
    # Note: This might not work perfectly due to JavaScript-generated content
    texts = [element.text for element in soup.find_all(['p', 'a', 'img'])]
    links = [element.get('href') for element in soup.find_all('a') if element.get('href')]
    images = [element.get('src') for element in soup.find_all('img') if element.get('src')]

    max_length = max(len(texts), len(links), len(images))
    texts += [None] * (max_length - len(texts))
    links += [None] * (max_length - len(links))
    images += [None] * (max_length - len(images))

    data = {'Text': texts, 'Links': links, 'Images': images}
    df = pd.DataFrame(data)
    print(df)

    return df

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form['search_query']
        url = f"https://www.youtube.com/results?search_query={search_query}"
        df = scrape_data(url)
        return render_template('index.html', data=df.to_html(), search_query=search_query)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)