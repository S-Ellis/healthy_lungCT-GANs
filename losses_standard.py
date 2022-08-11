#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Sam Ellis
Copyright 2022 Sam Ellis, King's College London
"""

import torch
import torch.nn as nn

criterion = nn.BCELoss()

def loss_gen(critic_real, critic_fake):
    batch_size = critic_fake.shape[0]
    
    real_labels = torch.full((batch_size,), 1.0, device=critic_fake.device)
    
    errG = criterion(torch.sigmoid(critic_fake),real_labels)
                    
    return errG    
    
    
def loss_dis(critic_real, critic_fake):
    batch_size = critic_real.shape[0]
    
    fake_labels = torch.full((batch_size,), 0.0, device=critic_real.device)
    real_labels = torch.full((batch_size,), 1.0, device=critic_real.device)
    
    errD_real = criterion(torch.sigmoid(critic_real),real_labels)
    
    errD_fake = criterion(torch.sigmoid(critic_fake),fake_labels)
    
    errD = errD_real + errD_fake
    
    return errD