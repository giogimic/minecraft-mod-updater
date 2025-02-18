# Minecraft Mod Auto-Updater

## Overview

The **Minecraft Mod Auto-Updater** is a Python script designed to automate the process of updating Minecraft mods within a specified directory. It ensures that all mods are updated to their latest versions compatible with a specified Minecraft version (e.g., 1.20.1), streamlining the maintenance of modded Minecraft environments.

## Features

- **Automatic Mod Updates:** Scans the specified mods directory and updates each mod to the latest compatible version for the specified Minecraft version.
- **Backup of Old Mods:** Before updating, the script moves outdated mods to a `backup` folder within the mods directory, preserving previous versions.
- **Compatibility Check:** Ensures that only mods compatible with the specified Minecraft version are downloaded and installed.
- **Logging:** Provides console output indicating the status of each mod (e.g., updated, already up to date, or no compatible version found).

## Prerequisites

- **Python Version:** 3.7 or higher
- **Required Libraries:** `requests` library (install via `pip install requests`)
