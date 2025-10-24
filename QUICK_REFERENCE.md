# Quick Reference Card - Lecker

## App Name
**Lecker** - German for "delicious" 🍽️

## Testing Commands

```bash
# Test on desktop
python main.py

# Build for Android
buildozer android debug

# Deploy to Android device
buildozer android deploy run
```

## Git Commands

```bash
# Initialize and upload
git init
git add .
git commit -m "Initial commit: Lecker v1.0.0"
git remote add origin https://github.com/FallenGodfather/lecker-recipe-app.git
git push -u origin main

# Future updates
git add .
git commit -m "Your message here"
git push
```

## New Features in This Version

### Bilingual Support
- 🇬🇧 English
- 🇩🇪 German ([translate:Deutsch])
- Instant language switching
- All text translated

### UI Improvements
- Smooth fade animations
- Rounded corners
- Modern color scheme
- Better spacing
- Custom button component
- Loading animations

## Language Toggle

Tap the language button (top right) to switch between:
- English → German
- German → English

## File Structure

```
lecker-recipe-app/
├── main.py                 # Main app (bilingual)
├── requirements.txt        # Dependencies
├── buildozer.spec         # Android config
├── README.md              # Documentation
├── LICENSE                # MIT License
├── .gitignore            # Git ignore
├── CONTRIBUTING.md        # How to contribute
├── CHANGELOG.md          # Version history
└── QUICK_REFERENCE.md    # This file
```

## Test Cases

1. **Language Switch Test**
   - Open app
   - Tap language button
   - Verify all text changes
   - Expected: Smooth transition to German/English

2. **Valid Input Test (English)**
   - Cuisine: Italian
   - Dishes: Pasta, Pizza
   - Flavors: Savory and cheesy
   - Expected: 10 recipe recommendations

3. **Valid Input Test (German)**
   - [translate:Küche]: [translate:Italienisch]
   - [translate:Gerichte]: [translate:Pasta, Pizza]
   - [translate:Geschmack]: [translate:herzhaft]
   - Expected: 10 recommendations

4. **Invalid Input Test**
   - Leave fields empty
   - Expected: Error in current language

5. **Animation Test**
   - Watch for smooth transitions
   - Button press animations
   - Card fade-in effects
   - Loading screen pulse

## UI Components

### RoundedButton
- Custom Kivy button
- Rounded corners (15px radius)
- Scale animation on press
- Customizable colors

### LanguageManager
- Stores all translations
- Supports English & German
- Easy to add more languages
- get() method for lookups

## Translations

Key translations in the app:

| English | German ([translate:Deutsch]) |
|---------|--------|
| Next | [translate:Weiter] |
| Find Recipes | [translate:Rezepte finden] |
| Start Over | [translate:Neu starten] |
| View Recipe | [translate:Rezept ansehen] |
| Your Personalized Recipes | [translate:Deine personalisierten Rezepte] |

## Author Info

- **Name**: Hassan Ali
- **GitHub**: FallenGodfather
- **Email**: hassanalijadavjee.work@gmail.com
- **License**: MIT
- **App Name**: Lecker (Delicious)

## Support

- Issues: https://github.com/FallenGodfather/lecker-recipe-app/issues
- Docs: See README.md
- Contributing: See CONTRIBUTING.md

## Performance Notes

- Animations run at 60 FPS
- Language switch is instant
- API calls timeout after 15 seconds
- Smooth transitions throughout
- Responsive on all devices
