# First Model
Create model from train datasets of gtsrb-small datasets.
Most of layers are copied from lecture.
the model has 32 convolutional filters so that I can distill the essence of the image
After convolution, I applied Pooling layer of (2, 2) to reduce the amount of inputs.
Then I flatten cell by cell to inputs of the neural network, which then will have 128 hidden layers and while attempting to create a model, dropout will randomly picks up 50% of the neurons so that overfitting is hopefully avoided.

The last layer will have the same number of outputs as number of the categories in the dataset.

The resulting model's accuracy was 0.9970, and loss was 0.0076.

# Second Model
I reduced the number of filters to 16 and accuracy is not dropping

# third model
I changed the number of filters back to 32 and then reduced the number of hidden units in the hidden layer to 64 and accuracy is still not dropping

# Fourth Model
The number of filters 16
The number of hidden units 64
accuracy is a bit fracutuating but still not dropping

# Fifth Model
the hidden units 32
filters 16
accuracy weas 0.85 0.99 0.92
accuracy is not stable enough 

# Sixth Model
I changed the number of filters back to 32.
hidden units 32
accuracy was 0.633, 0.622 0.633
It looks like that the more filters, the more overly filters change the image. 

# Seventh Model
I changed the pooling filter grid from (2, 2) to (3, 3).
the accuracy was 1.00, 0.985 0.91, and then 0.636
I thought that this might be an optimal pooling filter size, but sometimes accuracy plummets. 

# Eighth Model
Changed dropout ratio to 0.3.
The highest accuracy has been always 1.00 from this datasets, but after reducing the dropout ratio, accuracy is slightly decreased by 0.01 - 0.03.
I assume this is becasue of overfitting the model meaning the model is losing the generalization ability.
So I should bring back to 0.5

# Nineth Model 
I tried to add 2 layers of the size of 32 hidden layers.
And accuracy was less than 0.85. 

# Last Model
32 size of convolutional layer
(3, 3) pooling layer
64 size of hidden layer
0.5 dropout ratio
accuracy was around 0.98 on multiple attempts so this might be costly suitable model for me.