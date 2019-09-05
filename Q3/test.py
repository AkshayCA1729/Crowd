from urllib.request import urlretrieve
from PIL import Image
import os
import base64
import json


def url_info(url):                                      #function for url_info
    img_name = url.split('/')[-1]                       #retrieving image name
    try:
        img = urlretrieve(url, filename=img_name)
        imgg = Image.open(img_name)        #Copy a network object denoted by a URL to a local file
        img = Image.open(img_name)
        img = img.resize((320, 568))

        with open(img_name, 'rb') as i:
            encoded = base64.b64encode(i.read())         
            decoded = encoded.decode('UTF-8')

        json_path = img_name.split('.')[0] + '.json'       #creating json file

        info = {'image_url': url,
                'image_size': os.path.getsize(img_name),
                'image_resolution': imgg.size,
                'image_file': img_name,
                'json_file': json_path,
                'image64': decoded
                }

        with open(json_path, 'w') as j:
            json.dump(info, j)                            #adding info to json file

        print(info)

    except Exception as e:
        print(e)


url_info('https://www.python.org/static/opengraph-icon-200x200.png')   #function call for url_info
