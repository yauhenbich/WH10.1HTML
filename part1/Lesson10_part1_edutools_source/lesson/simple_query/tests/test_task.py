from task import app
from lesson.utils import SkyproTestCase

class TestCase(SkyproTestCase):

    def get_key(self):
        return "375645"


    def test_sort(self):
        with app.test_client() as client:

            #  проверка статуса

            path = '/search/?s=а'
            expected = '...'
            resp = client.get(path)
            self.assertEqual(200, resp.status_code, msg=f'Приложение не обрабатывает запрос к {path}')


            # ожидание и реальность

            path = '/search/?s=мос'
            expected = 'Москва'
            resp = client.get(path)
            self.assertEqual(expected, resp.get_data(True),
                             msg=f'Неверный ответ при запросе к {path} должно быть {expected}')


            # ожидание и реальность

            path = '/search/?s=кра'
            expected = 'Красноярск, Краснодар'
            resp = client.get(path)
            self.assertEqual(expected, resp.get_data(True),
                             msg=f'Неверный ответ при запросе к {path} должно быть {expected}')



            # ожидание и реальность

            path = '/search/?s=санкт'
            expected = 'Санкт-Петербург'
            resp = client.get(path)
            self.assertEqual(expected, resp.get_data(True),
                             msg=f'Неверный ответ при запросе к {path} должно быть {expected}')

