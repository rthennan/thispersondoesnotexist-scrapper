# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:12:05 2021

@author: Thennan
this-person-does-not-exist.com scraper
"""
from os import path,listdir,makedirs
import requests
from datetime import datetime as dt
from time import sleep
import random

personURL='https://thispersondoesnotexist.com/image'
artURL='https://thisartworkdoesnotexist.com/'
catURL = 'https://thiscatdoesnotexist.com/'
#creating lookup dictionaries for the URL request and folder location
folders = {1:'person',2:'art',3:'cat'}
urls = {1:personURL,2:artURL,3:catURL}
#create image directories if they don't exist:
for i in range(1,4):
    if not path.exists(folders[i]):
        makedirs(folders[i])
#If the pogram was interupted somehow and is restarted/resumed, this counter gives a rough idea of the number of images already stored.
counter=len(listdir('person'))
while True:
    date_time = dt.now().strftime("%Y_%m_%d_%H_%M_%S")+'.jpeg'
    for i in range(1,4):
            req= requests.get(urls[i])
            reqFile = path.join(folders[i],date_time)
            with open(reqFile, 'wb') as f:
                f.write(req.content)
    #Sleeping for 1-3 seconds before the next request. Randomizing the sleeptime to avoid looking like a bot. Mind Blastingly Smart  
    sleeptime = random.randint(1,3)    
    counter = counter+1
    print(f"{dt.now()} Epoch Number => {str(counter)}. Sleeping For {sleeptime} seconds")
    sleep(sleeptime)