# Quick Start Guide - Recipe AI Agent

## Test on Desktop (Easiest Way to Start)

```bash
# 1. Install dependencies
pip install kivy requests

# 2. Run the app
python recipe_agent_app.py
```

## Deploy to Android

```bash
# 1. Install buildozer
pip install buildozer

# 2. Install Android build dependencies (Linux/macOS)
# Ubuntu/Debian:
sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev cmake libffi-dev libssl-dev

# 3. Build APK (first time takes 15-30 minutes)
buildozer android debug

# 4. Find your APK in: bin/recipeagent-0.1-debug.apk
# Transfer to your phone and install!
```

## Deploy to iOS

```bash
# 1. Install tools (macOS only)
brew install autoconf automake libtool pkg-config
pip3 install Cython==0.29.10

# 2. Clone and build kivy-ios
git clone https://github.com/kivy/kivy-ios
cd kivy-ios
./toolchain.py build python3 kivy

# 3. Rename main file
cd ../recipe-ai-agent
mv recipe_agent_app.py main.py

# 4. Create Xcode project
../kivy-ios/toolchain.py create RecipeAgent .

# 5. Open in Xcode and build
open RecipeAgent-ios/RecipeAgent.xcodeproj
```

## How the App Works

1. **User opens app** → Sees first question
2. **Answers 3 questions** about food preferences:
   - Favorite cuisine
   - Favorite dishes
   - Preferred flavors
3. **AI agent processes** preferences
4. **Searches TheMealDB API** for matching recipes
5. **Displays 10 recommendations** with web links
6. **User clicks link** → Opens recipe in browser

## Features

✅ No hardcoded recipes - all from API  
✅ Real-time web search  
✅ Direct links to full recipes  
✅ Works offline after recommendations loaded  
✅ Simple, clean UI  
✅ Cross-platform (iOS + Android)

## Troubleshooting

**Import Error?**
```bash
pip install -r requirements.txt
```

**Buildozer Error?**
- Make sure you have 4GB free space
- Run: `buildozer android clean` then try again

**iOS Build Error?**
- Install Xcode Command Line Tools
- Make sure file is named "main.py" not "recipe_agent_app.py"

## Next Steps

- Edit questions in `recipe_agent_app.py` (line 183)
- Change number of recommendations (line 105)
- Add more API sources (edit RecipeAgent class)
- Customize UI colors (edit Window.clearcolor, button colors)

Ready to build? See README.md for full details!
