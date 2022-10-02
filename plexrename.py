import json
import time
import traceback
from urllib.parse import quote
import requests

###  以下参数通过打开plex资料库抓包获得，直接获取整个url替换即可

def rename():
    while 1:
        try:
            url = f'https://{plexurl}:32400/library/sections/1/all?type=1&id={id}&includeExternalMedia=1&title.value={filename}&titleSort.value={filename}&title.locked=1&titleSort.locked=1&X-Plex-Product=Plex Web&X-Plex-Version=4.87.2&X-Plex-Client-Identifier={X-Plex-Client-Identifier}&X-Plex-Platform=Chrome&X-Plex-Platform-Version=105.0&X-Plex-Features=external-media,indirect-media,hub-style-list&X-Plex-Model=bundled&X-Plex-Device=OSX&X-Plex-Device-Name=Chrome&X-Plex-Device-Screen-Resolution=1680x777,1680x1050&X-Plex-Token={X-Plex-Token}&X-Plex-Language=zh'

            payload = f'type=1&id={id}&includeExternalMedia=1&title.value={filename}&titleSort.value={filename}&title.locked=1&titleSort.locked=1&X-Plex-Product=Plex%20Web&X-Plex-Version=4.87.2&X-Plex-Client-Identifier={X-Plex-Client-Identifier}&X-Plex-Platform=Chrome&X-Plex-Platform-Version=105.0&X-Plex-Features=external-media%2Cindirect-media%2Chub-style-list&X-Plex-Model=bundled&X-Plex-Device=OSX&X-Plex-Device-Name=Chrome&X-Plex-Device-Screen-Resolution=1680x777%2C1680x1050&X-Plex-Token={X-Plex-Token}&X-Plex-Language=zh'
            r = requests.put(url ,timeout=5, data=payload)
            print(r.text)
            return
        except:
            traceback.print_exc()
            time.sleep(1)

def getlist():
    while 1:
        try:
            url = ''
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh',
                'Connection': 'keep-alive',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            }
            r = requests.get(url ,timeout=5, headers=headers)
            # print(r.text)
            j = json.loads(r.text)
            Metadata = j['MediaContainer']['Metadata']
            # print(r.text)
            return Metadata
        except:
            traceback.print_exc()
            time.sleep(1)

metadata = getlist()
for i in metadata:
    id = i['ratingKey']
    filename = i['Media'][0]['Part'][0]['file'].split('/')[-1]
    filename = quote(filename)
    rename()
