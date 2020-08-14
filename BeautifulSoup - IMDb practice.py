#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install -U BeautifulSoup4
import requests
from bs4 import BeautifulSoup 


# In[20]:


def find_endgame_genre(request_url):
    """
    >>> find_endgame_genre("https://www.imdb.com/title/tt4154796")
    ['Action', 'Adventure', 'Drama']
    """
    response = requests.get(request_url)
    response_text = response.text   # response_text is a long str.
    
    soup = BeautifulSoup(response_text)   # Change the str into readable word.
    soup.select(".subtext a")
#     print(soup.select(".subtext a"))
#     print(soup.select(".subtext a")[0].text)
#     print("-----------")
    movie = list()   # Or movie = []
    for m in soup.select(".subtext a"):
        movie.append(m.text)
    movie.pop()   # Delete the last element in the list.
    print(movie)


# In[21]:


find_endgame_genre("https://www.imdb.com/title/tt4154796")


# In[ ]:





# In[32]:


def find_endgame_cast(request_url):
    """
    >>> find_endgame_cast("https://www.imdb.com/title/tt4154796")
    ['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth', 'Scarlett Johansson', 'Jeremy Renner', 'Don Cheadle', 'Paul Rudd', 'Benedict Cumberbatch', 'Chadwick Boseman', 'Brie Larson', 'Tom Holland', 'Karen Gillan', 'Zoe Saldana', 'Evangeline Lilly']
    """
    response = requests.get(request_url)
    response_text = response.text
    soup = BeautifulSoup(response_text)
    soup.select(".primary_photo+ td a")
#     print(soup.select(".primary_photo+ td a"))
#     print(soup.select(".body .selectorgadget_selected")[0].text)
#     print("-----------")
    cast = []
    for m in soup.select(".primary_photo+ td a"):   # cast = [e.text.strip() for e in elems]
        cast.append(m.text.strip())
    print(cast)
    
    
    


# In[33]:


find_endgame_cast("https://www.imdb.com/title/tt4154796")


# In[ ]:





# In[81]:


def get_movie_data_from_url(request_url):
    """
    >>> movie_data = get_movie_data_from_url("https://www.imdb.com/title/tt4154796")
    >>> movie_data["moviePoster"]
    'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'
    >>> movie_data["movieGenre"]
    ['Action', 'Adventure', 'Drama']
    >>> movie_data["movieCast"]
    ['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth', 'Scarlett Johansson', 'Jeremy Renner', 'Don Cheadle', 'Paul Rudd', 'Benedict Cumberbatch', 'Chadwick Boseman', 'Brie Larson', 'Tom Holland', 'Karen Gillan', 'Zoe Saldana', 'Evangeline Lilly']
    """
    response = requests.get(request_url)
    response_text = response.text   # response_text is a long str.
    soup = BeautifulSoup(response_text)   # Change the str into readable word.
    
    # Genre
    movie = list()   # Or movie = []
    for m in soup.select(".subtext a"):
        movie.append(m.text)
    movie.pop()   # Delete the last element in the list.
    # print(movie)
    
    # Cast
    cast = []
    for m in soup.select(".primary_photo+ td a"):   # cast = [e.text.strip() for e in elems]
        cast.append(m.text.strip())
    # print(cast)
    
    # Poster
    poster = soup.select("#title-overview-widget img")[0].get('src')   # poster = soup.select(".poster img").get('src') 
    # print(poster)
    
    # print("-----------------")
    
    # Create a dictionary.
    dic = {
        "moviePoster": poster,
        "movieGenre": movie,
        "movieCast": cast,
    }
    #print(dic)
    return dic   # Cannot run without return. 
    


# In[84]:


get_movie_data_from_url("https://www.imdb.com/title/tt4154796")


# In[85]:


movie_data = get_movie_data_from_url("https://www.imdb.com/title/tt4154796")


# In[90]:


movie_data['moviePoster']


# In[87]:


movie_data["movieGenre"]


# In[89]:


movie_data["movieCast"]


# In[ ]:





# In[47]:


# Build a class to combine everything, and we don't hvae to repeat the same element again and again.
class FindEndgameData:
    def __init__(self, request_url):
        self._request_url = request_url
    def build_soup(self):
        response = requests.get(self._request_url)   # "self."_request_url
        soup = BeautifulSoup(response.text)
        self._soup = soup   # Equal to return soup   # State self._soup = soup
        # return soup
    def find_genre(self):
        genre = [e.text for e in self._soup.select('.subtext a')]
        genre.pop()
        return genre
    def find_cast(self):
        cast = [e.text.strip() for e in self._soup.select('.primary_photo+ td a')]
        return cast


# In[48]:


fed = FindEndgameData("https://www.imdb.com/title/tt4154796")
fed.build_soup()
print(fed.find_genre())
print(fed.find_cast())


# In[ ]:





# In[ ]:





# In[ ]:




