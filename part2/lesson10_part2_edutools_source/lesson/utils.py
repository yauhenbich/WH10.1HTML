import unittest

class StatMixin:
    def send_stat(self, result):
        if result.wasSuccessful():
            print("Задание выполнено! Ваш код:",  self.get_key())

class SkyproTestCase(StatMixin, unittest.TestCase):
    def run(self, *args, **kwargs):
        result = super().run(*args, **kwargs)
        self.send_stat(result)
        return result
