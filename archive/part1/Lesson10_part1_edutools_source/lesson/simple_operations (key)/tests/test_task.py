from task import app
from lesson.utils import SkyproTestCase

class TestCase(SkyproTestCase):

    def get_key(self):
        return "865549"


    def test_sort(self):
        with app.test_client() as client:

            #  проверка статуса

            path = '/all/'
            resp = client.get(path)
            self.assertEqual(200, resp.status_code, msg=f'Приложение не обрабатывает запрос к {path}')

            path = '/min/'
            resp = client.get(path)
            self.assertEqual(200, resp.status_code, msg=f'Приложение не обрабатывает запрос к {path}')

            path = '/max/'
            resp = client.get(path)
            self.assertEqual(200, resp.status_code, msg=f'Приложение не обрабатывает запрос к {path}')

            path = '/avg/'
            resp = client.get(path)
            self.assertEqual(200, resp.status_code, msg=f'Приложение не обрабатывает запрос к {path}')


            # ожидание и реальность

            path = '/all/'
            expected = '1240 60 230 20 310'
            resp = client.get(path)
            self.assertEqual(expected, resp.get_data(True),
                             msg=f'Неверный ответ при запросе к {path} должно быть {expected}')


            # ожидание и реальность


            path = '/max/'
            expected = '1240'
            resp = client.get(path)
            self.assertEqual(expected, resp.get_data(True),
                             msg=f'Неверный ответ при запросе к {path} должно быть {expected}')

            path = '/min/'
            expected = '20'
            resp = client.get(path)
            self.assertEqual(expected, resp.get_data(True),
                             msg=f'Неверный ответ при запросе к {path} должно быть {expected}')


            path = '/avg/'
            expected = '372'
            resp = client.get(path)
            self.assertEqual(expected, resp.get_data(True),
                             msg=f'Неверный ответ при запросе к {path} должно быть {expected}')
