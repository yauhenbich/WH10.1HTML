from lesson.utils import SkyproTestCase
from lesson.candidates_search.task import app
from bs4 import BeautifulSoup


class TestCase(SkyproTestCase):
    def test_form(self):
        with app.test_client() as client:
            get_resp = client.get('/')
            self.assertEqual(200, get_resp.status_code, msg='Представление должно обрабатывать GET-запросы по урлу /')

            post_resp = client.post('/')
            self.assertEqual(200, post_resp.status_code, msg='Представление должно обрабатывать POST-запросы по урлу /')

            self._test_get(get_resp)
            self._test_post(client)

    def _test_get(self, get_resp):
        soup = BeautifulSoup(get_resp.get_data(True), 'html5lib')

        forms = soup.find_all('form')

        self.assertEqual(1, len(forms), msg='Представление по GET-запросу должно возвращать страницу с 1 формой')

        form = forms[0]

        self.assertEqual('post', form.get('method'), msg='У формы должен быть задан атрибут method')

        all_p = soup.find_all('p')

        self.assertTrue(len(all_p) > 0, msg='На странице должен присутствовать список кандидатов.'
                                            ' Проверьте, что вы не изменяли html-разметку списка кандидатов'
                                            ' исходного примера.')

    def _test_post(self, client):
        resp = client.post('/', data={'position': 'python'})

        soup = BeautifulSoup(resp.get_data(True), 'html5lib')

        all_p = soup.find_all('p')

        msg = 'По запросу python должен найтись 1 кандидат. ' \
              'Проверьте, что вы используете алгоритм поиска из примера, ' \
              'и обрабатываете параметры не из GET-запроса, а из POST-запроса'

        self.assertEqual(1, len(all_p), msg)
        self.assertIn('python', all_p[0].find('span', class_='position').text.lower(), msg)

        resp = client.post('/', data={'position': 'develop'})

        soup = BeautifulSoup(resp.get_data(True), 'html5lib')

        all_p = soup.find_all('p')

        msg = 'По запросу develop должны найтись 3 кандидата. ' \
              'Проверьте, что вы используете алгоритм поиска из примера, ' \
              'и обрабатываете параметры не из GET-запроса, а из POST-запроса'

        self.assertEqual(3, len(all_p), msg)

        for p_item in all_p:
            self.assertIn('develop', p_item.find('span', class_='position').text.lower(), msg)
