from task import app, load_users
from lesson.utils import SkyproTestCase

users = load_users()

class TestCase(SkyproTestCase):

    def get_key(self):
        return "173645"

    def test_users(self):
        with app.test_client() as client:
            resp = client.get('/users/1/')
            self.assertNotEqual(404, resp.status_code, msg='Представление должно работать по урлу /users/1/')

            resp = client.get('/users/fsdfsd/')
            self.assertEqual(404, resp.status_code,
                             msg='Представление должно обрабатывать сегмент урла как целое число')

            not_found_str = 'Не найдено'

            for i in (0, 11, 20, 100, 1000):
                resp = client.get(f'/users/{i}/')

                self.assertEqual(404, resp.status_code,
                                 msg=f'Если по индексу не найден пользователь, то код ответ должен быть 404')
                self.assertEqual(not_found_str, resp.get_data(True),
                                 msg=f'Если по индексу не найден пользователь, то ответ должен быть {not_found_str}')

            for i, user in enumerate(users, start=1):
                resp = client.get(f'/users/{i}/')
                expected = f'{user["last_name"]} {user["first_name"]}'

                self.assertEqual(200, resp.status_code,
                                 msg=f'По индексу {i} должен возвращаться код ответа 200')
                self.assertEqual(expected, resp.get_data(True),
                                 msg=f'По индексу {i} должен возвращаться ответ {expected}')
