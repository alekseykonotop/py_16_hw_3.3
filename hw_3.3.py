import requests
from urllib.parse import urlencode





# Написать функцию поиска общих друзей:
# Функция должна принимать идентификаторы пользователей;
# Результат работы: список идентификаторов общих друзей со ссылками на страницы.
# Подсказка: обратите внимание на документацию методов.


# Алгоритм решения
# 1.0 Запросить идентификаторы ( возможно их будет больше 1) target_uid или target_uids
# 1.1 Получить ключ авторизации.
# 2.0 Используя метод friends.getMutual
#     ( https://vk.com/dev/friends.getMutual?params[source_uid]=3004869&params[target_uid]=3004879&params[v]=5.80 )
#     учесть кол-во остальных идентификаторов ( 1 или больше)
#     получить список идентификаторов общих друзей
# 2.1 Зная идентификаторы сформировать ссылки на профили пользователей
#     ( к строке "https://vk.com/id" добавить идентификатор)
# 3.0 Вывести результат в виде списка кортежей типа [(user_id, "https://vk.com/id00012344"), (), ()]


AUTH_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6623972 # id приложения konotop_hw_3.3

auth_params = {
    'client_id': APP_ID,
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.80'
}

# print('?'.join((AUTH_URL, urlencode(auth_params))))
# Получили ссылку: https://oauth.vk.com/authorize?client_id=6623972&scope=friends&response_type=token&v=5.80
# Взяли из ссылки token:
# access_token=70eab1891ceb9bb3224a88b56cb98e3a0768873efaec25436949c8f507adcf6cc70314784685f0f704128

TOKEN = '70eab1891ceb9bb3224a88b56cb98e3a0768873efaec25436949c8f507adcf6cc70314784685f0f704128'
VK_URL = 'https://vk.com/'


if __name__ == '__main__':
    print('********** START PROGRAMM **********')
    other_id = input('Введите через запятую идентификаторы: ').split(',')
    
    params = {
        'access_token': TOKEN,
        'source_uid': 3004879, #  id моей страницы
        'v': '5.80'
    }

    if len(other_id) > 1:
        other_id = [int(i) for i in other_id]
        params['target_uids'] = other_id
    else:
        other_id = int(other_id[0])
        params['target_uid'] = other_id

    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    common_friends_lst = response.json()["response"][0]["common_friends"]
    links_common_friends = []
    for id in common_friends_lst:
        links_common_friends.append('https://vk.com/id' + str(id))
    print('Формат вывода: \nпорядковый номер --> ("id пользователя, ссылка на профиль)."')
    res_lst = list(zip(common_friends_lst, links_common_friends))
    for n, friend in enumerate(res_lst):
        print('{0} --> {1}'.format(n, friend))
    print('Всего общих друзей: {0}.'.format(len(res_lst)))

# Идентификаторы для проверки: 13029946,3561263,546948