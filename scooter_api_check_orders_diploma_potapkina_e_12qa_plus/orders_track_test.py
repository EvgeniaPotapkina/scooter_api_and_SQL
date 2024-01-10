# Потапкина Евгения, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


# Тест, что код ответа равен 200
def test_orders_track():
    track_number = sender_stand_request.track_number
    orders_track_response = sender_stand_request.get_orders_track(track_number)
    assert orders_track_response.status_code == 200
