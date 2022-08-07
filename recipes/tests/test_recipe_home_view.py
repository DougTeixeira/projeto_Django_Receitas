from urllib import response
from .test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes import views



class RecipeHomeViewTest(RecipeTestBase):
    def test_recipe_home_view_functions_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)


    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)


    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')


    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here. 😥</h1>', 
            response.content.decode('utf-8')
            )


    def test_recipe_home_templates_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_recipe = response.context['recipes']
        content = response.content.decode('utf-8')

        self.assertEqual(response_recipe.first().title, 'Recipe Title')
        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 porções', content)
        self.assertEqual(len(response_recipe), 1)

    def test_recipe_home_templates_dont_load_recipes_not_published(self):
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here. 😥</h1>', 
            response.content.decode('utf-8')
            )
