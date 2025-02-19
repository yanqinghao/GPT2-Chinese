import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))), "utils"
    )
)

import argparse
import thulac

from tqdm import tqdm
from keras.preprocessing.text import Tokenizer
from read_file import read_news_vocab, read_small_vocab


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--raw_data_path",
        default="../data/train.json",
        type=str,
        required=False,
        help="原始训练语料",
    )
    parser.add_argument(
        "--vocab_file",
        default="vocab_processed.txt",
        type=str,
        required=False,
        help="生成vocab链接",
    )
    parser.add_argument(
        "--vocab_size", default=50000, type=int, required=False, help="词表大小"
    )
    args = parser.parse_args()

    lac = thulac.thulac(seg_only=True)
    tokenizer = Tokenizer(num_words=args.vocab_size)
    print("args:\n" + args.__repr__())
    print("This script is extremely slow especially for large corpus. Take a break.")

    lines = read_news_vocab(args.raw_data_path, lac)

    tokenizer.fit_on_texts(lines)
    vocab = list(tokenizer.index_word.values())
    pre = ["[SEP]", "[CLS]", "[MASK]", "[PAD]", "[UNK]"]
    vocab = pre + vocab
    with open(args.vocab_file, "w") as f:
        for word in vocab[: args.vocab_size + 5]:
            f.write(word + "\n")


if __name__ == "__main__":
    main()
