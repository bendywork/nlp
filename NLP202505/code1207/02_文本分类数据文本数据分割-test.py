# -*- coding: utf-8 -*-
"""
Create Date Time : 2025/12/7 10:38
Create User : 19410
Desc : jieba分词内部主要基于词典匹配实现，首先获取所有可能的分词方式，然后在所有分词方式选择最有可能的分词结果
"""
import os
from pathlib import Path
import jieba

BASE_DIR = os.path.dirname(__file__)
jieba.load_userdict(os.path.join(BASE_DIR, "text_classify.dict"))
print(os.path.join(os.path.dirname(__file__)))

def split_text(text):
    return jieba.lcut(text) # 分词
    # return list(text)  # 分字 -- 直接将字作为词存在

def read_file_and_write_tokens(in_file, out_file):
    os.makedirs(os.path.dirname(out_file), exist_ok=True)

    with open(in_file, "r", encoding="utf-8") as reader:
        with open(out_file, "w", encoding="utf-8") as writer:
            for line in reader:
                text, label = line.strip().split("\t")
                tokens = split_text(text)
                writer.writelines(f"{' '.join(tokens)}\t{label}\n")
if __name__ == '__main__':
    read_file_and_write_tokens(
        in_file=os.path.join(BASE_DIR,"../datas/text_classify/train.csv"),
        out_file=os.path.join(BASE_DIR, "../datas/text_classify/train_tokens.csv")
    )
