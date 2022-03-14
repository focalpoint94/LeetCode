class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        wordSet = set()
        for word in dict:
            for i, c in enumerate(word):
                neighbor = word[:i] + '#' + word[i+1:]
                if neighbor in wordSet:
                    return True
                wordSet.add(neighbor)
        return False
