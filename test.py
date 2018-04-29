#!/usr/bin/env python

"""Tests for the Flask Heroku template."""

import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_page_works(self):
        rv = self.app.get('/')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)

    def test_results_api_works(self):
        rv = self.app.get('/api/results')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)

    def test_404_page(self):
        rv = self.app.get('/i-am-not-found/')
        self.assertEqual(rv.status_code, 404)


if __name__ == '__main__':
    unittest.main()
