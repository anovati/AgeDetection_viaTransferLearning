# Age Detection from Facial Features via Transfer Learning: a CV project
An  hands-on exploration of the concept of Transfer Learning & Fine-Tuning.
The task is about determining the categorical age of people based on their facial feature. This is done by fine-tuning a general purpose CV Neural Network (MobileNetV2) which is fine-tuned to gain expertise on face evaluation for age detection.

For this project, the Kaggle [*facial_age*]([url](https://www.kaggle.com/datasets/frabbisw/facial-age)) dataset was used for the fine-tuned training of the model.

## Goal
The goal of this project was to learn how to exploit previous, more thorough learning of a Deep CNN over a much more extensive and varied dataset for a more specific application such as Age Detection. I studied the performance of the fine-tuning process when applied into deeper and deeper layers of the newtwork. 

## Repository Structure
* _Age_Classification_through_Transfer_Learning.ipynb_ is the project notebook. It contains the whole project, with a step-by-step description and considerations over the results obtained from the experiments.
* _src_ folder contains some helper functions source code necessary for dataset pre-processing.
* _input_ folder contains only a _readme.txt_ file with instructions over how to obtain the dataset, which is then preprocessed as described in the notebook
* _output_ folder contains the data obtained from training/fine-tuning the models.

## Framework
Project realized in TensorFlow Keras

