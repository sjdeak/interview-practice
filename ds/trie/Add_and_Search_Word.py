import os


# 在Trie的基础搜索上增加单字符通配符支持
class WordDictionary:

  def __init__(self):
    self.isWordEnd = False
    self.children = {}

  def addWord(self, word: str) -> None:
    if not word:
      self.isWordEnd = True
      return
    firstCh = word[0]
    if firstCh not in self.children:
      self.children[firstCh] = WordDictionary()
    self.children[firstCh].addWord(word[1:])

  def search(self, word: str) -> bool:
    if not word:
      return self.isWordEnd
    if word[0] == '.':
      return any([child.search(word[1:]) for child in self.children.values()])
    if word[0] not in self.children:
      return False
    return self.children[word[0]].search(word[1:])

  def startsWith(self, prefix: str) -> bool:
    if not prefix: return True
    if prefix[0] in self.children:
      return self.children[prefix[0]].startsWith(prefix[1:])
    else:
      return False


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  wd = WordDictionary()
  print('wd.addWord("bad"):', wd.addWord("bad"))
  print('wd.addWord("dad"):', wd.addWord("dad"))
  print('wd.addWord("mad"):', wd.addWord("mad"))
  print('wd.search("pad"):', wd.search("pad"))
  print('wd.search("bad"):', wd.search("bad"))
  print('wd.search(".ad"):', wd.search(".ad"))
  print('wd.search("b.."):', wd.search("b.."))
