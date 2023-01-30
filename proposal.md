# Practicum Sprint 1

## Team Name (if applicable)

## Tentative Team Members & Roles (if applicable)
1. Yoon Choi (jchoi471@gatech.edu) - Developer
2. Hoesu Chun (hchun33@gatech.edu) - Developer
3. Yuna Lee (ylee847@gatech.edu) - Developer

## 1st Project Choice

### Topic
Deep Learning on X-ray - Classifying diseases (Covid19, Pneumonia, Tuberculosis)

### Project Type
Personally Defined Project

### Problem Summary
Deep Learning, especially Convolutional Neural Networks, has recently been very successful in computer vision. It has evolved to better manpower in some specific tasks. Our team will exploit the latest technology to identify human diseases such as Covid19, Pneumonia, and Tuberculosis in X-ray images.

### Proposed Solution
Our team will train a Convolutional Neural Network to identify human diseases in X-ray images. If time allows, our team will provide a web interface where a user can upload his/her X-ray image and get the analyzed results.

### Potential Blockers (provide mitigation ideas if possible)
Training a deep neural network requires a huge computer resource. Given resource constraints, our team may consider using cloud computing. In addition, deploying a model with a web interface may involve various technical difficulties and potential costs. Our team may consider a local deployment option with Docker.

## 2nd Project Choice

### Topic
Machine Learning to predict Stroke

### Project Type
Personally Defined Project

### Problem Summary
According to CDC, "1 in 6 deaths from cardiovascular disease was due to stroke" and someone in the U.S. has a stroke every 40 seconds [2]. As we can see, a stroke is a very big problem in the U.S. Our team will utilize machine learning techniques & data related to stroke to determine contributing factors to stroke and predict them given one's health conditions.

### Proposed Solution
We will explore various machine learning techniques to predict stroke within acceptable margins. Not only that, if we have enough time, we will make a web application where one can upload personal information, such as BMI and glucose levels, to help identify one's likelihood of having a stroke.

### Potential Blockers (provide mitigation ideas if possible)
Deploying a web application may take a bit of time, which we could have spent on developing a machine learning model. We will mitigate this by learning about various frontend and backend frameworks used commonly in the industry to speed the process.

## 3rd Project Choice
### Topic
Cataract Detection on Retinal Image Using Deep Learning

### Project Type
Personally Defined Project

### Problem Summary
A cataract is a prevalent disease among seniors. According to a national eye institute, more than half of US citizens aged 80 or older either have cataracts or have had surgery to remove it. [3] Since they even can lead to vision loss, it is important to discover them at the right moment when they happen. Our team will utilize transfer learning on the photographs of left and right eyes to identify whether they have a cataract.

### Proposed Solution
We will utilize VGG19 architecture to detect cataracts in retinal images. Additionally, if possible, we will build a web interface to identify whether uploaded retinal images have cataracts.

### Potential Blockers (provide mitigation ideas if possible)
The dataset has many more normal images than the images with cataracts. To deal with these unbalanced datasets appropriately, we will do up-sampling or down-sampling before training it. Besides, to train image datasets, we will utilize GPU provided by Google Colab. Like 1st and 2nd projects, web deployment is another problem, but we will mitigate it similarly.

## References
1. Sitaula, C., Hossain, M.B. Attention-based VGG-16 model for COVID-19 chest X-ray image classification. Appl Intell 51, 2850–2863 (2021). https://doi.org/10.1007/s10489-020-02055-x
2. Centers for Disease Control and Prevention. (2022, October 14). Stroke facts. Centers for Disease Control and Prevention. Retrieved January 29, 2023, from https://www.cdc.gov/stroke/facts.htm
3. National Eye Institute. (2023, January 13). Cataracts. https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/cataracts