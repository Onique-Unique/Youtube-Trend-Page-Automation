
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


web = webdriver.Chrome()
#web.get("https://www.youtube.com/feed/trending?bp=4gIcGhpnYW1pbmdfY29ycHVzX21vc3RfcG9wdWxhcg%3D%3D")

web.get("https://www.youtube.com/gaming")

time.sleep(1)

#YT_TrendGameTop = web.find_element_by_id('video-title').get_attribute('aria-label').replace("'", "")

#print((YT_TrendGameTop)

counter = 0
find_href = web.find_elements_by_id('video-title')
for my_href in find_href:
    TopTrend = print(my_href.get_attribute("aria-label"))
    counter += 1
    if counter == 5:
        break
    print("\n")
#if TopTrend != None:    
       # print(TopTrend)
        
    
    
