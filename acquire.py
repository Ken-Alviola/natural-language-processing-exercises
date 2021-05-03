import numpy as np
import pandas as pd
from requests import get
from bs4 import BeautifulSoup
import os



def get_blog_articles(url_list):
    article_list = []
    for url in url_list:
        url = url
        headers = {'User-Agent': 'Codeup Data Science'}
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.text)
        article = soup.find('div', class_='jupiterx-main-content')
        title = article.find('h1').text
        content = article.find_all('p')
        content_list = [x.text for x in content]
        content = ' '.join(content_list)
        dictionary = {
            'title': title,
            'content': content
        }
        article_list.append(dictionary)
    return article_list


def get_news_articles(url):
    response = get(url)
    soup = BeautifulSoup(response.text)
    card_stack = soup.find('div', class_='card-stack')
    cards = card_stack.find_all('div', class_='news-card z-depth-1')
    
    article_list = []
    
    for card in cards:
        title = card.find('span', itemprop='headline').text
        content = card.find('div', itemprop='articleBody').text
        author = card.find('span', class_='author').text
        dictionary = {'title': title,
                      'author': author,
                      'content': content
                      }
        article_list.append(dictionary)
        
    return article_list