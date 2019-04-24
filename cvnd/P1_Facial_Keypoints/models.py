import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as I

class Net(nn.Module):
    """ Convolutional Neural Network
        The network architecture is inspired by 1710.00977 [arXiv].
    """
    def __init__(self):
        super(Net, self).__init__()
        
        # How to computer tensor shapes after one conv layer:
        # input tensor shape (batchsize, n, H, W)
        # apply conv. with n output channel, stride S, padding P, FxF kernel
        # output tensor shape (batchsize, n, m, m) with m = (W-F+P)/S + 1

        # Arguments of layers:
        # nn.Conv2d(input channels, output channels, square conv. kernel)
        # nn.MaxPool2d(kernel_size, stride)

        # fixed input tensor shape (batchsize, n, H, W) = (., 1, 224, 224)
        # fixed output tensor shape (., 136)
        
        self.conv1 = nn.Conv2d(1, 32, 5, padding=2)  # (.,32,224,224)
        self.pool1 = nn.MaxPool2d(4, 4)              # (.,32,56,56)
        self.drop1 = nn.Dropout(p=0.1)

        self.conv2 = nn.Conv2d(32, 64, 3, padding=1) # (.,64,56,56)
        self.pool2 = nn.MaxPool2d(4, 4)              # (.,64,14,14)
        self.drop2 = nn.Dropout(p=0.2)

        self.fc1 = nn.Linear(64*14*14,512) # (., 512)
        self.drop3 = nn.Dropout(p=0.3)

        self.fc2 = nn.Linear(512, 136)

    def forward(self, x):
        x = self.drop1(self.pool1(F.relu(self.conv1(x))))
        x = self.drop2(self.pool2(F.relu(self.conv2(x))))
        x = x.view(x.size(0), -1) 
        x = self.drop3(F.relu(self.fc1(x)))
        x = self.fc2(x)
        return x
