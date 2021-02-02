import collections

class TrieNode:
    def __init__(self):
        self.word = False
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str) -> None:
        node = self.root
        node.count += 1
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count+=1
        node.word = True

    def search(self, word:str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startWith(self, word:str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def solution(words, queries):
    t = Trie()
    len_dict = collections.defaultdict(int)
    for word in words:
        t.insert(word)
        len_dict[len(word)] += 1
    print(len_dict)
    print(t)
    ans = []
    for q in queries:
        lq = len(q)
        cnt = q.count("?")
        print(cnt)
        if q[-1] == '?':
            print(t.find(q))
            ll = len(q)
            check = q[:ll-cnt]
            if t.startWith(check):
                print("exist")
            print(q[:ll-cnt])
    result = []

    return


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    solution(words, queries)