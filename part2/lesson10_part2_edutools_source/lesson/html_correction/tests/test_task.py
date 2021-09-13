from lesson.utils import SkyproTestCase

from bs4 import BeautifulSoup


class TestCase(SkyproTestCase):

    def get_key(self):
        return "155598"


    def test_form(self):
        with open('form.html', 'r') as fh:
            soup = BeautifulSoup(fh.read(), "html.parser")

            all_body = soup.find_all('body')

            self.assertEqual(1, len(all_body), msg='В документе должен быть тег body')

            body = all_body[0]
            all_form = body.find_all('form')

            self.assertEqual(1, len(all_form), msg='Внутри тега body должна быть форма (тег form)')

            form = all_form[0]
            all_p = form.find_all('p')
            msg = 'Внутри тега form должен быть 1 тег p с текстом Пример формы'

            self.assertEqual(1, len(all_p), msg)
            self.assertEqual('Пример формы', all_p[0].text, msg)

            all_label = form.find_all('label')
            msg = 'Внутри тега form должен быть 1 тег label с текстом Ваше имя:'

            self.assertEqual(1, len(all_label), msg)
            self.assertEqual('Ваше имя:', all_label[0].text, msg)

            self.assertEqual(None, all_label[0].get('value'), msg='Тег label не имеет атрибута value')
            self.assertEqual('br', all_label[0].find_next().name, msg='После тега label должен быть тег <br>')

            all_input = form.find_all('input')
            msg = 'Внутри тега form должен быть 1 тег input с атрибутом type=text и value=Мое имя'

            self.assertEqual(1, len(all_input), msg)
            self.assertEqual('', all_input[0].text, msg)
            self.assertEqual('text', all_input[0].get('type'), msg)
            self.assertEqual('Мое имя', all_input[0].get('value'), msg)

            self.assertEqual('br', all_input[0].next_sibling.name,
                             msg='После тега input должно быть текста Мое имя, а должен идти тег <br>')

            all_button = form.find_all('button')
            msg = 'Внутри тега form должен быть 1 тег button с атрибутом type=submit и содержимым Отправить'

            self.assertEqual(1, len(all_button), msg)
            self.assertEqual('Отправить', all_button[0].text, msg)
            self.assertEqual('submit', all_button[0].get('type'), msg)
            self.assertEqual('', all_button[0].get('value', ''),
                             msg='У тега button атрибут value не должен быть равен Отправить')

