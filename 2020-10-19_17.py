class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations

    def letterCombinations_2(self, digits: str):
        if digits == '':
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        from queue import Queue
        q = Queue()
        lst = ['']
        for i in digits:
            q.put(i)
        while not q.empty():
            new = []
            s = phoneMap[q.get()]
            for i in lst:
                for j in s:
                    new.append(i + j)
            lst = new
        return lst

    def letterCombinations_3(self, digits: str):
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if digits == '':
            return []

        def backtrack(con, nextdigit):
            if len(nextdigit) == 0:
                res.append(con)
            else:
                for i in phoneMap[nextdigit[0]]:
                    backtrack(con + i, nextdigit[1:])

        res = []
        backtrack('', digits)
        return res



if __name__ == '__main__':
    test = Solution()
    print(test.letterCombinations_3('234'))
