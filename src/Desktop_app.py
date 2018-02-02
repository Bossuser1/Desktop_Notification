# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:08:30 2018

@author: traoreb
"""

import time
import notify2
from topnews import topStories
 
# path to notification window icon
#ICON_PATH = "put full path to icon image here"
ICON_PATH = "/home/traoreb/Bureau/Python/Desktop_Notification/src/news_icon.png" 
# fetch news items
newsitems = topStories()
 
# initialise the d-bus connection
notify2.init("News Notifier")
 
# create Notification object
n = notify2.Notification(None, icon = ICON_PATH)
 
# set urgency level
n.set_urgency(notify2.URGENCY_NORMAL)
 
# set timeout for a notification
n.set_timeout(10000)
 
for newsitem in newsitems:
    try: 
        # update notification data for Notification object
    	n.update(newsitem['title'], newsitem['description']) 
    	# show notification on screen
    	n.show()
    	# short delay between notifications
    except:
	pass
    time.sleep(15)
