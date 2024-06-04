# 朴素算法
def naive_search(source, pattern):
    # 记录匹配的位置
    positions = []
    # 遍历源字符串，从每一个字符开始检查是否匹配模式字符串
    for i in range(len(source) - len(pattern) + 1):
        # 如果当前子串等于模式字符串，则记录当前位置
        if source[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions



# KMP算法
def compute_lps(pattern):
    # 生成部分匹配表（LPS数组）
    lps = [0] * len(pattern)
    length = 0  # 长度
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(source, pattern):
    lps = compute_lps(pattern)
    positions = []
    i = j = 0  # i是source的索引，j是pattern的索引
    while i < len(source):
        if pattern[j] == source[i]:
            i += 1
            j += 1
        if j == len(pattern):
            positions.append(i - j)
            j = lps[j - 1]
        elif i < len(source) and pattern[j] != source[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions



# BM算法
def preprocess_bad_character(pattern):
    # 生成坏字符表
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char

def bm_search(source, pattern):
    m = len(pattern)
    n = len(source)
    bad_char = preprocess_bad_character(pattern)
    positions = []
    s = 0  # s是源字符串的起始位置
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == source[s + j]:
            j -= 1
        if j < 0:
            positions.append(s)
            s += (m - bad_char[ord(source[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(source[s + j])])
    return positions



def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

source = read_file('source.txt')
pattern = read_file('pattern.txt')

naive_positions = naive_search(source, pattern)
kmp_positions = kmp_search(source, pattern)
bm_positions = bm_search(source, pattern)

print("Naive Search Positions:", naive_positions)
print("KMP Search Positions:", kmp_positions)
print("BM Search Positions:", bm_positions)
