"""
Recipe AI Agent - Cross-platform mobile application
Runs on iOS and Android using Kivy framework
Uses TheMealDB API for recipe recommendations
"""

import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import webbrowser

Window.clearcolor = (0.95, 0.95, 0.95, 1)


class RecipeAgent:
    """AI Agent for recipe recommendations based on user preferences"""

    def __init__(self):
        self.user_preferences = {
            'cuisine': '',
            'favorite_dishes': '',
            'flavor_profile': ''
        }
        self.api_base = "https://www.themealdb.com/api/json/v1/1"

    def set_preferences(self, cuisine, dishes, flavors):
        """Store user preferences"""
        self.user_preferences['cuisine'] = cuisine
        self.user_preferences['favorite_dishes'] = dishes
        self.user_preferences['flavor_profile'] = flavors

    def search_recipes_by_cuisine(self, cuisine):
        """Search recipes by cuisine area"""
        try:
            url = f"{self.api_base}/filter.php?a={cuisine}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('meals', [])
        except Exception as e:
            print(f"Error fetching cuisine recipes: {e}")
        return []

    def search_recipes_by_ingredient(self, ingredient):
        """Search recipes by main ingredient"""
        try:
            url = f"{self.api_base}/filter.php?i={ingredient}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('meals', [])
        except Exception as e:
            print(f"Error fetching ingredient recipes: {e}")
        return []

    def search_recipes_by_name(self, name):
        """Search recipes by dish name"""
        try:
            url = f"{self.api_base}/search.php?s={name}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('meals', [])
        except Exception as e:
            print(f"Error fetching name recipes: {e}")
        return []

    def get_meal_details(self, meal_id):
        """Get detailed recipe information"""
        try:
            url = f"{self.api_base}/lookup.php?i={meal_id}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('meals'):
                    return data['meals'][0]
        except Exception as e:
            print(f"Error fetching meal details: {e}")
        return None

    def generate_recommendations(self):
        """Generate recipe recommendations based on user preferences"""
        recommendations = []

        # Search by cuisine
        if self.user_preferences['cuisine']:
            cuisine_results = self.search_recipes_by_cuisine(
                self.user_preferences['cuisine']
            )
            recommendations.extend(cuisine_results[:5])

        # Search by favorite dishes
        if self.user_preferences['favorite_dishes']:
            dishes = self.user_preferences['favorite_dishes'].split(',')
            for dish in dishes[:2]:  # Limit to 2 dishes
                dish = dish.strip()
                dish_results = self.search_recipes_by_name(dish)
                if dish_results:
                    recommendations.extend(dish_results[:3])

        # Search by flavor keywords from flavor profile
        if self.user_preferences['flavor_profile']:
            flavors = self.user_preferences['flavor_profile'].lower()
            # Extract potential ingredients from flavor description
            flavor_keywords = ['chicken', 'beef', 'fish', 'vegetable', 
                             'pasta', 'rice', 'spicy', 'sweet']
            for keyword in flavor_keywords:
                if keyword in flavors:
                    flavor_results = self.search_recipes_by_ingredient(keyword)
                    if flavor_results:
                        recommendations.extend(flavor_results[:2])
                        break

        # Remove duplicates by meal ID
        seen = set()
        unique_recommendations = []
        for meal in recommendations:
            if meal['idMeal'] not in seen:
                seen.add(meal['idMeal'])
                unique_recommendations.append(meal)

        return unique_recommendations[:10]  # Return top 10 recommendations


