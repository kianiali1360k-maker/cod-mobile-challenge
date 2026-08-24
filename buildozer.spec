[app]
title = COD Mobile Challenge
package.name = codchallenge
package.domain = org.codchallenge
source.dir = .
source.include_exts = py,png,jpg,jpeg
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 35
android.minapi = 23
android.archs = arm64-v8a
android.accept_sdk_license = True
