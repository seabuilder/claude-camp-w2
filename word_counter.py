# word_counter.py — 护理记录词频统计器
# Week 2 练习 2：字典 / 循环 / 排序 / 忽略大小写
# 场景：统计护理交班记录或病情描述中的高频词汇

print("=== 护理记录词频统计器 ===")
print("请输入一段护理记录文字（直接按 Enter 结束输入）:")
print("-" * 40)

lines = []
while True:
    try:
        line = input()
        if line == "":
            break
        lines.append(line)
    except EOFError:
        break

text = " ".join(lines).strip()

if not text:
    print("⚠️ 未输入任何内容")
else:
    # 用字典统计词频，忽略大小写和标点
    word_count = {}
    for word in text.lower().split():
        clean = "".join(c for c in word if c.isalpha())
        if clean:
            word_count[clean] = word_count.get(clean, 0) + 1

    if not word_count:
        print("⚠️ 没有可统计的词汇")
    else:
        # 按出现次数从高到低排序
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

        total_words  = sum(word_count.values())
        unique_words = len(word_count)
        print(f"\n共 {total_words} 个词，{unique_words} 种不同词汇：")
        print("-" * 40)
        print(f"  {'词汇':<20} {'次数':>4}")
        print("-" * 40)
        for word, count in sorted_words:
            bar = "█" * count
            print(f"  {word:<20} {count:>4}  {bar}")
