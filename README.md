# Image Classifier by ANN

This project builds a simple artificial neural network to classify handwritten digits from the MNIST dataset using TensorFlow and Keras.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python numberPredict.py
```

## Notes

- The script loads MNIST data from Keras.
- It normalizes pixel values to the range 0-1.
- It trains a dense feed-forward ANN for digit classification.
