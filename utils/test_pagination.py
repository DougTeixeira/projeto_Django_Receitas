from django.urls import reverse, resolve
from unittest import TestCase
from utils.pagination import make_pagination_range
from recipes.tests.test_recipe_base import RecipeTestBase

class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range= list(range(1,21)),
            qty_pages=4,
            current_page=1
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

    def test_make_sure_middle_ranges_ate_correct(self):
        pagination = make_pagination_range(
            page_range= list(range(1,21)),
            qty_pages=4,
            current_page=10
        )['pagination']
        self.assertEqual([9,10,11,12], pagination)

        pagination = make_pagination_range(
            page_range= list(range(1,21)),
            qty_pages=4,
            current_page=12
        )['pagination']
        self.assertEqual([11,12,13,14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
            page_range= list(range(1,21)),
            qty_pages=4,
            current_page=19
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)

        pagination = make_pagination_range(
            page_range= list(range(1,21)),
            qty_pages=4,
            current_page=21
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)