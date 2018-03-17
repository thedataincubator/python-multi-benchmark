import time
import json
import requests
from functools import wraps
from selenium import webdriver

URL = "https://en.wikipedia.org/wiki/Special:Random"

def timed(func):
  @wraps(func)
  def wrapper(i):
    start = time.time()
    length = len(func(i))
    end = time.time()
    return {
      "start": start,
      "length": length,
      "func": func.__name__,
      "end": end,
      "i": i,
    }
  return wrapper

@timed
def request_func(i):
  return requests.get(URL).text

@timed
def selenium_func(i):
  driver = webdriver.PhantomJS()
  driver.get(URL)
  page_source = driver.page_source
  driver.close()
  return page_source
