# -*- coding: utf-8 -*-
"""
Created on Mon May 19 12:09:25 2025

@author: undefined_qi

"""

import nltk
from nltk.corpus import words

# 下载词库（只需首次运行）


# 获取指定长度的英文单词
def get_words_by_length(length):
    word_list = words.words()
    filtered = [word.lower() for word in word_list if len(word) == length and word.isalpha()]
    return filtered

# 过滤灰色字母（不允许出现的字母）
def filter_by_absent_letters(filtered, absent_string):
    absent_string = absent_string.strip().lower()
    if not absent_string:
        return filtered
    absent_set = set(absent_string)
    return [word for word in filtered if not any(letter in word for letter in absent_set)]

# 过滤黄色字母（必须出现但位置未知）
def filter_by_present_letters(word_list, present_string):
    present_string = present_string.strip().lower()
    if not present_string:
        return word_list
    present_set = set(present_string)
    return [word for word in word_list if all(letter in word for letter in present_set)]

# 过滤绿色字母（必须出现在指定位置）
def filter_by_known_positions(word_list, known_list):
    """
    保留在指定位置拥有指定字母的单词。
    输入形式为 ["4e", "1s"] 表示：
    第4个字母是 e，第1个字母是 s（人类习惯从1数）
    """
    if not known_list:
        return word_list
    known_positions = {}
    for item in known_list:
        if len(item) < 2:
            continue
        try:
            pos = int(item[:-1]) - 1  # 修正这里！
            if pos < 0:
                continue
            letter = item[-1].lower()
            known_positions[pos] = letter
        except ValueError:
            continue
    result = []
    for word in word_list:
        match = True
        for pos, letter in known_positions.items():
            if pos >= len(word) or word[pos] != letter:
                match = False
                break
        if match:
            result.append(word)
    return result


# 交互式使用
def interactive_wordle_solver():
    # 第一次输入：字母长度
    while True:
        first_input = input("请输入目标单词长度（如6），或输入 q 退出：").strip()
        if first_input.lower() == "q":
            return
        try:
            length = int(first_input)
            break
        except ValueError:
            print("❌ 请输入有效的整数，例如 6")

    current_words = get_words_by_length(length)
    print(f"✅ 共找到 {len(current_words)} 个 {length} 字母的候选词")
    print(current_words[:20])
    print("之后将每轮依次输入：灰字母 → 黄字母 → 绿字母。输入回车跳过该轮类型。输入 q 可随时退出。")

    absent_letters = ""
    present_letters = ""
    known_list = []

    while True:
        print("\n--- 新一轮线索输入 ---")

        # 输入灰色字母
        absent_input = input("❌ 请输入灰色字母（不可出现的），或回车跳过：").strip().lower()
        if absent_input == "q":
            break
        absent_letters += absent_input

        # 输入黄色字母
        present_input = input("🟡 请输入黄色字母（存在但未知位置），或回车跳过：").strip().lower()
        if present_input == "q":
            break
        present_letters += present_input

        # 输入绿色位置字母提示
        known_input = input("🟩 请输入绿色位置提示（如 4e,1s）注意从1开始数，或回车跳过：").strip().lower()
        if known_input == "q":
            break
        if known_input:
            items = [x.strip() for x in known_input.split(",") if len(x.strip()) >= 2]
            known_list.extend(items)

        # 每轮重新过滤
        words0 = filter_by_absent_letters(current_words, absent_letters)
        words1 = filter_by_present_letters(words0, present_letters)
        words2 = filter_by_known_positions(words1, known_list)
        current_words = words2

        print(f"\n🎯 当前剩余 {len(current_words)} 个候选词：")
        print(current_words[:20])
        print("继续输入下一轮线索，或输入 q 退出\n")



# 启动主程序
if __name__ == "__main__":
    interactive_wordle_solver()
