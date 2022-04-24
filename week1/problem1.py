string = input()

def not_matching(pattern):
    stack = []
    
    for i in range(len(pattern)):
        if pattern[i] in  "([{":
            stack.append(pattern[i])
        else:
            if len(stack) == 0:
                # first char is not opening bracket so the length of the stack is 0
                print(i+1)
                return False
            top = stack.pop()
            if (top == "(" and pattern[i] != ")") or (top == "[" and pattern[i] != "]") or (top == "{" and pattern[i] != "}"):
                print(i+1)
                return False

    if len(stack):
        print(i+1)

    return len(stack) == 0


if __name__ == "__main__":
    val = not_matching(string)
    if val:
        print('SUCCESS')
