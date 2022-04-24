q = int(input())
queries = [input() for _ in range(q)]

stack = []
auxilary_stack = []
result = []

print()
print()
for que in queries:
    
    print(que)

    if "push" in que and len(auxilary_stack) != 0:
        x = que.split()[-1]
        y = auxilary_stack[-1]
        if y < x:
            auxilary_stack.append(x)
        else:
            auxilary_stack.append(y)
        stack.append(x)

    elif "push" in que and len(auxilary_stack) == 0:
        x = que.split()[-1]
        auxilary_stack.append(x)
        stack.append(x)


    elif "pop" in que and len(auxilary_stack) != 0:
        auxilary_stack.pop()
        stack.pop()
    elif "pop" in que and len(auxilary_stack) == 0:
        pass

    elif "max" in que and len(auxilary_stack) != 0:
        result.append(auxilary_stack[-1])
    elif "max" in que and len(auxilary_stack) == 0:
        pass

for val in result:
    print(val)
