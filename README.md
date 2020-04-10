# Pap Smear Image Classification with Pytorch

<img width="400" src="misc/pap.png"></img>

## Intro

Cervical cancer is a very common cancer in women worldwide, but it can easily be prevented by either HPV vaccine or frequent pap smear screening. Most of the deaths from cervical cancer occur in low income countries where screening is less available. Even in more developed countries, trained specialist have to face a taxing task of looking at many slides under a microscope just to find a few that are abnormal. Deep learning presents great opportunities for revolutionizing abnormality detection on pap smear slides. In this project we present the result of four experiments we
performed with neural network models trained, validated and tested with the SIPaKMeD pap smear data set. Our models classified respective images with high accuracy levels and could be used to design real life applications that would highly reduce the costs of pap smear screenings and possibly reduce cervical cancer rates.

## Data 
The dataset is publicly available at [SiPaKMed](http://www.cs.uoi.gr/~marina/sipakmed.html). The Database contains 4049 images of isolated cells that have been manually cropped from 966 cluster cell images of Pap smear slides.

## How do you run it

All the code is available in the jupyter notebook, just run the below command. 
```sh
jupyter notebook Model_training.ipynb  
```

## Models

Convolutional neural network (CNN) models we used are VGG-11, Resnet-18, Resnet-50 and Resnet-101. The input to the networks are raw RGB images. They are resized to 224 x 224 pixels. We added Pytroch’s Adaptive-MaxPool and AdaptiveAveragePool2d, flattened them out and concatenated them to form a linear layer. Then we applied a dropout layer with a dropout rate of 0.5 followed with a linear layer.

The optimizer Adam was used to train the models. To make the models converge faster and increase accuracy, we implemented a scheduler which reduces the learning rate at each epoch. Training is terminated after 50 epochs. All the models were trained using Pytorch for Python.

## Results
<img src="misc/confusion_matrix.png"></img>

The table displays the classification of cropped cell images using Resnet50

## Useful Materials Discovered During the Project

1. How to finetune your model.  
https://medium.com/udacity-pytorch-challengers/ideas-on-how-to-fine-tune-a-pre-trained-model-in-pytorch-184c47185a20

2. Startup working on medical diagnostics  
https://www.enlitic.com/
