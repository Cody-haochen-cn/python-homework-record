# 《红楼梦》人物出场统计，输出出场次数最多的 10 个

import jieba

def main():
    # 1. 读入《红楼梦》文本
    f = open("红楼梦.txt", "r", encoding="utf-8")
    txt = f.read()
    f.close()

    # 2. 用 jieba 分词
    words = jieba.lcut(txt)

    # 3. 用字典统计每个词出现次数
    counts = {}
    for w in words:
        # 去掉长度为 1 的词（标点、虚词之类）
        if len(w) == 1:
            continue
        counts[w] = counts.get(w, 0) + 1

    # 4. 将字典转成列表并按出现次数排序
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)

    # 5. 输出出现次数最多的前 10 个人物/词语
    print("《红楼梦》出场次数最多的 10 个人物：")
    for i in range(10):
        word, count = items[i]
        print(f"{i+1}. {word}：{count} 次")

if __name__ == "__main__":
    main()