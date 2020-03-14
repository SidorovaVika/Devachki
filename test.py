import unittest
from app import create_app

class SomeFlaskTestCase(unittest.TestCase):
    def setUp(self):  # настройка теста
        self.app = create_app()
        self.client = self.app.test_client()
    def test_logout(self):
        rv = self.client.get('/logout')
        self.assertEqual(302, rv.status_code)
    def test_signup(self):
        rv = self.client.post('/signup', data={"Имя": "Главный", "Фамилия":"Самый","E-mail":"important@mail.ru", "Телефон":"+79215729636", "Отделение":"Тихвин", "Пароль":"1234" })
        self.assertEqual(200, rv.status_code)
    def test_signG(self):
        rv = self.client.get('/signup')
        self.assertEqual(200, rv.status_code)
    def test_logoutG(self):
        rv = self.client.get('/')
        self.assertEqual(200, rv.status_code)
    def test_userG(self):
        rv = self.client.get('/user/1'})
        self.assertEqual(200, rv.status_code)