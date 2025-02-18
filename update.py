import os
import requests
import shutil
import json

# Configuration
MODS_DIR = 'path/to/your/mods/folder'  # Replace with the path to your mods directory
MINECRAFT_VERSION = '1.20.1'  # Specify the Minecraft version
BACKUP_DIR = os.path.join(MODS_DIR, 'backup')

# Ensure backup directory exists
os.makedirs(BACKUP_DIR, exist_ok=True)

# Modrinth API endpoint
API_URL = 'https://api.modrinth.com/v2'

def get_mod_info(mod_name):
    """Fetch mod information from Modrinth by mod name."""
    response = requests.get(f'{API_URL}/search', params={'query': mod_name, 'limit': 1})
    if response.status_code == 200:
        results = response.json().get('hits', [])
        if results:
            return results[0]
    return None

def get_latest_version(mod_id):
    """Get the latest version of the mod compatible with the specified Minecraft version."""
    response = requests.get(f'{API_URL}/project/{mod_id}/version')
    if response.status_code == 200:
        versions = response.json()
        for version in versions:
            if MINECRAFT_VERSION in version['game_versions']:
                return version
    return None

def update_mods():
    """Update mods in the specified directory."""
    for filename in os.listdir(MODS_DIR):
        if filename.endswith('.jar'):
            mod_path = os.path.join(MODS_DIR, filename)
            print(f'Checking mod: {filename}')
            mod_name = filename.rsplit('-', 1)[0]  # Extract mod name from filename
            mod_info = get_mod_info(mod_name)
            if mod_info:
                latest_version = get_latest_version(mod_info['project_id'])
                if latest_version:
                    latest_filename = latest_version['files'][0]['filename']
                    if latest_filename != filename:
                        print(f'Updating {filename} to {latest_filename}')
                        # Backup old mod
                        shutil.move(mod_path, os.path.join(BACKUP_DIR, filename))
                        # Download new mod
                        download_url = latest_version['files'][0]['url']
                        response = requests.get(download_url)
                        with open(os.path.join(MODS_DIR, latest_filename), 'wb') as f:
                            f.write(response.content)
                    else:
                        print(f'{filename} is already up to date.')
                else:
                    print(f'No compatible version found for {mod_name} with Minecraft {MINECRAFT_VERSION}.')
            else:
                print(f'No information found for mod: {mod_name}')

if __name__ == '__main__':
    update_mods()
