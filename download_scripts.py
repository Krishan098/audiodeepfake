import requests
import os

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

# Replace these URLs with actual GitHub Gist URLs or your own hosting
# For now, we'll create the files directly
scripts = {
    "data_collection.py": "https://example.com/data_collection.py",
    "audio_preprocessing.py": "https://example.com/audio_preprocessing.py",
    "audio_augmentation.py": "https://example.com/audio_augmentation.py",
    "feature_extraction.py": "https://example.com/feature_extraction.py",
    "model_training.py": "https://example.com/model_training.py"
}

for filename, url in scripts.items():
    download_file(url, filename)