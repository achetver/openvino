# ******************************************************************************
# Copyright 2017-2020 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************


from ngraph.opset1.ops import absolute
from ngraph.opset1.ops import absolute as abs
from ngraph.opset1.ops import acos
from ngraph.opset4.ops import acosh
from ngraph.opset1.ops import add
from ngraph.opset1.ops import asin
from ngraph.opset4.ops import asinh
from ngraph.opset3.ops import assign
from ngraph.opset1.ops import atan
from ngraph.opset4.ops import atanh
from ngraph.opset1.ops import avg_pool
from ngraph.opset1.ops import batch_norm_inference
from ngraph.opset2.ops import batch_to_space
from ngraph.opset1.ops import binary_convolution
from ngraph.opset3.ops import broadcast
from ngraph.opset3.ops import bucketize
from ngraph.opset1.ops import ceiling
from ngraph.opset1.ops import ceiling as ceil
from ngraph.opset1.ops import clamp
from ngraph.opset1.ops import concat
from ngraph.opset1.ops import constant
from ngraph.opset1.ops import convert
from ngraph.opset1.ops import convert_like
from ngraph.opset1.ops import convolution
from ngraph.opset1.ops import convolution_backprop_data
from ngraph.opset1.ops import cos
from ngraph.opset1.ops import cosh
from ngraph.opset1.ops import ctc_greedy_decoder
from ngraph.opset4.ops import ctc_loss
from ngraph.opset3.ops import cum_sum
from ngraph.opset3.ops import cum_sum as cumsum
from ngraph.opset1.ops import deformable_convolution
from ngraph.opset1.ops import deformable_psroi_pooling
from ngraph.opset1.ops import depth_to_space
from ngraph.opset1.ops import detection_output
from ngraph.opset1.ops import divide
from ngraph.opset1.ops import elu
from ngraph.opset3.ops import embedding_bag_offsets_sum
from ngraph.opset3.ops import embedding_bag_packed_sum
from ngraph.opset3.ops import embedding_segments_sum
from ngraph.opset3.ops import extract_image_patches
from ngraph.opset1.ops import equal
from ngraph.opset1.ops import erf
from ngraph.opset1.ops import exp
from ngraph.opset1.ops import fake_quantize
from ngraph.opset1.ops import floor
from ngraph.opset1.ops import floor_mod
from ngraph.opset1.ops import gather
from ngraph.opset1.ops import gather_tree
from ngraph.opset2.ops import gelu
from ngraph.opset1.ops import greater
from ngraph.opset1.ops import greater_equal
from ngraph.opset1.ops import grn
from ngraph.opset1.ops import group_convolution
from ngraph.opset1.ops import group_convolution_backprop_data
from ngraph.opset3.ops import gru_cell
from ngraph.opset1.ops import hard_sigmoid
from ngraph.opset4.ops import hswish
from ngraph.opset1.ops import interpolate
from ngraph.opset1.ops import less
from ngraph.opset1.ops import less_equal
from ngraph.opset1.ops import log
from ngraph.opset1.ops import logical_and
from ngraph.opset1.ops import logical_not
from ngraph.opset1.ops import logical_or
from ngraph.opset1.ops import logical_xor
from ngraph.opset1.ops import lrn
from ngraph.opset4.ops import lstm_cell
from ngraph.opset1.ops import lstm_sequence
from ngraph.opset1.ops import matmul
from ngraph.opset1.ops import max_pool
from ngraph.opset1.ops import maximum
from ngraph.opset1.ops import minimum
from ngraph.opset4.ops import mish
from ngraph.opset1.ops import mod
from ngraph.opset1.ops import multiply
from ngraph.opset2.ops import mvn
from ngraph.opset1.ops import negative
from ngraph.opset4.ops import non_max_suppression
from ngraph.opset3.ops import non_zero
from ngraph.opset1.ops import normalize_l2
from ngraph.opset1.ops import not_equal
from ngraph.opset1.ops import one_hot
from ngraph.opset1.ops import pad
from ngraph.opset1.ops import parameter
from ngraph.opset1.ops import power
from ngraph.opset1.ops import prelu
from ngraph.opset1.ops import prior_box
from ngraph.opset1.ops import prior_box_clustered
from ngraph.opset1.ops import psroi_pooling
from ngraph.opset4.ops import proposal
from ngraph.opset1.ops import range
from ngraph.opset3.ops import read_value
from ngraph.opset4.ops import reduce_l1
from ngraph.opset4.ops import reduce_l2
from ngraph.opset1.ops import reduce_logical_and
from ngraph.opset1.ops import reduce_logical_or
from ngraph.opset1.ops import reduce_max
from ngraph.opset1.ops import reduce_mean
from ngraph.opset1.ops import reduce_min
from ngraph.opset1.ops import reduce_prod
from ngraph.opset1.ops import reduce_sum
from ngraph.opset1.ops import region_yolo
from ngraph.opset2.ops import reorg_yolo
from ngraph.opset1.ops import relu
from ngraph.opset1.ops import reshape
from ngraph.opset1.ops import result
from ngraph.opset1.ops import reverse_sequence
from ngraph.opset3.ops import rnn_cell
from ngraph.opset3.ops import roi_align
from ngraph.opset2.ops import roi_pooling
from ngraph.opset5.ops import round
from ngraph.opset3.ops import scatter_elements_update
from ngraph.opset3.ops import scatter_update
from ngraph.opset1.ops import select
from ngraph.opset1.ops import selu
from ngraph.opset3.ops import shape_of
from ngraph.opset3.ops import shuffle_channels
from ngraph.opset1.ops import sigmoid
from ngraph.opset1.ops import sign
from ngraph.opset1.ops import sin
from ngraph.opset1.ops import sinh
from ngraph.opset1.ops import softmax
from ngraph.opset4.ops import softplus
from ngraph.opset2.ops import space_to_batch
from ngraph.opset1.ops import space_to_depth
from ngraph.opset1.ops import split
from ngraph.opset1.ops import sqrt
from ngraph.opset1.ops import squared_difference
from ngraph.opset1.ops import squeeze
from ngraph.opset1.ops import strided_slice
from ngraph.opset1.ops import subtract
from ngraph.opset4.ops import swish
from ngraph.opset1.ops import tan
from ngraph.opset1.ops import tanh
from ngraph.opset1.ops import tensor_iterator
from ngraph.opset1.ops import tile
from ngraph.opset3.ops import topk
from ngraph.opset1.ops import transpose
from ngraph.opset1.ops import unsqueeze
from ngraph.opset1.ops import variadic_split