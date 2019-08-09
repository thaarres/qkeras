# Copyright 2019 Google LLC
#
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
# ==============================================================================
"""Example the usage of activation functions in qkeras."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import keras.backend as K
from qkeras import *

def main():
  np.random.seed(42)
  a = K.constant([-3.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 3.0])
  a = K.constant([0.194336])
  print(" a =", K.eval(a).astype(np.float16))
  print("qa =", K.eval(quantized_relu(6,2)(a)).astype(np.float16))
  print("ss =", K.eval(smooth_sigmoid(a)).astype(np.float16))
  print("hs =", K.eval(hard_sigmoid(a)).astype(np.float16))
  print("ht =", K.eval(hard_tanh(a)).astype(np.float16))
  print("st =", K.eval(smooth_tanh(a)).astype(np.float16))
  c = K.constant(np.arange(-1.5, 1.51, 0.3))
  print(" c =", K.eval(c).astype(np.float16))
  print("qb_111 =", K.eval(quantized_bits(1,1,1)(c)).astype(np.float16))
  print("qb_210 =", K.eval(quantized_bits(2,1,0)(c)).astype(np.float16))
  print("qb_211 =", K.eval(quantized_bits(2,1,1)(c)).astype(np.float16))
  print("qb_300 =", K.eval(quantized_bits(3,0,0)(c)).astype(np.float16))
  print("qb_301 =", K.eval(quantized_bits(3,0,1)(c)).astype(np.float16))
  c_1000 = K.constant(np.array([list(K.eval(c))] * 1000))
  b = np.sum(K.eval(bernoulli()(c_1000)).astype(np.int32), axis=0) / 1000.0
  print("       hs =", K.eval(hard_sigmoid(c)).astype(np.float16))
  print("    b_all =", b.astype(np.float16))
  T = 0.0
  t = K.eval(stochastic_ternary(threshold=T)(c_1000)).astype(np.int32)
  for i in range(10):
    print("sternary({}) =".format(i), t[i])
  print("   st_all =", np.round(
      np.sum(t.astype(np.float32), axis=0).astype(np.float16) /
      1000.0, 2).astype(np.float16))
  print("  ternary =", K.eval(ternary(threshold=0.5)(c)).astype(np.int32))
  b = K.eval(stochastic_binary()(c_1000)).astype(np.int32)
  for i in range(5):
    print("sbinary({}) =".format(i), b[i])
  print("sbinary =", np.round(np.sum(b, axis=0) / 1000.0, 2).astype(np.float16))
  print(" binary =", K.eval(binary()(c)).astype(np.int32))
  c = K.constant(np.arange(-1.5, 1.51, 0.3))
  print(" c =", K.eval(c).astype(np.float16))
  print(" b_10 =", K.eval(binary(1)(c)).astype(np.float16))
  print("qr_10 =", K.eval(quantized_relu(1,0)(c)).astype(np.float16))
  print("qr_11 =", K.eval(quantized_relu(1,1)(c)).astype(np.float16))
  print("qr_20 =", K.eval(quantized_relu(2,0)(c)).astype(np.float16))
  print("qr_21 =", K.eval(quantized_relu(2,1)(c)).astype(np.float16))
  print("qr_101 =", K.eval(quantized_relu(1,0,1)(c)).astype(np.float16))
  print("qr_111 =", K.eval(quantized_relu(1,1,1)(c)).astype(np.float16))
  print("qr_201 =", K.eval(quantized_relu(2,0,1)(c)).astype(np.float16))
  print("qr_211 =", K.eval(quantized_relu(2,1,1)(c)).astype(np.float16))
  print("qt_200 =", K.eval(quantized_tanh(2,0)(c)).astype(np.float16))
  print("qt_210 =", K.eval(quantized_tanh(2,1)(c)).astype(np.float16))
  print("qt_201 =", K.eval(quantized_tanh(2,0,1)(c)).astype(np.float16))
  print("qt_211 =", K.eval(quantized_tanh(2,1,1)(c)).astype(np.float16))
  set_internal_sigmoid("smooth"); print("with smooth sigmoid")
  print("qr_101 =", K.eval(quantized_relu(1,0,1)(c)).astype(np.float16))
  print("qr_111 =", K.eval(quantized_relu(1,1,1)(c)).astype(np.float16))
  print("qr_201 =", K.eval(quantized_relu(2,0,1)(c)).astype(np.float16))
  print("qr_211 =", K.eval(quantized_relu(2,1,1)(c)).astype(np.float16))
  print("qt_200 =", K.eval(quantized_tanh(2,0)(c)).astype(np.float16))
  print("qt_210 =", K.eval(quantized_tanh(2,1)(c)).astype(np.float16))
  print("qt_201 =", K.eval(quantized_tanh(2,0,1)(c)).astype(np.float16))
  print("qt_211 =", K.eval(quantized_tanh(2,1,1)(c)).astype(np.float16))
  set_internal_sigmoid("real"); print("with real sigmoid")
  print("qr_101 =", K.eval(quantized_relu(1,0,1)(c)).astype(np.float16))
  print("qr_111 =", K.eval(quantized_relu(1,1,1)(c)).astype(np.float16))
  print("qr_201 =", K.eval(quantized_relu(2,0,1)(c)).astype(np.float16))
  print("qr_211 =", K.eval(quantized_relu(2,1,1)(c)).astype(np.float16))
  print("qt_200 =", K.eval(quantized_tanh(2,0)(c)).astype(np.float16))
  print("qt_210 =", K.eval(quantized_tanh(2,1)(c)).astype(np.float16))
  print("qt_201 =", K.eval(quantized_tanh(2,0,1)(c)).astype(np.float16))
  print("qt_211 =", K.eval(quantized_tanh(2,1,1)(c)).astype(np.float16))
  set_internal_sigmoid("hard")
  print(" c =", K.eval(c).astype(np.float16))
  print("q2_31 =", K.eval(quantized_po2(3,1)(c)).astype(np.float16))
  print("q2_32 =", K.eval(quantized_po2(3,2)(c)).astype(np.float16))
  print("qr2_21 =", K.eval(quantized_relu_po2(2,1)(c)).astype(np.float16))
  print("qr2_22 =", K.eval(quantized_relu_po2(2,2)(c)).astype(np.float16))
  print("qr2_44 =", K.eval(quantized_relu_po2(4,1)(c)).astype(np.float16))


if __name__ == '__main__':
  main()