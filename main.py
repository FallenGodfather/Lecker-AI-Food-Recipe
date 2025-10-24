"""
Lecker - Recipe Recommendation Agent
Author: Hassan Ali (FallenGodfather)
GitHub: https://github.com/FallenGodfather

A bilingual (English/German) mobile app that suggests recipes based on food preferences.
Built with Python and Kivy for iOS and Android.
"""

import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.graphics import Color, RoundedRectangle
import webbrowser

# Modern color scheme
Window.clearcolor = (0.97, 0.97, 0.98, 1)


class LanguageManager:
    """Handles translations between English and German"""

    def __init__(self):
        self.current_language = 'en'  # Default to English

        # All translations stored here
        self.translations = {
            'en': {
                'app_title': 'Lecker',
                'subtitle': 'Your Personal Recipe Finder',
                'question_1': "What's your favorite cuisine?",
                'question_1_hint': 'Examples: Italian, Chinese, Mexican, Indian',
                'question_2': 'What are your favorite dishes?',
                'question_2_hint': 'You can list multiple, separated by commas',
                'question_3': 'What kind of flavors do you enjoy?',
                'question_3_hint': 'Examples: spicy, sweet, savory, tangy',
                'input_placeholder': 'Type your answer here...',
                'next_button': 'Next',
                'find_recipes_button': 'Find Recipes',
                'error_empty': 'Please enter an answer!',
                'error_too_short': 'Please provide a more detailed answer!',
                'loading_text': 'Finding perfect recipes for you...',
                'loading_subtitle': 'This may take a moment',
                'results_title': 'Your Personalized Recipes',
                'results_subtitle': 'Based on your preferences',
                'view_recipe': 'View Recipe',
                'start_over': 'Start Over',
                'try_again': 'Try Again',
                'no_results': "Couldn't find matching recipes",
                'no_results_subtitle': 'Try different preferences',
                'language_switch': '🇩🇪 Deutsch',
                'recipe_count': 'recipes found'
            },
            'de': {
                'app_title': 'Lecker',
                'subtitle': 'Dein persönlicher Rezeptfinder',
                'question_1': 'Was ist deine Lieblingsküche?',
                'question_1_hint': 'Beispiele: Italienisch, Chinesisch, Mexikanisch',
                'question_2': 'Was sind deine Lieblingsgerichte?',
                'question_2_hint': 'Du kannst mehrere auflisten, durch Kommas getrennt',
                'question_3': 'Welche Geschmacksrichtungen magst du?',
                'question_3_hint': 'Beispiele: scharf, süß, herzhaft, würzig',
                'input_placeholder': 'Gib deine Antwort hier ein...',
                'next_button': 'Weiter',
                'find_recipes_button': 'Rezepte finden',
                'error_empty': 'Bitte gib eine Antwort ein!',
                'error_too_short': 'Bitte gib eine ausführlichere Antwort!',
                'loading_text': 'Finde perfekte Rezepte für dich...',
                'loading_subtitle': 'Das kann einen Moment dauern',
                'results_title': 'Deine personalisierten Rezepte',
                'results_subtitle': 'Basierend auf deinen Vorlieben',
                'view_recipe': 'Rezept ansehen',
                'start_over': 'Neu starten',
                'try_again': 'Nochmal versuchen',
                'no_results': 'Keine passenden Rezepte gefunden',
                'no_results_subtitle': 'Versuche andere Vorlieben',
                'language_switch': '🇬🇧 English',
                'recipe_count': 'Rezepte gefunden'
            }
        }

    def get(self, key):
        """Get translation for current language"""
        return self.translations[self.current_language].get(key, key)

    def switch_language(self):
        """Toggle between English and German"""
        self.current_language = 'de' if self.current_language == 'en' else 'en'


