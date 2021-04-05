def solution(p):
    if len(p) == 0:
        return ""

    u, v = balance(p)
    if correct(u):
        return u + solution(v)
    else:
        temp = "(" + solution(v) + ")"
        re = list(u[1:-1])
        for i in range(0, len(re)):
            if re[i] == "(":
                re[i] = ")"
            else:
                re[i] = "("
        return temp + ''.join(re)


def balance(p):
    u, v = "", ""
    n_left = 0
    n_right = 0
    is_balance = False
    for c in p:
        if is_balance is False:
            u += c
            if c == "(":
                n_left += 1
            else:
                n_right += 1
            if n_left == n_right:
                is_balance = True
        else:
            v += c

    return u, v


def correct(p):
    if p is False:
        return True
    stack = []
    for c in p:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) <= 0:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    # print(solution("(()())()"))
    # print(solution(")("))
    print(solution("()))((()"))
    print(solution(""))
