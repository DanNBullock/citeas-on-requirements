# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:50:39 2022

@author: dbullock
"""

#open requirements.txt file
with open('requirements.txt') as f:
    lines = f.readlines()

#emailAdress='githubActionTest@DanNBullock.com'
emailAdress=''
apiStem='https://api.citeas.org/product/'


import requests
#make a url request
testURL=''.join([apiStem,lines[0].replace('\n',''),'?',emailAdress])

outAPIresponse=requests.get(testURL)

import json
outResponseJson=json.loads(outAPIresponse.text)

#optionsKey=['APS','Harvard','Nature','MLA','Chicago','Vancouver']
#set default choice to Nature
defaultCiteFormat=2

#loop and ship

outCitation=outResponseJson['citations'][defaultCiteFormat]['citation']