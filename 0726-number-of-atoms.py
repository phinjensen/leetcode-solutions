# Whew
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [collections.Counter()]
        element = None
        count = 1
        i = 0
        while i < len(formula):
            char = formula[i]
            if char.isupper():
                start = i
                end = i + 1
                while end < len(formula) and formula[end].islower():
                    end += 1
                element = formula[start:end]
                stack[-1][element] += 1
                i = end
                continue
            elif char.isnumeric():
                start = i
                end = i + 1
                while end < len(formula) and formula[end].isnumeric():
                    end += 1
                count = int(formula[start:end])
                if element:
                    stack[-1][element] += count - 1
                else:
                    atoms = stack.pop()
                    #print(atoms)
                    stack[-1] += Counter({key: count * val for key, val in atoms.items()})
                i = end
                continue
            elif char == '(':
                element = None
                stack.append(collections.Counter())
            elif char == ')':
                element = None
                if i + 1 >= len(formula) or not formula[i+1].isnumeric():
                    atoms = stack.pop()
                    stack[-1] += atoms
            i += 1
        result = []
        for k in sorted(stack[-1]):
            result.append(k)
            count = stack[-1][k]
            if count > 1:
                result.append(str(count))
        return "".join(result)
