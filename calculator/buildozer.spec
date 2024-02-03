[app]

# (required) Title of your application
title = Calculator
# (required) Package name for Android APK, avoid using spaces
package.name = com.miskat.calculator

# (required) Package domain (needed for Android/Java apps)
package.domain = org.calculator

# (optional) Application version
version = 1.0

# (optional) Application icon (replace with the path to your icon file)
icon.filename = cal.png

# (required) Source directory containing the main.py file and other resources
source.dir = .

# (optional) Presplash background color (default is black)
presplash.color = #FFFFFF

# (optional) Presplash image (replace with the path to your presplash image)
# presplash.filename = path/to/your/presplash.png

# (required) List of requirements (Kivy is required)
requirements = kivy

# (optional) Orientation (landscape, portrait, or all)
orientation = portrait

# (optional) Build dependencies for APK
# For example, you might need specific libraries or dependencies
# android.gradle_dependencies = com.android.support:support-v4:24.1.1

# (optional) Android API to use for the APK
android.api = 29

# (optional) Minimum API required by your APK
android.minapi = 21

# (optional) Android SDK version to use
# android.sdk = 20

# (optional) Android NDK version to use
# android.ndk = 21.4.7075529

# (optional) Android permissions
# android.permissions = INTERNET

# (optional) Android components (services, activities)
# android.services = com.android.example.MyService
# android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-1234567890123456~1234567890

# (optional) Preset for compilation (default is debug)
# profile = release

