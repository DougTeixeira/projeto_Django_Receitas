from urllib import response
from .test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes import views

class RecipeDetailViewTest(RecipeTestBase):
    def test_recipe_detail_view_functions_is_correct(self):
        view = resolve(reverse('recipes:recipe', args=(1, )))
        self.assertIs(view.func, views.recipe)


    def test_recipe_detail_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:recipe', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_load_the_correct_recipe(self):
        needed_title = 'This is a detail page - It load one recipe'
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        response_recipe = response.context['recipe']
        content = response.content.decode('utf-8')

        self.assertEqual(response_recipe.title, needed_title)
        self.assertIn(needed_title, content)

    def test_recipe_detail_templates_dont_load_recipe_not_published(self):
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:recipe', 
        kwargs={'id': recipe.id}))
        
        self.assertEqual(response.status_code, 404)