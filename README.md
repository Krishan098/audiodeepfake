# Audio Deepfake Detection Project

This project helps you build an audio deepfake detection system using ML techniques.

## Setup
1. Run `./setup.sh` to initialize the project
2. Activate the environment: `source .venv/bin/activate`

## Project Structure
- `data_collection.py` - Tools for gathering audio datasets
- `audio_preprocessing.py` - Audio cleaning and standardization 
- `audio_augmentation.py` - Data augmentation techniques
- `feature_extraction.py` - Extract audio features (MFCCs, spectral features, etc)
- `model_training.py` - ML model training and evaluation

## Workflow
1. Collect data using `data_collection.py`
2. Preprocess and segment audio with `audio_preprocessing.py`
3. Augment your dataset with `audio_augmentation.py`
4. Extract features with `feature_extraction.py`
5. Train and evaluate models with `model_training.py`