class RecipeAgent:
    """
    Handles recipe recommendations based on user preferences.
    Uses TheMealDB API to fetch real recipes.
    """

    def __init__(self):
        self.cuisine = ""
        self.dishes = ""
        self.flavors = ""
        self.base_url = "https://www.themealdb.com/api/json/v1/1"

    def save_preferences(self, cuisine, dishes, flavors):
        """Store what the user told us about their food preferences"""
        self.cuisine = cuisine.strip()
        self.dishes = dishes.strip()
        self.flavors = flavors.strip()

    def fetch_by_cuisine(self, cuisine_name):
        """Get recipes from a specific cuisine"""
        try:
            endpoint = f"{self.base_url}/filter.php?a={cuisine_name}"
            response = requests.get(endpoint, timeout=15)

            if response.status_code == 200:
                data = response.json()
                meals = data.get('meals', [])
                return meals if meals else []
            else:
                return []

        except requests.exceptions.Timeout:
            print("Request timed out")
            return []
        except requests.exceptions.ConnectionError:
            print("No internet connection")
            return []
        except Exception as error:
            print(f"Error: {error}")
            return []

    def fetch_by_ingredient(self, ingredient_name):
        """Find recipes with a specific ingredient"""
        try:
            endpoint = f"{self.base_url}/filter.php?i={ingredient_name}"
            response = requests.get(endpoint, timeout=15)

            if response.status_code == 200:
                data = response.json()
                meals = data.get('meals', [])
                return meals if meals else []
            else:
                return []

        except Exception as error:
            print(f"Error fetching by ingredient: {error}")
            return []

    def fetch_by_name(self, dish_name):
        """Search for recipes by dish name"""
        try:
            endpoint = f"{self.base_url}/search.php?s={dish_name}"
            response = requests.get(endpoint, timeout=15)

            if response.status_code == 200:
                data = response.json()
                meals = data.get('meals', [])
                return meals if meals else []
            else:
                return []

        except Exception as error:
            print(f"Error searching by name: {error}")
            return []

    def build_recommendation_list(self):
        """
        Generate personalized recipe recommendations.
        Combines results from multiple searches.
        """
        all_results = []

        # Search by cuisine
        if self.cuisine:
            cuisine_recipes = self.fetch_by_cuisine(self.cuisine)
            if cuisine_recipes:
                all_results.extend(cuisine_recipes[:5])

        # Search by favorite dishes
        if self.dishes:
            dish_list = [d.strip() for d in self.dishes.split(',') if d.strip()]

            for dish in dish_list[:3]:
                dish_recipes = self.fetch_by_name(dish)
                if dish_recipes:
                    all_results.extend(dish_recipes[:2])

        # Search by flavor keywords
        if self.flavors:
            flavor_text = self.flavors.lower()

            ingredient_keywords = {
                'chicken': ['chicken', 'poultry', 'hähnchen', 'huhn'],
                'beef': ['beef', 'meat', 'steak', 'rind', 'fleisch'],
                'fish': ['fish', 'seafood', 'fisch', 'meeresfrüchte'],
                'pasta': ['pasta', 'noodle', 'nudel'],
                'rice': ['rice', 'reis'],
                'vegetable': ['vegetable', 'veggie', 'gemüse'],
                'spicy': ['spicy', 'hot', 'chili', 'scharf'],
                'sweet': ['sweet', 'dessert', 'süß']
            }

            for ingredient, keywords in ingredient_keywords.items():
                for keyword in keywords:
                    if keyword in flavor_text:
                        flavor_recipes = self.fetch_by_ingredient(ingredient)
                        if flavor_recipes:
                            all_results.extend(flavor_recipes[:2])
                        break

        # Remove duplicates
        unique_recipes = []
        seen_ids = set()

        for recipe in all_results:
            meal_id = recipe.get('idMeal')
            if meal_id and meal_id not in seen_ids:
                seen_ids.add(meal_id)
                unique_recipes.append(recipe)

        return unique_recipes[:10]


