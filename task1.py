def foo(str):
    res = []
    skob = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for i in str:
        if i in skob:
            res.append(i)
        elif i != skob[res.pop()]:
            return False

    return len(res) == 0


print(foo('()'))