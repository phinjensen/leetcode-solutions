# A lot harder than it felt. The most difficult part was figuring out how to prevent the 5-letters
# from prefixing each other, like the erroneous "VL" for 45. Figuring it out with pure math was
# seemingly impossible (maybe there's a modulo or division trick, but I couldn't find it), so I
# eventually realized that if a number * 2 is in our symbols list, it's one of those and could
# be ignored.
symbols = {
    1000: "M",
    500:  "D",
    100:  "C",
    50:   "L",
    10:   "X",
    5:    "V",
    1:    "I",
}

class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        while num > 0:
            for k, i in symbols.items():
                if k * 4 <= num:
                    result.append(symbols[k])
                    result.append(symbols[k*5])
                    num -= k*4
                    break
                elif k <= num:
                    result.append(i)
                    num -= k
                    break
                elif k * 9/10 <= num and k * 2 not in symbols:
                    result.append(symbols[k // 10])
                    result.append(i)
                    num -= k * 9/10
                    break

        return "".join(result)
