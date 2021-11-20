#!/bin/bash
python3 -m visdom.server -port 1337
python3 main.py --model hamida --dataset WATER_HSI --training_sample 0.85 --epoch 50 --cuda 0  --class_balancing