# Word Search

## Prompt

Given a 2D grid of characters and a word, find all occurrences of the given word in the grid. A word can be matched in all 8 directions at any point. Word is said to be found in a direction if all characters match in this direction (not in zig-zag form).
The 8 directions are, Horizontally Left, Horizontally Right, Vertically Up, Vertically Down and 4 Diagonal directions.

Sources:
https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/

https://leetcode.com/problems/word-search/
https://leetcode.com/problems/word-search-ii/

## Notes

This is a common interview question and a good grid question for testing algorithm fundamentals.

## Variations

Variation 1: Tell if *one* word is in the grid.

Variation 2: Tell if *multiple* words are in the grid

## Solution

### Variation 1

For variation 1, we only need to traverse a grid and run a dfs search.

We will use backtracking

If there are N elements in the grid then we need to search 3 neighboring cells. We don't check the cell we just came from. This gives us a time complexity of O(N*3^w) where w is the length of the worth we are looking for and N is the number of cells.

Space complexity is O(1) if we don't count the call stack memory.

Here we modify the grid:

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        nrows, ncols = len(board), len(board[0]) if board else 0
        
        def valid(r, c):
            return 0 <= r < nrows and 0 <= c < ncols
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                
        def dfs(r: int, c: int, ending: str) -> bool:
            if len(ending) == 0:
                return True
            
            ans = False
            
            if valid(r, c) and board[r][c] == ending[0]:
                board[r][c] = '*'
                ans = any(dfs(r+x, c+y, ending[1:]) for x, y in directions)
                board[r][c] = ending[0]
            return ans
        return any(dfs(r, c, word) for r in range(nrows) for c in range(ncols))
```

### Variation 2

Given a list of words, find how many are in the grid:

We will use a trie structure to hold the words.

Time complexity: same as variation 1 above. But w is the length of the largest word.

Space complexity: O(N) because we have to make a trie stucture.

```python
class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = collections.defaultdict(TrieNode)
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def add(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            node.char = c
        node.word = word

class Solution:
                    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        nrows, ncols = len(board), len(board[0]) if board else 0
        
        def valid(r, c):
            return 0 <= r < nrows and 0 <= c < ncols
    
        def search(r, c, trie_node):
            
            if not valid(r, c) or board[r][c] == '#' or not board[r][c] in trie_node.children:
                return
            
            ch = board[r][c]
            
            node = trie_node.children[ch]
            
            nonlocal ans
            if node.word:
                ans.append(node.word)
                node.word = None

            board[r][c] = '#'
            
            dirs = [-1, 0, 1, 0, -1]
            for i in range(4):
                nr, nc = r + dirs[i], c + dirs[i+1]
                search(nr, nc, node)
                    
            board[r][c] = ch
        
        
        trie = Trie()
        for word in words:
            trie.add(word)
        
        ans = []
        
        for r in range(nrows):
            for c in range(ncols):
                search(r, c, trie.root)
                
        return ans
    
```