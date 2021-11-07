from bs4 import BeautifulSoup

from lesson.utils import SkyproTestCase


class TestCase(SkyproTestCase):

    def get_key(self):
        return "375064"

    def test_wiki(self):
        with open('wiki.html', 'r') as fh:
            soup = BeautifulSoup(fh.read(), 'html5lib')

            all_b = soup.find_all('b')

            self.assertEqual(1, len(all_b), msg='На странице должен быть 1 тег b')
            self.assertEqual('Содержание', all_b[0].text, msg='Текст внутри тега b должен быть Содержание')

            all_ul = soup.find_all('ul')

            self.assertEqual(1, len(all_ul), msg='На странице должен быть 1 тег ul с оглавлением')

            all_li = all_ul[0].find_all('li')
            self.assertEqual(5, len(all_li), msg='В списке с оглавлением должно быть 5 элементов с тегом li')

            for li_item in all_li:
                all_a = li_item.find_all('a')
                self.assertEqual(1, len(all_a),
                                 msg='Внутри каждого элемента списка должна быть ссылка на параграф или изображение')

                self.assertNotEqual('', all_a[0].get('href'),
                                    msg='У ссылок внутри элементов списка должны быть заполнены атрибуты href')

            all_p = soup.find_all('p')

            self.assertEqual(4, len(all_p), msg='На странице должно быть 4 параграфа с текстом')

            for p_item in all_p:
                self.assertNotEqual('', p_item.get('id', ''), msg='У параграфов должен быть задан атрибут id')

            all_img = soup.find_all('img')

            self.assertEqual(1, len(all_img), msg='На странице должно должно быть 1 изображение с Гвидо')
            self.assertNotEqual('', all_img[0].get('id', ''), msg='У изображения должен быть задан атрибут id')
            self.assertNotEqual('', all_img[0].get('alt', ''), msg='У изображения должен быть задан атрибут alt')

            for li_item, p_item in zip(all_li, all_p+all_img):
                self.assertEqual(li_item.find('a')['href'], '#' + p_item['id'],
                                 msg='Атрибут href у ссылки должен быть равен # + значение атрибута id того элемента, '
                                     'на который ссылается данный элемент списка.')
