#!/bin/bash

pip install torch==1.7.0 torchvision==0.8.1
# pip install \
# tqdm==4.52.0 \
# termcolor==1.1.0 \
# h5py==3.1.0 \
# pandas==1.1.4 \
# tensorboardX==2.1 \
# scikit-learn==0.23.2 \
# matplotlib==3.3.3 \
# torch-scatter==2.0.5 \
# torch-sparse==0.6.8 \
# torch-cluster==1.5.8 \
# torch-spline-conv==1.2.0 \
# torch-geometric==1.6.1
pip install tqdm termcolor pandas h5py tensorboardX scikit-learn matplotlib pretrainedmodels
pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-1.13.0+cu117.html
pip install torch_geometric
