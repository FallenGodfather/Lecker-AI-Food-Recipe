# Lecker - Recipe Recommendation Agent 🍽️

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Kivy](https://img.shields.io/badge/Kivy-2.3.0-brightgreen.svg)](https://kivy.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-iOS%20%7C%20Android-lightgrey.svg)]()
[![Languages](https://img.shields.io/badge/Languages-English%20%7C%20German-orange.svg)]()

**Lecker** (German for "delicious") is a smart, bilingual mobile app that recommends personalized recipes based on your food preferences. Built with Python and Kivy for seamless cross-platform deployment on iOS and Android.

![Recipe Agent Demo](https://img.shields.io/badge/Status-Active-success)

## ✨ Features

- 🌍 **Bilingual Support** - Switch between English and German with one tap
- 🤖 **AI-Driven Recommendations** - Smart matching based on your preferences
- 🎨 **Modern UI** - Smooth animations and rounded design elements
- 🌐 **Real Recipe Database** - Uses TheMealDB API (2000+ recipes)
- 📱 **Cross-Platform** - Works on iOS and Android
- 🔗 **Web Links** - Each recipe links to detailed cooking instructions
- ✅ **Input Validation** - Won't crash on invalid inputs
- 🚀 **Fast & Smooth** - Animated transitions and responsive design

## 🎯 What Does It Do?

This AI-powered app learns about your food preferences by asking three simple questions:

1. **What's your favorite cuisine?** (Italian, Chinese, Mexican, etc.)
2. **What are your favorite dishes?** (List them out)
3. **What flavors do you enjoy?** (Spicy, sweet, savory, etc.)

Then it searches through thousands of real recipes and gives you **10 personalized recommendations** with direct links to view the full recipes online!

### Language Support

**English** 🇬🇧 and **German** 🇩🇪 are fully supported:
- All UI text translates
- Questions and hints in both languages
- Error messages in your chosen language
- Recipe count and button labels adapt
- Seamless language switching

## 🖼️ Screenshots

*Coming soon - will add screenshots after testing on devices*

## 🛠️ Installation

### For Testing on Desktop

```bash
# Clone the repository
git clone https://github.com/FallenGodfather/lecker-recipe-app.git
cd lecker-recipe-app

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

### For Android

```bash
# Install buildozer
pip install buildozer

# Install build dependencies (Ubuntu/Debian)
sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Build the APK
buildozer android debug

# Install on your device
buildozer android deploy run
```

Your APK will be in `bin/lecker-1.0.0-debug.apk`

### For iOS

```bash
# Install dependencies (macOS only)
brew install autoconf automake libtool pkg-config
pip3 install Cython==0.29.10

# Clone kivy-ios
git clone https://github.com/kivy/kivy-ios
cd kivy-ios

# Build for iOS
./toolchain.py build python3 kivy

# Create Xcode project
./toolchain.py create Lecker /path/to/lecker-recipe-app

# Open and build in Xcode
open Lecker-ios/Lecker.xcodeproj
```

## 📋 Requirements

- Python 3.8 or higher
- Kivy 2.3.0
- requests library
- Internet connection (for fetching recipes)

See `requirements.txt` for complete list.

## 🎮 How to Use

1. **Launch the app**
2. **Choose your language** - Tap the language button (top right)
3. **Answer three questions** about your food preferences
4. **Wait a moment** while it searches for recipes
5. **Browse recommendations** - See your personalized recipe list
6. **Tap "View Recipe"** to see cooking instructions
7. **Enjoy cooking!** 👨‍🍳

## 🌐 Language Examples

### English Interface
- "What's your favorite cuisine?"
- "Find Recipes"
- "Your Personalized Recipes"
- "View Recipe"

### German Interface ([translate:Deutsche Oberfläche])
- [translate:Was ist deine Lieblingsküche?]
- [translate:Rezepte finden]
- [translate:Deine personalisierten Rezepte]
- [translate:Rezept ansehen]

## 🏗️ Project Structure

```
lecker-recipe-app/
│
├── main.py                 # Main application code (bilingual)
├── buildozer.spec          # Android build configuration
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── .gitignore            # Git ignore rules
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md          # Version history
└── QUICK_REFERENCE.md    # Quick commands
```

## 🔧 Technical Details

### Architecture

**LanguageManager Class**
- Stores all translations (English & German)
- Handles language switching
- Provides translation lookup method

**RecipeAgent Class**
- Manages user preferences
- Interacts with TheMealDB API
- Generates personalized recommendations
- Supports multilingual ingredient keywords

**RoundedButton Class**
- Custom button with rounded corners
- Smooth press/release animations
- Customizable colors

**LeckerApp Class**
- Main application logic
- Bilingual UI management
- Smooth animations and transitions
- Modern, responsive design

### UI Enhancements

- ✨ **Smooth Animations** - Fade in/out, scale, and opacity effects
- 🔘 **Rounded Corners** - Modern card design with RoundedRectangle
- 🎨 **Modern Color Scheme** - Carefully chosen colors for readability
- 📏 **Better Spacing** - More breathing room between elements
- 💫 **Loading Animation** - Pulsing text during recipe search
- 🎯 **Responsive Layout** - Adapts to different screen sizes

### API Integration

Uses **TheMealDB API** (https://www.themealdb.com/api.php):
- Free to use
- No authentication required
- 2000+ recipes from various cuisines
- Supports multilingual searches

## 🐛 Bug Fixes & Improvements

From previous version:

- ✅ Added comprehensive input validation
- ✅ Implemented smooth animations throughout
- ✅ Modern UI with rounded corners
- ✅ Bilingual support (English/German)
- ✅ Language toggle button
- ✅ Better error messages
- ✅ Improved spacing and layout
- ✅ Custom button component
- ✅ Staggered card animations
- ✅ Loading screen with animation

## 🚧 Known Issues

- First API call might be slightly slow
- Requires active internet connection
- Some obscure cuisines might not return many results

## 📝 Future Plans

- [ ] Healthy ratings for proper nutrition 
- [ ] Daily Recipes depending on mood and cravings
- [ ] Add more languages (French, Spanish, Italian)
- [ ] Add recipe images/thumbnails
- [ ] Implement favorites/bookmarks
- [ ] Add dietary filters (vegan, gluten-free)
- [ ] Offline mode with cached recipes
- [ ] Recipe ratings
- [ ] Shopping list generator
- [ ] Dark mode
- [ ] Voice input support

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Hassan Ali (FallenGodfather)**

- GitHub: [@FallenGodfather](https://github.com/FallenGodfather)
- Email: hassanalijadavjee.work@gmail.com

## 🙏 Acknowledgments

- [Kivy](https://kivy.org/) - For the amazing cross-platform framework
- [TheMealDB](https://www.themealdb.com/) - For the free recipe API
- [Buildozer](https://github.com/kivy/buildozer) - For easy Android packaging
- Python community - For all the helpful resources

## ⭐ Show Your Support

If you like this project, please give it a ⭐ on GitHub!

## 🌟 Why "Lecker"?

**Lecker** is a German word meaning "delicious" or "tasty". It perfectly captures what this app is all about - finding delicious recipes that match your taste! The name also reflects the app's bilingual nature, bridging English and German speakers.

---

Made with ❤️ and 🇩🇪 by Hassan Ali
