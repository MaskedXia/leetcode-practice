#127.单词接龙：给定两个单词（beginWord 和 endWord）和一个字典
# ，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#每次转换只能改变一个字母。
#转换过程中的中间单词必须是字典中的单词。
from collections import defaultdict
def ladderLength(beginWord, endWord, wordList):
    if not beginWord or not endWord or not wordList or endWord not in wordList:
        return 0
    all_combo_dict = defaultdict(list)
    L = len(beginWord)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)
    queue = [(beginWord,1)]
    visited = {beginWord: True}
    while queue:
        current_word, level = queue.pop(0)
        for i in range(L):
            intermedia = current_word[:i] + '*' + current_word[i+1:]
            for word in all_combo_dict[intermedia]:
                if word == endWord:
                    return level + 1
                if word not in visited:
                    queue.append((word, level+1))
                    visited[word] = True
            all_combo_dict[intermedia] = []
    return 0

