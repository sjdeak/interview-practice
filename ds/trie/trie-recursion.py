def buildTrie(words):
  t = Trie()
  for w in words:
    t.insert(w)
  return t


class Trie:

  def __init__(self):
    self.isWordEnd = False
    self.children = {}

  def insert(self, word: str) -> None:
    if not word:
      self.isWordEnd = True
      return
    firstCh = word[0]
    if firstCh not in self.children:
      self.children[firstCh] = Trie()
    self.children[firstCh].insert(word[1:])

  def search(self, word: str) -> bool:
    if not word:
      return self.isWordEnd
    if word[0] not in self.children:
      return False
    return self.children[word[0]].search(word[1:])

  def startsWith(self, prefix: str) -> bool:
    if not prefix: return True
    if prefix[0] in self.children:
      return self.children[prefix[0]].startsWith(prefix[1:])
    else:
      return False
