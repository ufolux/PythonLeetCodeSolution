class Solution:
    def addDigit1(self, num: int) -> int:
        temp = 0
        while num >= 10:
            while num != 0:
                temp += num % 10
                num //= 10
            num = temp
            temp = 0
        return num

    def addDigit2(self, num: int) -> int:
        """
        :param num:
        :return:
        Python 中 % 代表取模，并不是求余
        eg: 1 % 9 = 1 但 -1 % 9 = 8
        这主要和语言的底层机制有关系， 其实取模和取余在目标上是一致的，但是因为语言对取余和取模上定义的不同，导致得到的结果不同。
        对于整型数a，b来说，取模运算或者求余运算的方法都是：

        求整数商： c = a/b;
        计算模或者余数： r = a - c*b
        但是求模运算和求余运算在第一步不同，取余运算在取c的值时，向0 方向舍入(fix()函数)，而取模运算在计算c的值时，向负无穷方向舍入(floor()函数)。

        例如

        计算-7 Mod 4
        那么：a = -7；b = 4；
        第一步：求整数商c，c应该是-1.75，如进行求模运算c = -2（向负无穷方向舍入），求余运算则c = -1（向0方向舍入）；
        第二步：计算模和余数的公式相同，但因c的值不同，求模时r = 1，求余时r = -3。
        归纳：

        当a和b符号一致时，求模运算和求余运算所得的c的值一致，因此结果一致。
        当符号不一致时，结果不一样。求模运算结果的符号和b一致，求余运算结果的符号和a一致。
        经过测试，在C/C++, C#, JAVA, PHP这几门主流语言中，%运算符都是做取余运算，而在python中的%是做取模运算。
        """
        num = num - 1
        return (num % 9 + 1) if num >= 0 else (num % -9 + 1)


s = Solution()
s.addDigit2(0)

