import model
import matplotlib.pyplot as plt
import torch
import data

print("test")
# Pick manual seed
torch.manual_seed(41)

# create model
model_instance = model.Model()

# set criterion (Mean Squared Error)
criterion = torch.nn.MSELoss() # criterion measures how well the prediction of model was

# choose adam optimizer, lr = learning rate (if error doesn't go down after a bunch of iterations lower lr)
optimizer = torch.optim.Adam(model_instance.parameters(), lr=0.001)  # parameters are layers

# train model
x_train = data.x_train
y_train = data.y_train

model_instance.train() # set model to trainingsmode

# Epochs (one run through all the training data)
epochs = 1000
losses = [] # values showing relative difference between pred data and real data

for i in range(epochs):

    y_pred = model_instance(x_train)  # go forward and get a prediction

    loss = criterion(y_pred, y_train)  # predicted values vs the y_train (measure loss/error)

    # keep track of losses
    losses.append(loss.item())

    # print every 10 epoch
    if i % 10 == 0:
        print(f"Epoch: {i} loss: {loss.item():.4f}")

    # back propagation
    # optimizer is an algorithm to update balances of neural network, based on loss
    optimizer.zero_grad()  # sets gradients back to zero
    loss.backward()  # calculate gradients
    optimizer.step()  # updates weights, based on calculated gradients

# plot losses
plt.figure(figsize=(10, 5))
plt.plot(range(1, epochs + 1), losses, label='Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss over epochs')
plt.legend()
plt.grid(True)
plt.show()