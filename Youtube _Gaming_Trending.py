
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

web = webdriver.Chrome()
web.get("https://www.youtube.com/feed/trending?bp=4gIcGhpnYW1pbmdfY29ycHVzX21vc3RfcG9wdWxhcg%3D%3D")

time.sleep(1)

find_href = web.find_elements_by_id('video-title')
for my_href in find_href:
    TopTrend = print(my_href.get_attribute("aria-label"))
    print("\n")
    if TopTrend != None:    
        print(TopTrend)
    
    
