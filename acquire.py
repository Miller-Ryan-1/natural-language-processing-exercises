import pandas as pd
import numpy as np
import re
import requests
from bs4 import BeautifulSoup as bs

def acquire_codeup_blog():
    '''
    Scrapes the Codeup website for 5 random blogs on the front blog page and pulls key info out
    '''
    
    # Create a header for access
    headers = {'User-Agent': 'Codeup Data Science'}
    
    # Create a list of 5 distinct random numbers
    a = range(15)
    blog_posts = np.random.choice(a, size=5, replace=False, p=None)
    blog_posts = blog_posts
    blog_posts = list(blog_posts)

    # Create the soup object for the hompage
    r = requests.get('https://codeup.com/blog/', headers = headers)
    soup = bs(r.content, 'html.parser')

    # Find all the blog entry urls on homepage, put into list 'blog_links
    blog_list = soup.find_all('h2', attrs={'class':'entry-title'})
    blog_links = []
    for n in blog_posts:
        blog = blog_list[n]
        blog_links.append(blog.a["href"])

    # Loop through blog pages using their direct urls and pull out important info
    blogs_info = []
    for blog in blog_links:
        blog_info = {}
        r = requests.get(blog, headers = headers)
        soup = bs(r.content, 'html.parser')
        blog_info['Title'] = soup.find('h1', attrs = {'class':'entry-title'}).text
        blog_info['Published'] = soup.find('span', attrs = {'class' : 'published'}).text
        blog_info['Content'] = soup.find('div', attrs = {'class' : 'entry-content'}).text.strip()
        blogs_info.append(blog_info)

    return blogs_info  