from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from typing import Iterable, List
import csv
import tqdm
from torch import Tensor
import torch
import torch.nn as nn
from torch.nn import Transformer
import math
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def generate_square_subsequent_mask(sz):
    mask = (torch.triu(torch.ones((sz, sz), device=DEVICE)) == 1).transpose(0, 1)
    mask = mask.float().masked_fill(mask == 0, float('-inf')).masked_fill(mask == 1, float(0.0))
    return mask


UNK_IDX, PAD_IDX, BOS_IDX, EOS_IDX = 0, 1, 2, 3

ys = torch.ones(1, 1).fill_(BOS_IDX).type(torch.long).to(DEVICE)
print(ys)

print(ys.size(0))
# tgt_mask = (generate_square_subsequent_mask(ys.size(0)).type(torch.bool)).to(DEVICE)

res = generate_square_subsequent_mask(ys.size(0)).type(torch.bool)
print(res)

print()

ys = torch.cat([ys, torch.ones(1, 1).type_as(torch.ones(1, 1)).fill_(3)], dim=0)
print(ys)
print(ys.size(0))
res = generate_square_subsequent_mask(ys.size(0)).type(torch.bool)
print(res)



ys = torch.cat([ys, torch.ones(1, 1).type_as(torch.ones(1, 1)).fill_(1)], dim=0)
print(ys)
print(ys.size(0))
res = generate_square_subsequent_mask(ys.size(0)).type(torch.bool)
print(res)
