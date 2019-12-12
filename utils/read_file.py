import json


def read_small_json(data_path):
    """
    read json like this
    ["第一篇文章的正文", "第二篇文章的正文", "第三篇文章的正文"]
    """
    with open(data_path, "r", encoding="utf8") as f:
        print("reading lines")
        lines = json.load(f)
        lines = [
            line.replace("\n", " [SEP] ") for line in lines
        ]  # 用[SEP]表示换行, 段落之间使用SEP表示段落结束
        print("finsh load raw data")
        return lines


def read_news_json(data_path):
    """
    read json like this
    {"news_id": "411086456", 
    "keywords": "英国石油公司发现巨型油田 股价飙升3倍！", 
    "desc": "英国石油天然气投资公司(UKOG)9日说，英格兰南部地底***", 
    "title": "英国石油公司发现巨型油田 股价飙升3倍！", 
    "source": "移动中金在线", 
    "time": "04-10 15:15", 
    "content": "英国石油天然气投资公司(UKOG)9日说，英格兰南部地底探测到规模巨大的油田，石油储量***"}
    """
    lines = []
    with open(data_path, "r", encoding="utf8") as fp:
        line = fp.readline()
        while line:
            item = json.loads(line)
            lines.append(item["content"].replace("\n", " [SEP] "))
            line = fp.readline()
    print("There are {} lines content.".format(len(lines)))
    return lines


def read_small_vocab(data_path):
    """
    read json like this
    ["第一篇文章的正文", "第二篇文章的正文", "第三篇文章的正文"]
    """
    with open(data_path, "r", encoding="utf8") as f:
        print("reading lines")
        lines = json.load(f)
        lines = [line for line in lines]
        print("finsh load raw data")
        return lines


def read_news_vocab(data_path, lac):
    """
    read json like this
    {"news_id": "411086456", 
    "keywords": "英国石油公司发现巨型油田 股价飙升3倍！", 
    "desc": "英国石油天然气投资公司(UKOG)9日说，英格兰南部地底***", 
    "title": "英国石油公司发现巨型油田 股价飙升3倍！", 
    "source": "移动中金在线", 
    "time": "04-10 15:15", 
    "content": "英国石油天然气投资公司(UKOG)9日说，英格兰南部地底探测到规模巨大的油田，石油储量***"}
    """
    lines = []
    with open(data_path, "r", encoding="utf8") as fp:
        line = fp.readline()
        count = 0
        while line:
            item = json.loads(line)
            cut_item = lac.cut(item["content"], text=True)
            lines.append(cut_item)
            line = fp.readline()
            if count % 10000 == 0:
                print("There are {} lines content already processed.".format(count))
            count += 1

    print("There are {} lines content.".format(len(lines)))
    return lines
