from lesson.utils import SkyproTestCase
from lesson.search_form.task import app
from bs4 import BeautifulSoup


class TestCase(SkyproTestCase):

    def get_key(self):
        return "008200"

    def test_form(self):
        with app.test_client() as client:
            get_resp = client.get('/search/')
            self.assertEqual(200, get_resp.status_code,
                             msg='Представление должно обрабатывать GET-запросы по урлу /search/')
            #
            # post_resp = client.post('/search/')
            # self.assertEqual(200, post_resp.status_code,
            #                  msg='Представление должно обрабатывать POST-запросы по урлу /search/')

            self._test_get(client)
            self._test_post(client)

    def _test_get(self, client):
        resp = client.get('/search/')

        soup = BeautifulSoup(resp.get_data(True), 'html5lib')

        forms = soup.find_all('form')

        self.assertEqual(1, len(forms), msg='Представление по GET-запросу должно возвращать страницу с 1 формой')

        form = forms[0]

        self.assertEqual('post', form.get('method'), msg='У формы должен быть задан атрибут method')

        all_text_input = form.find_all('input', type='text')

        self.assertEqual(1, len(all_text_input), msg='В форме должно быть 1 текстовое поле (атрибут type="text")')

        self.assertEqual('search', all_text_input[0].get('name'),
                         msg='У текстового поля атрибут name должен быть равен "search"')

        input_submit = form.find_all('input', type='submit') + form.find_all('button', type='submit')

        self.assertEqual(1, len(input_submit), msg='В форме должна быть 1 кнопка с типом submit (input или button)')

    def _test_post(self, client):
        search = 'python'
        resp = client.post('/search/', data={'search': search})

        soup = BeautifulSoup(resp.get_data(True), 'html5lib')

        all_h1 = soup.find_all('h1')

        msg = f'В ответ на POST-запрос приложение должно возвращать 1 заголовок h1 с текстом ' \
              '"Результаты по запросу {search}"'

        self.assertEqual(1, len(all_h1), msg)

        h1 = all_h1[0]

        self.assertEqual(f'Результаты по запросу {search}', h1.text, msg)

        all_i = h1.find_all('i') + h1.find_all('em')

        msg = 'В заголовке h1 значение, указанное в текстовом поле, должно отображаться курсивом'

        self.assertEqual(1, len(all_i), msg)
        self.assertEqual(search, all_i[0].text, msg)
