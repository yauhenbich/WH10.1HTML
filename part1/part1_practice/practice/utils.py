import unittest


class StatMixin:
    def send_stat(self, result):
        ok = result.wasSuccessful()
        errors = result.errors
        failures = result.failures

        print('ok' if ok else 'not ok')
        print('errors', errors)
        print('failures', failures)


class SkyproTestCase(StatMixin, unittest.TestCase):
    def run(self, *args, **kwargs):
        result = super().run(*args, **kwargs)

        self.send_stat(result)

        return result
