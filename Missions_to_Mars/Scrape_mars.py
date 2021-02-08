# Dependencies
import pandas as pd
import requests as req
import time
from bs4 import BeautifulSoup as bs
from splinter import Browser

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/Users/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)