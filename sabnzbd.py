import requests
import os
import shutil
import time
from urllib.parse import quote

path = 'input'
nzbfiles = []
for root, dirs, files in os.walk(path):
    for file in files:
        nzbfiles.append(os.path.join(root, file))


for nzbfile in nzbfiles:
    params = {
        'mode': 'addlocalfile',
        'apikey': '062280e120e44541b6e7979347e333f7', #nzb add key
        'name': os.getcwd() + '\\' + nzbfile,
    }
    response = requests.get('http://127.0.0.1:8080/sabnzbd/api', params=params)
    print(response.text)


time.sleep(60)
while True:
    params = {
        'mode': 'queue',
        'apikey': '47d022277d614d64a8450432a997b9a0' #api key
    }

    response = requests.get('http://127.0.0.1:8080/sabnzbd/api', params=params).json()
    if response['queue']['status'] == "Idle":
            for dir in nzbfiles:
                dir = str(dir).replace(path,"Downloads").replace('.nzb', '')
                file = dir.split('\\')[-1]
                dir = dir.replace(file,'')
                if not os.path.exists(dir):
                    os.makedirs(dir)
                shutil.move("Downloads/"+file, dir)
            exit(0)
    print("the server is not idle")
    time.sleep(60)