class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in range(len(tokens)):
            result = 0

            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                operator = tokens[i]

                result += int(eval(operand1 + operator + operand2))
                print(operand1 + operator + operand2 + "=" + str(result))
                stack.append(str(result))
        if stack:
            return int(stack[0])
        return result