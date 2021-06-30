# Cassava Leaf Disease Prediction
## Introduction
As Cassava is considered as the second largest provider of carbohydrates in Africa, 80% of household farms in Africa grow this as it can also withstand harah condition. But viral diseases are major sources of poor yields. Existing method of detecting diseases requires the help of government-funded agricultural expert to visually inspect and diagnose the plants. A plant can be diagnosed for any disease easily without the help of government and very early using Deep Learning. This problem is all about classifying Cassava leafs on the basis of disease to which the plant is infected. All you need to provide an image of target plant. Image of plant leaf will be classified to be one class out 5 classes (0 for  Cassava Bacterial Blight (CBB), 1 for Cassava Brown Streak Disease (CBSD), 2 for Cassava Green Mottle (CGM), 3 for Cassava Mosaic Disease (CMD) and 4 for Healthy).
## DataSource
Data includes a folder with images of infected and healthy leafs and a CSV file which includes file name and label of that image to which it belongs. This data is publically accessible on Kaggle. Data for model training consist of 21,367 labeled images which were collected during a regular survey in Uganda and labeled by experts  at the National Crops Resources Research Institute (NaCRRI) in collaboration with the AI lab at Makerere University, Kampala. Random images with its label can be seen below.

![image](https://user-images.githubusercontent.com/66907101/124010026-e9f37f80-d9fb-11eb-911d-e4a5f7a8f386.png)
## Model Training
Tensorflow/Keras has been used for training the model for classifying the images into different classes using architecture of EfficientNetB3 (Different pre trained model has been tried like VGG16, VGG19, etc, but none of them were giving satisfactory accuracy). Sequential model has been used for training this model and the architecture of the model can be seen below.

![image](https://user-images.githubusercontent.com/66907101/124010752-da286b00-d9fc-11eb-8dff-f474bf19ffe1.png)

Using above architecture with image augmentation and using EarlyStopping and  ReduceLROnPlateau Callbacks gives an accuracy of 0.8469 on validating the model on validation data. Hyperparameter Tuning has been tried using Keras-Tunner RandomSearch with 20 trials for 2 epoches which doesn't generates improved accuracy and thus our main model was used for deployment and creating the web app.
