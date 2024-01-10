import configuration  # Импорт информации из файла configuration
import requests
import data  # Импорт информации из файла data


# Функция на создание заказа
def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         # подставляем полный url
                         json=body)  # тело


# Сохранение результата вызова функции на создание заказа
new_orders_response = post_new_orders(data.orders_body)

track_orders = new_orders_response.json()  # Сохраняем в переменную ответ на запрос создания заказа

track_number = track_orders["track"]  # Сохраняем номер трека заказа


# Функция на получения заказа по треку заказа
def get_orders_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.ORDERS_TRACK_PATH + str(track))