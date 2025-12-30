# Vehicle Damage Classification using Deep Learning

This project focuses on building a deep learning model to classify vehicle damage from images.  
The main objective is to learn visual damage patterns using convolutional neural networks and transfer learning techniques.

---

## Problem Definition

Given an image of a vehicle, the model predicts the damage type and location.  
This is formulated as a **multi-class image classification** problem.

---

## Damage Categories

The dataset contains six classes:

- Front Breakage  
- Front Crushed  
- Front Normal  
- Rear Breakage  
- Rear Crushed  
- Rear Normal  

---

## Models Used

### Custom CNN (Baseline)
- Implemented using PyTorch
- Multiple convolution blocks with:
  - Conv2D
  - Batch Normalization
  - ReLU activation
  - Max Pooling
- Fully connected layers with Dropout
- Used to understand feature learning from scratch

### ResNet50 (Transfer Learning)
- Pretrained on ImageNet
- Early layers frozen to reuse learned features
- Fine-tuned:
  - Layer4
  - Final fully connected layer
- Custom classification head for 6 classes

Transfer learning significantly improved accuracy and training stability.

---

## Techniques Applied

- Transfer Learning
- Fine-tuning pretrained networks
- Layer freezing and selective unfreezing
- Dropout for regularization
- Batch Normalization
- Image normalization using ImageNet statistics
- Cross-Entropy loss for multi-class classification
- Adam optimizer

---

## Hyperparameter Optimization

Hyperparameters were tuned using **Optuna**, including:
- Learning rate
- Dropout rate

Each Optuna trial:
- Trains the model for a few epochs
- Evaluates validation accuracy
- Selects the best-performing configuration

---

## Training Workflow

1. Image loading and preprocessing
2. Resizing and normalization
3. Model initialization with pretrained weights
4. Freezing and fine-tuning selected layers
5. Training using backpropagation
6. Validation on unseen data
7. Saving trained model weights

---

## Project Structure

- training/        → Model training and experiments  
- streamlit-app/   → Inference interface  
- fastapi-server/  → API wrapper  
- model/           → Saved trained model  

---

## Key Learnings

- Pretrained models capture strong low-level and mid-level features
- Fine-tuning only selected layers helps prevent overfitting
- Transfer learning reduces training time significantly
- Hyperparameter tuning improves generalization




