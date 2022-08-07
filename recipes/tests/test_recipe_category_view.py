from urllib import response
from .test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes import views

class RecipeCategoryViewTest(RecipeTestBase):
    def test_recipe_category_view_functions_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)


    def test_recipe_category_view_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_templates_loads_recipes(self):
        needed_title = 'This is a category test'
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1, )))
        response_recipe = response.context['recipes']
        content = response.content.decode('utf-8')

        self.assertEqual(response_recipe[0].title, needed_title)
        self.assertIn(needed_title, content)

    def test_recipe_category_templates_dont_load_recipes_not_published(self):
        category = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:category', 
        kwargs={'category_id': category.id}))
        
        self.assertEqual(response.status_code, 404)


