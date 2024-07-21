import requests
import json
import time
import csv
import random
 




headers = {
  'accept': 'application/json',
  'accept-language': 'en-GB,en-US,en',
  'app-session-id': '1dc16123-4c42-4be8-96c6-86865f676bfb',
  'app-session-time-elapsed': '-1921786',
  'app-version': '1052300',
  'content-type': 'application/json',
  'origin': 'https://tinder.com',
  'persistent-device-id': 'ece77f34-6fb4-45f6-86e1-b230bb246fcd',
  'platform': 'web',
  'priority': 'u=1, i',
  'referer': 'https://tinder.com/',
  'sec-ch-ua': '"Chromium";v="124", "Opera";v="110", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'tinder-version': '5.23.0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0',
  'user-session-id': '5d3c74cc-b7a4-4d06-8e97-bfbae33568d2',
  'user-session-time-elapsed': '1723023',
  'x-auth-token': '677c0e87-6a92-4fa5-83da-883e531098e8',
  'x-supported-image-formats': 'webp,jpeg'
}
 
headers = {
          'accept': 'application/json',
            'accept-language': 'en-GB,en-US,en',
              'app-session-id': '4d3a42d7-1821-465b-949b-9c281cdafb7a',
                'app-session-time-elapsed': '583860',
                  'app-version': '1052300',
                    'content-type': 'application/json',
                      'origin': 'https://tinder.com',
                        'persistent-device-id': 'ece77f34-6fb4-45f6-86e1-b230bb246fcd',
                          'platform': 'web',
                            'priority': 'u=1, i',
                              'referer': 'https://tinder.com/',
                                'sec-ch-ua': '"Chromium";v="124", "Opera";v="110", "Not-A.Brand";v="99"',
                                  'sec-ch-ua-mobile': '?0',
                                    'sec-ch-ua-platform': '"macOS"',
                                      'sec-fetch-dest': 'empty',
                                        'sec-fetch-mode': 'cors',
                                          'sec-fetch-site': 'cross-site',
                                            'tinder-version': '5.23.0',
                                              'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0',
                                                'user-session-id': '57a53ddc-0273-46c8-b1d4-ba038dfac167',
                                                  'user-session-time-elapsed': '583860',
                                                    'x-auth-token': 'd40c5bba-cbae-4cd6-8023-5fa97161d98b',
                                                      'x-supported-image-formats': 'webp,jpeg'
                                                      }




def get_content():
    url = "https://api.gotinder.com/v2/recs/core?locale=en-GB"
    payload = {}
    return requests.request("GET", url, headers=headers, data=payload)

def update_location(lat,lon):   


    url = "https://api.gotinder.com/passport/user/travel?locale=en-GB"

    payload = json.dumps({
    "lat": lat,
    "lon": lon
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)

    return response



def send(id, s_number, liked_content_id ):
    url = f"https://api.gotinder.com/like/{id}?locale=en-GB"
    payload = json.dumps({
    "s_number": s_number,
    "user_traveling": 1,
    "liked_content_id": liked_content_id,
    "liked_content_type": "photo"
    })
    return requests.request("POST", url, headers=headers, data=payload)

locations = []
with open('citiesee.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
        locations.append(line)

for location in locations[30:]:
    for i in range(5):
        
        lat = float(location[2])
        lng = float(location[3])
        lat = lat + round(random.random()*random.random()*0.01,4)
        lng = lng + round(random.random()*random.random()*0.01,4)
        try:
            update_location(lat, lng)
            time.sleep(6)
            response = get_content()
            time.sleep(1)
            data = json.loads(response.text)['data']
            if not data:
                continue
            rows = data['results']
            if not rows:
                    continue
        except:
            continue

        for row in rows:
                time.sleep(0.4)
                user = row['user']
                id = row['user']['_id']
                s_number = row['s_number']
                pic_id = row['user']['photos'][0]['id']
                send(id, s_number, pic_id)
                print({ "name": user['name'], "real_loc": location[0], "dist": row['distance_mi']})
