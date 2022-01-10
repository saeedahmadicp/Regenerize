
# Description
The idea implemented by our project is to colorize grey, worn-out pictures. To achieve accuracy, we gathered a large amount of dataset from “keddle.com” and google search images. We removed the noise from our dataset by deleting irrelevant data, then we divided it into different classes by grouping pictures of each type into separate folders.Then, we fed this data into our model to train it. After satisfactory numbers of epochs and accuracy, we tested it to validate our requirements.

# Detailed problem Statement
## Aim of the Project:
When we were implementing our project, we realized how useful Artificial Intelligence can be to solve our day-to-day lives. We also wished to create a platform to deliver what we have learnt to other people. So, to prove that we chose a very practical project that can be easily explained to a beginner wishing to start with their exploration. The aim of the object simply was to achieve a successfully trained model with an accuracy of over 85%. To give the user ease of access, we wanted to design an interface that makes it easier for the user to upload any image of “landscape” or “human” type. Then, the picture will be stored in the same directory from where the user can easily get hold of it. The user can colorize any number of photos by entering one picture at a time. Not only that, but also we were able to make a fully customized website that contains the relevant documentation and guide for our project along with the code.

## Deliverables:
The deliverables of the project include an application, a website, a comprehensive presentation presenting the complete project, a complete folder of the code containing the comprehension for the ease of understanding, and  samples  of inputted black and white images and their related colorized images achieved by our encoder.   

# Approach to Solution
To achieve the solution to the problem, we firstly tried to make a basic algorithm. The basic algorithm of the model is as follows:
Convert our presented dataset into latent-state representations.(encoding) 
Detect the lightest pixel: mark it as the lightest
Detect the darkest shade: mark it as darkest
Compare the mid-tones with the shadows and highlights and then colorize them accordingly.
If it is a portrait, it needs to detect the features and then colorize them according to the training done.
Produce a reconstructed input from the presented latent-state representation. (decoding)
Compare it to the original dataset image, and deduce the accuracy percentage.
Loop through until the maximum number of epochs reached or a specified accuracy reached.
 


