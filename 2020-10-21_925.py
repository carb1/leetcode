class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pre = None
        na = 0
        ty = 0
        while na <= len(name) - 1:
            if ty >= len(typed):
                return False
            print(name[na], typed[ty])
            if name[na] != typed[ty]:
                if typed[ty] == pre:
                    ty += 1
                else:
                    return False
            else:
                pre = typed[ty]
                na += 1
                ty += 1

        if ty <= len(typed):
            print(list(typed[ty:]))
            print(len(set(list(typed[ty:]))))
            if len(set(list(typed[ty:]))) <= 1:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    test = Solution()
    print(test.isLongPressedName("pyplrz","ppyypllr"))
