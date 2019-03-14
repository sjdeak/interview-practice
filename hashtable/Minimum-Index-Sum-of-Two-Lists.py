from collections import defaultdict


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1Index = {name: i for i, name in enumerate(list1)}
        res = defaultdict(list)  # {index和: 餐厅名列表}
        
        for i, name in enumerate(list2):
            if name in list1Index:
                indexSum = i + list1Index[name]
                res[indexSum].append(name)
                
        return res[min(res.keys())]


if __name__ == '__main__':
    def test(s, t):
        print(s, t, Solution().findRestaurant(s, t))


    test(["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["KFC", "Shogun", "Burger King"])
    