class RecipeAgentApp(App):
    """Main Kivy Application for Recipe AI Agent"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.agent = RecipeAgent()
        self.current_step = 0
        self.questions = [
            "What is your favorite cuisine? (e.g., Italian, Chinese, Mexican, Indian, Japanese)",
            "What are your favorite dishes? (separate with commas)",
            "What flavors do you like the most? (e.g., spicy, sweet, savory, tangy)"
        ]
        self.answers = []

    def build(self):
        """Build the UI"""
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Title
        title = Label(
            text='Recipe AI Agent',
            size_hint_y=None,
            height=60,
            font_size='24sp',
            bold=True,
            color=(0.2, 0.4, 0.8, 1)
        )
        self.main_layout.add_widget(title)

        # Question label
        self.question_label = Label(
            text=self.questions[0],
            size_hint_y=None,
            height=100,
            font_size='16sp',
            color=(0.1, 0.1, 0.1, 1),
            text_size=(Window.width - 40, None)
        )
        self.main_layout.add_widget(self.question_label)

        # Input field
        self.input_field = TextInput(
            multiline=False,
            size_hint_y=None,
            height=50,
            font_size='16sp',
            hint_text='Type your answer here...'
        )
        self.main_layout.add_widget(self.input_field)

        # Submit button
        self.submit_btn = Button(
            text='Submit',
            size_hint_y=None,
            height=50,
            font_size='18sp',
            background_color=(0.2, 0.6, 0.9, 1),
            color=(1, 1, 1, 1)
        )
        self.submit_btn.bind(on_press=self.submit_answer)
        self.main_layout.add_widget(self.submit_btn)

        # Results scroll view (hidden initially)
        self.results_scroll = ScrollView(size_hint=(1, 1))
        self.results_layout = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None,
            padding=10
        )
        self.results_layout.bind(minimum_height=self.results_layout.setter('height'))
        self.results_scroll.add_widget(self.results_layout)

        return self.main_layout

    def submit_answer(self, instance):
        """Handle answer submission"""
        answer = self.input_field.text.strip()

        if not answer:
            self.question_label.text = "Please provide an answer!"
            return

        self.answers.append(answer)
        self.input_field.text = ''
        self.current_step += 1

        if self.current_step < len(self.questions):
            # Show next question
            self.question_label.text = self.questions[self.current_step]
        else:
            # All questions answered, generate recommendations
            self.show_loading()
            self.generate_and_display_recommendations()

    def show_loading(self):
        """Show loading message"""
        self.question_label.text = "Analyzing your preferences and finding recipes...\nThis may take a few seconds."
        self.submit_btn.disabled = True
        self.input_field.disabled = True

    def generate_and_display_recommendations(self):
        """Generate and display recipe recommendations"""
        # Set user preferences
        self.agent.set_preferences(
            cuisine=self.answers[0],
            dishes=self.answers[1],
            flavors=self.answers[2]
        )

        # Get recommendations
        recommendations = self.agent.generate_recommendations()

        # Clear existing layout
        self.main_layout.clear_widgets()

        # Add title
        title = Label(
            text='Your Personalized Recipe Recommendations',
            size_hint_y=None,
            height=70,
            font_size='20sp',
            bold=True,
            color=(0.2, 0.4, 0.8, 1)
        )
        self.main_layout.add_widget(title)

        # Add summary
        summary = Label(
            text=f"Based on your love for {self.answers[0]} cuisine\nand {self.answers[1]}",
            size_hint_y=None,
            height=60,
            font_size='14sp',
            color=(0.3, 0.3, 0.3, 1)
        )
        self.main_layout.add_widget(summary)

        # Display recommendations
        if recommendations:
            self.results_layout.clear_widgets()

            for idx, meal in enumerate(recommendations, 1):
                meal_box = BoxLayout(
                    orientation='vertical',
                    size_hint_y=None,
                    height=120,
                    padding=10
                )

                meal_name = Label(
                    text=f"{idx}. {meal['strMeal']}",
                    size_hint_y=None,
                    height=40,
                    font_size='16sp',
                    bold=True,
                    color=(0.1, 0.1, 0.1, 1),
                    halign='left',
                    valign='middle'
                )
                meal_name.bind(size=meal_name.setter('text_size'))
                meal_box.add_widget(meal_name)

                # View recipe button
                view_btn = Button(
                    text='View Full Recipe Online',
                    size_hint_y=None,
                    height=40,
                    font_size='14sp',
                    background_color=(0.3, 0.7, 0.4, 1),
                    color=(1, 1, 1, 1)
                )
                view_btn.meal_id = meal['idMeal']
                view_btn.bind(on_press=self.open_recipe_link)
                meal_box.add_widget(view_btn)

                # Separator
                separator = Label(
                    text='─' * 50,
                    size_hint_y=None,
                    height=20,
                    color=(0.7, 0.7, 0.7, 1)
                )
                meal_box.add_widget(separator)

                self.results_layout.add_widget(meal_box)

            self.main_layout.add_widget(self.results_scroll)

            # Add restart button
            restart_btn = Button(
                text='Start Over',
                size_hint_y=None,
                height=50,
                font_size='16sp',
                background_color=(0.8, 0.3, 0.3, 1),
                color=(1, 1, 1, 1)
            )
            restart_btn.bind(on_press=self.restart_app)
            self.main_layout.add_widget(restart_btn)
        else:
            error_label = Label(
                text="Sorry, couldn't find recommendations.\nPlease try again with different preferences.",
                font_size='16sp',
                color=(0.8, 0.2, 0.2, 1)
            )
            self.main_layout.add_widget(error_label)

            restart_btn = Button(
                text='Try Again',
                size_hint_y=None,
                height=50,
                font_size='16sp'
            )
            restart_btn.bind(on_press=self.restart_app)
            self.main_layout.add_widget(restart_btn)

    def open_recipe_link(self, instance):
        """Open recipe detail link in browser"""
        meal_id = instance.meal_id
        # TheMealDB website URL for the recipe
        url = f"https://www.themealdb.com/meal/{meal_id}"
        webbrowser.open(url)

    def restart_app(self, instance):
        """Restart the application"""
        self.current_step = 0
        self.answers = []
        self.agent = RecipeAgent()

        # Rebuild UI
        self.main_layout.clear_widgets()
        self.build()


if __name__ == '__main__':
    RecipeAgentApp().run()
