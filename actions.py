from rasa_core_sdk import Action
import requests
import json
import ast

from rasa_core_sdk.executor import CollectingDispatcher


class ActionGetNewst(Action):

    def name(self):
        return 'action_get_news'

    def run(self, dispatcher, tracker, domain):
        category = tracker.get_slot('category')
        print(',,,,', category)
        if category:
            url = 'http://localhost:5051/get_definations'
            params = {'category': category}
            response = requests.get(url, params)
            print(response)
            json_response = response.json()
            print(json_response)
            for item in json_response["msg_dict"]:
                print(item)
                for key, value in item.items():
                    print(key, value)
                    if key == "Text":
                        dispatcher.utter_message(value)
                    elif key == "Image_Url":
                        image_list = value
                        for image in image_list:
                            dispatcher.utter_template("utter_image", tracker, image = image)

            # img_url = {"image" : "https://www.filmibeat.com/wimgm/1366x70/desktop/2019/01/xrajinikanth_1547097026110.jpg.pagespeed.ic.eDCPjv2jbo.jpg"}
            # url = {"image" : "https://drive.google.com/uc?export=view&id=1dTsOA60uXFd63NEA2rKIItEJyRkizATE"}
            # db_url = {"image" : "https://dl.dropboxusercontent.com/s/a7imxoy2g0hmxmd/220px-WALL-Eposter.jpg?raw=1"}                      
            # dispatcher.utter_message(json_data)
            # dispatcher.utter_template("utter_image", tracker, image = db_url["image"])

        return[]