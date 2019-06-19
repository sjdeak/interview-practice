class Trie:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.isWordEnd = False
    self.children = {}

  def insert(self, word: str) -> None:
    """
    Inserts a word into the trie.
    """
    if not word:
      self.isWordEnd = True
      return
    firstCh = word[0]
    if firstCh not in self.children:
      self.children[firstCh] = Trie()
    self.children[firstCh].insert(word[1:])

  def search(self, word: str) -> bool:
    """
    Returns if the word is in the trie.
    用循环来获取末尾节点
    """
    now = self
    for ch in word:
      if ch not in now.children:
        return False
      now = now.children[ch]
    return now.isWordEnd

  def startsWith(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    if not prefix: return True
    if prefix[0] in self.children:
      return self.children[prefix[0]].startsWith(prefix[1:])
    else:
      return False


if __name__ == '__main__':
  word = 'hello'
  prefix = 'hel'

  obj = Trie()
  obj.insert(word)
  print('obj.search(word):', obj.search(word))
  print('obj.search(\'wrong_word\'):', obj.search('wrong_word'))
  print('obj.startsWith(prefix):', obj.startsWith(prefix))
