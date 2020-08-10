#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


import time

def get_to_movie_page(movie_title):
    executable_path = "C:/Users/Paul/Desktop/chromedriver.exe"
    driver = webdriver.Chrome(executable_path)   # Duplicate a chromedriver to the file (C:\Users\Paul\anaconda3\envs\selenium)
    
    # Get to imdb.com index page.
    driver.get("https://www.imdb.com/")
    
    # Search movie
    element = driver.find_element_by_css_selector("#suggestion-search")
    element.send_keys(movie_title)
    
    # Click search button.
    element = driver.find_element_by_css_selector("#suggestion-search-button")
    element.click()
    
    # Click movie category button.
    elements = driver.find_elements_by_css_selector('.findTitleSubfilterList a')
    elements[0].click()
    
    # Sleep for 2 seconds.
    time.sleep(2)
    
    # Click the most similar search result.
    elements = driver.find_elements_by_css_selector(".result_text a")
    elements[0].click()
    
    movie_url = driver.current_url
    driver.close()
    return movie_url


# In[3]:


get_to_movie_page('Inception')


# In[ ]:




