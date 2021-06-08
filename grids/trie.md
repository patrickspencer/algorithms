# Trie

Implemention of a trie in python

credit:
[this leetcode solution](https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58989/My-python-solution)

```python
class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.word=False
            self.children={}
    
    class Trie:
    
        def __init__(self):
            self.root = TrieNode()
    
        def insert(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    node.children[i]=TrieNode()
                node=node.children[i]
            node.word=True
    
        def search(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    return False
                node=node.children[i]
            return node.word
    
        def startsWith(self, prefix):
            node=self.root
            for i in prefix:
                if i not in node.children:
                    return False
                node=node.children[i]
            return True
```

often times you only need the insert function

```python
class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.word=False
            self.children={}
    
    class Trie:
    
        def __init__(self):
            self.root = TrieNode()
    
        def insert(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    node.children[i]=TrieNode()
                node=node.children[i]
            node.word=True
```

A faster implementation:

```python
trie = {}

def add(word):
    node = trie
    for w in word:
        if not w in node:
            node[w] = {}
        node = node[w]
    node['$'] = True

for word in words:
    add(word)
```

## Test input

```python
words = ['apple', 'app', 'bed', 'bid', 'bud']

from pprint import PrettyPrinter
pp = PrettyPrinter()
pp.pprint(trie)
```

output:

```python
{'a': {'p': {'p': {'$': True, 'l': {'e': {'$': True}}}}},
 'b': {'e': {'d': {'$': True}},
       'i': {'d': {'$': True}},
       'u': {'d': {'$': True}}}}
```

## Problems that use this:

[https://leetcode.com/problems/word-search-ii/](https://leetcode.com/problems/word-search-ii/)

[https://leetcode.com/problems/stream-of-characters/](https://leetcode.com/problems/stream-of-characters/)

[https://leetcode.com/problems/stream-of-characters/](https://leetcode.com/problems/stream-of-characters/)

[https://leetcode.com/problems/design-add-and-search-words-data-structure/](https://leetcode.com/problems/stream-of-characters/)