class RoundedButton(Button):
    """Custom button with rounded corners and smooth animations"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)  # Transparent

        with self.canvas.before:
            self.bg_color = Color(0.25, 0.6, 0.85, 1)
            self.bg_rect = RoundedRectangle(
                pos=self.pos, 
                size=self.size, 
                radius=[15]
            )

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def on_press(self):
        # Scale down animation
        anim = Animation(size=(self.width * 0.95, self.height * 0.95), duration=0.1)
        anim.start(self)

    def on_release(self):
        # Scale back up
        anim = Animation(size=(self.width / 0.95, self.height / 0.95), duration=0.1)
        anim.start(self)


class LeckerApp(App):
    """
    Main application class for Lecker Recipe Finder.
    Bilingual support: English and German.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Lecker'
        self.agent = RecipeAgent()
        self.lang = LanguageManager()
        self.step = 0
        self.user_answers = []

    def build(self):
        """Set up the initial UI"""
        self.root_layout = FloatLayout()

        # Main content container
        self.content_box = BoxLayout(
            orientation='vertical', 
            padding=25, 
            spacing=18,
            size_hint=(0.9, 0.85),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Language switch button (top right)
        self.lang_button = Button(
            text=self.lang.get('language_switch'),
            size_hint=(None, None),
            size=(120, 45),
            pos_hint={'right': 0.98, 'top': 0.98},
            font_size='14sp',
            background_color=(0.95, 0.95, 0.95, 1),
            color=(0.2, 0.2, 0.2, 1)
        )
        self.lang_button.bind(on_press=self.toggle_language)
        self.root_layout.add_widget(self.lang_button)

        # App title
        self.title_label = Label(
            text=self.lang.get('app_title'),
            size_hint_y=None,
            height=70,
            font_size='32sp',
            bold=True,
            color=(0.15, 0.35, 0.75, 1)
        )
        self.content_box.add_widget(self.title_label)

        # Subtitle
        self.subtitle_label = Label(
            text=self.lang.get('subtitle'),
            size_hint_y=None,
            height=35,
            font_size='16sp',
            color=(0.4, 0.4, 0.4, 1),
            italic=True
        )
        self.content_box.add_widget(self.subtitle_label)

        # Spacer
        self.content_box.add_widget(Label(size_hint_y=None, height=20))

        # Question display
        self.question_display = Label(
            text=self.lang.get('question_1'),
            size_hint_y=None,
            height=80,
            font_size='18sp',
            color=(0.1, 0.1, 0.1, 1),
            halign='center',
            valign='middle',
            bold=True
        )
        self.question_display.bind(size=self.question_display.setter('text_size'))
        self.content_box.add_widget(self.question_display)

        # Hint text
        self.hint_label = Label(
            text=self.lang.get('question_1_hint'),
            size_hint_y=None,
            height=50,
            font_size='14sp',
            color=(0.5, 0.5, 0.5, 1),
            halign='center',
            valign='middle',
            italic=True
        )
        self.hint_label.bind(size=self.hint_label.setter('text_size'))
        self.content_box.add_widget(self.hint_label)

        # Text input with better styling
        self.answer_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=55,
            font_size='17sp',
            hint_text=self.lang.get('input_placeholder'),
            padding=[15, 18],
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=(0.25, 0.6, 0.85, 1),
            hint_text_color=(0.6, 0.6, 0.6, 1)
        )
        self.content_box.add_widget(self.answer_input)

        # Error message label
        self.error_label = Label(
            text='',
            size_hint_y=None,
            height=0,
            font_size='15sp',
            color=(0.9, 0.2, 0.2, 1),
            bold=True
        )
        self.content_box.add_widget(self.error_label)

        # Next button (using custom rounded button)
        self.next_button = RoundedButton(
            text=self.lang.get('next_button'),
            size_hint_y=None,
            height=60,
            font_size='19sp',
            color=(1, 1, 1, 1),
            bold=True
        )
        self.next_button.bind(on_release=self.handle_answer)
        self.content_box.add_widget(self.next_button)

        # Results scroll view
        self.results_scroll = ScrollView(size_hint=(1, 1))
        self.results_container = GridLayout(
            cols=1,
            spacing=15,
            size_hint_y=None,
            padding=15
        )
        self.results_container.bind(
            minimum_height=self.results_container.setter('height')
        )
        self.results_scroll.add_widget(self.results_container)

        self.root_layout.add_widget(self.content_box)

        return self.root_layout

    def toggle_language(self, instance):
        """Switch between English and German"""
        self.lang.switch_language()

        # Update language button text
        self.lang_button.text = self.lang.get('language_switch')

        # Rebuild UI with new language
        if self.step < 3:
            # Still in question phase
            self.update_question_ui()
        else:
            # In results phase - just update button text
            self.lang_button.text = self.lang.get('language_switch')

    def update_question_ui(self):
        """Update all UI text for current question"""
        self.title_label.text = self.lang.get('app_title')
        self.subtitle_label.text = self.lang.get('subtitle')

        # Update question text
        question_key = f'question_{self.step + 1}'
        hint_key = f'question_{self.step + 1}_hint'
        self.question_display.text = self.lang.get(question_key)
        self.hint_label.text = self.lang.get(hint_key)

        # Update input placeholder
        self.answer_input.hint_text = self.lang.get('input_placeholder')

        # Update button text
        if self.step == 2:
            self.next_button.text = self.lang.get('find_recipes_button')
        else:
            self.next_button.text = self.lang.get('next_button')

    def show_error(self, message_key):
        """Display an error message"""
        self.error_label.text = self.lang.get(message_key)
        self.error_label.height = 50

        # Fade in animation
        self.error_label.opacity = 0
        anim = Animation(opacity=1, duration=0.3)
        anim.start(self.error_label)

    def hide_error(self):
        """Clear the error message"""
        self.error_label.text = ''
        self.error_label.height = 0

    def handle_answer(self, button_instance):
        """Process the user's answer"""
        user_input = self.answer_input.text.strip()

        # Validate input
        if not user_input:
            self.show_error('error_empty')
            return

        if len(user_input) < 3:
            self.show_error('error_too_short')
            return

        # Input is valid
        self.hide_error()
        self.user_answers.append(user_input)
        self.answer_input.text = ''
        self.step += 1

        # Check if more questions remain
        if self.step < 3:
            self.update_question_ui()
        else:
            # All questions answered
            self.show_loading_screen()
            self.get_recommendations()

    def show_loading_screen(self):
        """Show loading animation"""
        self.question_display.text = self.lang.get('loading_text')
        self.hint_label.text = self.lang.get('loading_subtitle')
        self.next_button.disabled = True
        self.answer_input.disabled = True

        # Pulsing animation for loading text
        anim = Animation(opacity=0.5, duration=0.8) + Animation(opacity=1, duration=0.8)
        anim.repeat = True
        anim.start(self.question_display)

    def get_recommendations(self):
        """Fetch and display recommendations"""
        # Save preferences
        self.agent.save_preferences(
            cuisine=self.user_answers[0],
            dishes=self.user_answers[1],
            flavors=self.user_answers[2]
        )

        # Get recommendations
        recommendations = self.agent.build_recommendation_list()

        # Clear current UI
        self.content_box.clear_widgets()

        # Results title
        results_title = Label(
            text=self.lang.get('results_title'),
            size_hint_y=None,
            height=65,
            font_size='26sp',
            bold=True,
            color=(0.15, 0.35, 0.75, 1)
        )
        self.content_box.add_widget(results_title)

        # Subtitle with count
        if recommendations:
            subtitle_text = f"{len(recommendations)} {self.lang.get('recipe_count')}"
        else:
            subtitle_text = self.lang.get('results_subtitle')

        results_subtitle = Label(
            text=subtitle_text,
            size_hint_y=None,
            height=40,
            font_size='15sp',
            color=(0.4, 0.4, 0.4, 1),
            italic=True
        )
        self.content_box.add_widget(results_subtitle)

        # Display results or error
        if recommendations:
            self.results_container.clear_widgets()

            for index, recipe in enumerate(recommendations, start=1):
                recipe_card = self.create_recipe_card(index, recipe)
                self.results_container.add_widget(recipe_card)

                # Stagger animations for smooth appearance
                recipe_card.opacity = 0
                anim = Animation(opacity=1, duration=0.4)
                anim.start(recipe_card)

            self.content_box.add_widget(self.results_scroll)

            # Restart button
            restart_button = RoundedButton(
                text=self.lang.get('start_over'),
                size_hint_y=None,
                height=60,
                font_size='18sp',
                color=(1, 1, 1, 1),
                bold=True
            )
            restart_button.bg_color.rgba = (0.75, 0.25, 0.25, 1)
            restart_button.bind(on_release=self.restart_app)
            self.content_box.add_widget(restart_button)

        else:
            # No results found
            no_results = Label(
                text=self.lang.get('no_results'),
                size_hint_y=None,
                height=80,
                font_size='18sp',
                color=(0.7, 0.2, 0.2, 1),
                bold=True
            )
            self.content_box.add_widget(no_results)

            no_results_subtitle = Label(
                text=self.lang.get('no_results_subtitle'),
                size_hint_y=None,
                height=50,
                font_size='15sp',
                color=(0.5, 0.5, 0.5, 1)
            )
            self.content_box.add_widget(no_results_subtitle)

            retry_button = RoundedButton(
                text=self.lang.get('try_again'),
                size_hint_y=None,
                height=60,
                font_size='18sp',
                color=(1, 1, 1, 1),
                bold=True
            )
            retry_button.bind(on_release=self.restart_app)
            self.content_box.add_widget(retry_button)

    def create_recipe_card(self, number, recipe):
        """Create a modern recipe card"""
        card = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=120,
            padding=15,
            spacing=10
        )

        # Add background
        with card.canvas.before:
            Color(1, 1, 1, 1)
            card.bg_rect = RoundedRectangle(
                pos=card.pos, 
                size=card.size, 
                radius=[12]
            )
        card.bind(pos=lambda *args: setattr(card.bg_rect, 'pos', card.pos))
        card.bind(size=lambda *args: setattr(card.bg_rect, 'size', card.size))

        # Recipe name
        name_label = Label(
            text=f"{number}. {recipe.get('strMeal', 'Unknown')}",
            size_hint_y=None,
            height=40,
            font_size='17sp',
            bold=True,
            color=(0.1, 0.1, 0.1, 1),
            halign='left',
            valign='middle'
        )
        name_label.bind(size=name_label.setter('text_size'))
        card.add_widget(name_label)

        # View button
        view_button = RoundedButton(
            text=f"🍽️  {self.lang.get('view_recipe')}",
            size_hint_y=None,
            height=50,
            font_size='16sp',
            color=(1, 1, 1, 1),
            bold=True
        )
        view_button.bg_color.rgba = (0.3, 0.7, 0.4, 1)
        view_button.recipe_id = recipe.get('idMeal')
        view_button.bind(on_release=self.open_recipe_url)
        card.add_widget(view_button)

        return card

    def open_recipe_url(self, button_instance):
        """Open recipe in browser"""
        recipe_id = button_instance.recipe_id
        if recipe_id:
            url = f"https://www.themealdb.com/meal/{recipe_id}"
            try:
                webbrowser.open(url)
            except Exception as error:
                print(f"Couldn't open browser: {error}")

    def restart_app(self, button_instance):
        """Reset and start over"""
        self.step = 0
        self.user_answers = []
        self.agent = RecipeAgent()

        # Fade out animation
        anim = Animation(opacity=0, duration=0.2)
        anim.bind(on_complete=lambda *args: self.rebuild_ui())
        anim.start(self.content_box)

    def rebuild_ui(self):
        """Rebuild the UI from scratch"""
        self.root_layout.clear_widgets()
        self.build()

        # Fade in animation
        self.content_box.opacity = 0
        anim = Animation(opacity=1, duration=0.3)
        anim.start(self.content_box)


# Run the app
if __name__ == '__main__':
    LeckerApp().run()
