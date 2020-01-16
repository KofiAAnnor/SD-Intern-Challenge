from run import app, Intern
import unittest
from flask import json


class Tests(unittest.TestCase):

    def test_valid_get_request(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Intern.query.all(), [])
        Intern.query.delete()

    def test_valid_post_request(self):
        tester = app.test_client(self)
        js = [{"first_name": "test1", "last_name": "Voss", "position":"Software Development Intern", "school": "UMCP",
               "degree_program": "Computer Science"}]
        response = tester.post('/', data=json.dumps(js), content_type='application/json')
        self.assertFalse(Intern.query.filter_by(first_name='test1').first() is None)
        self.assertEqual(response.status_code, 200)
        Intern.query.delete()

    def test_invalid_post_request(self):
        tester = app.test_client(self)
        js = [{"first_name": "test2", "last_name": "Voss", "position":"Software Intern", "school": "UMCP",
               "degree_program": "Computer Science"}]
        response = tester.post('/', data=json.dumps(js), content_type='application/json')
        self.assertEqual(Intern.query.filter_by(first_name='test2').first(), None)
        self.assertEqual(response.status_code, 400)
        Intern.query.delete()

    def test_valid_post_request_multiple(self):
        tester = app.test_client(self)
        js = [{"first_name": "test3", "last_name": "Voss", "position":"Software Development Intern", "school": "UMCP",
               "degree_program": "Computer Science"},
              {"first_name": "test4", "last_name": "Voss", "position":"Software Development Intern", "school": "UMBC",
               "degree_program": "Computer Science"}]
        response = tester.post('/', data=json.dumps(js), content_type='application/json')
        self.assertFalse(Intern.query.filter_by(first_name='test3').first() is None)
        self.assertFalse(Intern.query.filter_by(first_name='test4').first() is None)
        self.assertEqual(response.status_code, 200)
        Intern.query.delete()

    def test_invalid_post_request_multiple(self):
        tester = app.test_client(self)
        js = [{"first_name": "test5", "last_name": "Voss", "position":"Software Development Intern", "school": "UMCP",
               "degree_program": "Computer Science"},
              {"first_name": "test6", "last_name": "Voss", "position":"Research Intern", "school": "UMBC",
               "degree_program": "Linguistics"},
              {"first_name": "test7", "last_name": "Voss", "position": "Bio-Informatics Intern", "school": "UMBC",
               "degree_program": "Biology"}
              ]
        response = tester.post('/', data=json.dumps(js), content_type='application/json')
        self.assertEqual(Intern.query.filter_by(first_name='test5').first(),  None)
        self.assertEqual(Intern.query.filter_by(first_name='test6').first(),  None)
        self.assertEqual(Intern.query.filter_by(first_name='test7').first(),  None)
        self.assertEqual(response.status_code, 400)
        Intern.query.delete()


if __name__ == "__main__":
    unittest.main()
