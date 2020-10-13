class Solution:
    """
    罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

    字符          数值
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

    通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
    给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

    示例 1:

    输入: 3
    输出: "III"
    示例 2:

    输入: 4
    输出: "IV"
    示例 3:

    输入: 9
    输出: "IX"
    示例 4:

    输入: 58
    输出: "LVIII"
    解释: L = 50, V = 5, III = 3.
    示例 5:

    输入: 1994
    输出: "MCMXCIV"
    解释: M = 1000, CM = 900, XC = 90, IV = 4.
    """
    def intToRoman(self, num: int) -> str:
        def lst_append(lst, n, s):
            for i in range(n):
                lst.append(s)
            return lst

        lst = []
        remain = num
        while remain > 0:
            print(remain)
            if remain >= 1000:
                m_num = remain // 1000
                remain = remain % 1000
                lst = lst_append(lst, m_num, 'M')
            elif remain >= 500:
                if remain // 100 == 9:
                    lst.append('CM')
                    remain = remain % 100
                else:
                    m_num = remain // 500
                    remain = remain % 500
                    lst = lst_append(lst, m_num, 'D')
            elif remain >= 100:
                m_num = remain // 100
                remain = remain % 100
                if m_num == 4:
                    lst.append('CD')
                else:
                    lst = lst_append(lst, m_num, 'C')
            elif remain >= 50:
                print(remain)
                if remain // 10 == 9:
                    lst.append('XC')
                    remain = remain % 10
                else:
                    m_num = remain // 50
                    remain = remain % 50
                    lst = lst_append(lst, m_num, 'L')
            elif remain >= 10:
                m_num = remain // 10
                remain = remain % 10
                if m_num == 4:
                    lst.append('XL')
                else:
                    lst = lst_append(lst, m_num, 'X')
            elif remain >= 5:
                if remain == 9:
                    lst.append('IX')
                    remain = remain % 1
                else:
                    m_num = remain // 5
                    remain = remain % 5
                    lst = lst_append(lst, m_num, 'V')
            elif remain >= 1:
                m_num = remain // 1
                remain = remain % 1
                if m_num == 4:
                    lst.append('IV')
                else:
                    lst = lst_append(lst, m_num, 'I')
            else:
                remain = 0
        return ''.join(lst)

    def intToRoman_2(self, num: int) -> str:
        hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                   5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key
                res += hashmap[key] * count
                num = num % key
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.intToRoman_2(40))
