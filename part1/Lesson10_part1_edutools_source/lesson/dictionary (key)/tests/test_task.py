from task import app, vocab
from lesson.utils import SkyproTestCase

class TestCase(SkyproTestCase):

    def get_key(self):
        return "423304"

    def test_index(self):
        with app.test_client() as client:
            for key, value in vocab.items():
                resp = client.get(f'/{key}/')
                expected = f'Значение для ключа {key} - {value}'

                self.assertEqual(200, resp.status_code,
                                 msg=f'Урл /{key}/ должен возвращать код ответа 200')
                self.assertEqual(expected, resp.get_data(True),
                                 msg=f'Урл /{key}/ должен возвращать "{expected}"')

            resp = client.get(f'/not_vacab_value/')
            expected = 'Ключ не найден'

            self.assertEqual(404, resp.status_code,
                             msg=f'Для значений не из словаря представление должно возвращать код ответа 404')
            self.assertEqual(expected, resp.get_data(True),
                             msg=f'Для значений не из словаря представление должно возвращать "{expected}"')
