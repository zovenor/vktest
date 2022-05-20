import requests
import datetime
import pickle
from configs import *


def get_status(current_status, id, link_id):
    # profiles = vk_api.users.get(user_id=id, fields='online, last_seen', v=5.131, access_token=token)
    profiles = requests.get(
        f'https://api.vk.com/method/users.get?user_id={id}&access_token={token}&v=5.131&fields=online, last_seen').json()[
        'response']
    data = None
    try:
        data = pickle.load(open(file_url, 'rb'))
    except:
        pass
    if (not current_status) and (profiles[0]['online']):  # если появился в сети, то выводим время
        now = datetime.datetime.now()
        print('Появился в сети в: ', now.strftime("%d-%m-%Y %H:%M"))
        if data is None:
            data = {str(link_id): [f'Появился в сети в: {now.strftime("%d-%m-%Y %H:%M")}', ]}
            pickle.dump(data, open(file_url, 'wb'))
        else:
            if str(link_id) in data:
                data[str(link_id)].append(f'Появился в сети в: {now.strftime("%d-%m-%Y %H:%M")}')
                pickle.dump(data, open(file_url, 'wb'))
            else:
                data[str(link_id)] = [f'Появился в сети в: {now.strftime("%d-%m-%Y %H:%M")}', ]
                pickle.dump(data, open(file_url, 'wb'))
        return True
    if (current_status) and (not profiles[0]['online']):  # если был онлайн, но уже вышел, то выводим время выхода

        if data is None:
            data = {str(link_id): [
                f'Вышел из сети: {datetime.datetime.fromtimestamp(profiles[0]["last_seen"]["time"]).strftime("%d-%m-%Y %H:%M")}', ]}
            pickle.dump(data, open(file_url, 'wb'))
        else:
            if data[str(link_id)]:
                data[str(link_id)].append(
                    f'Вышел из сети: {datetime.datetime.fromtimestamp(profiles[0]["last_seen"]["time"]).strftime("%d-%m-%Y %H:%M")}')
                pickle.dump(data, open(file_url, 'wb'))
            else:
                data[str(link_id)] = [
                    f'Вышел из сети: {datetime.datetime.fromtimestamp(profiles[0]["last_seen"]["time"]).strftime("%d-%m-%Y %H:%M")}', ]
                pickle.dump(data, open(file_url, 'wb'))

        return False
    return current_status
