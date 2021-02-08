import requests
from pprint import pprint
import os 

token = input('Введите токен: ')

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version, id):
        self.token = token
        self.version = version 
        self.params = {
            'access_token' : self.token,
            'v': self.version
        } 
        self.id = id
        
    def __and__(self, other):
        first_id = self.id
        second_id = self.id
        self.params_for_mutual_friends = {'access_token': token, 
        'v':'5.126', 
        'source_uid': first_id, 
        'target_uid': second_id}
        self.mutual_friends = requests.get(self.url+'friends.getMutual', self.params_for_mutual_friends).json()['response']
        print(self.mutual_friends)
         
    def __str__(self):
        url = 'https://api.vk.com/method/'
        params = {
            'access_token' : token,
            'v': '5.126',
            'fields': 'domain',
            'id': self.id
        } 
        screen_name = requests.get(url+'users.get', params).json()['response'][0]['domain']

        url_two = str('https://vk.com/' + str(screen_name))
        return url_two

       
first = int(input('Введите id пользователя: '))  
second = int(input('Введите id пользователя: '))  

vk_client = VkUser(token, '5.126', first)
vk_client_two = VkUser(token, '5.126', second)

vk_client&vk_client_two
print(vk_client)





# id1= 33468893
# id2= 552934290
# вывод ссылки на сайт 

# self.id = requests.get(self.url+'users.get', self.params).json()['response'][0]['id']
