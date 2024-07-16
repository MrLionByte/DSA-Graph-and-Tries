class TrieNode:
    def _init_(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def _init_(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):
        def _delete(node, word, depth):
            if not node:
                return False
            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                return len(node.children) == 0

            char = word[depth]
            if char in node.children and _delete(node.children[char], word, depth + 1):
                del node.children[char]
                return not node.is_end_of_word and len(node.children) == 0
            return False
        
        _delete(self.root, word, 0)

trie = Trie()
trie.insert("bat")
trie.insert("ball")
trie.insert("bark")


trie.delete("ball")

print(trie.search("ball"))  

print(trie.search("bat"))