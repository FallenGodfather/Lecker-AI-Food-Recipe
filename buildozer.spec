[app]

# Application Info
title = Lecker
package.name = lecker
package.domain = com.fallengodfather

# Source configuration
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0.0

# Requirements
requirements = python3,kivy==2.3.0,requests

# Display settings
orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Android API levels
android.api = 31
android.minapi = 21

# NDK version
android.ndk = 25b

# Enable AndroidX
android.enable_androidx = True

# App theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# Don't skip updates
android.skip_update = False

# Accept licenses
android.accept_sdk_license = True

# Meta-data
author = Hassan Ali (FallenGodfather)
android.meta_data = com.fallengodfather.lecker

[buildozer]

# Log level (0=error, 1=info, 2=debug)
log_level = 2

# Warn if running as root
warn_on_root = 1
