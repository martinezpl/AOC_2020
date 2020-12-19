def simp_calc(x, o, y):
    if o == '+':
        return x+y
    elif o == '*':
        return x*y

def eval_bracket(b_l, inc):
    val = 0
    i = 0
    op = ''
    while i < len(b_l):
        if b_l[i] == ')':
            print('bracket:', val)
            inc += 1
            return val, inc
        
        if b_l[i] == '(':
            br, inc = eval_bracket(b_l[i+1:], inc)
            if i == 0:
                val = br
            else:
                val = simp_calc(val, op, br)
            i = b_l.index(')')
            print('pre:', b_l)
            b_l.pop(b_l.index(')'))
            print('post:', b_l)
            continue

        if b_l[i] == '+' or b_l[i] == '*':
            op = b_l[i]
        elif b_l[i].isnumeric():
            if i != 0:
                val = simp_calc(val, op, int(b_l[i]))
            else:
                val = int(b_l[i])
        i += 1

solutions = []

with open('input.txt') as f:
    for line in f:
        if line != '\n':
            print(line)
            b_l = [ch for ch in line if ch != ' ']  
            val = 0
            i = 0
            op = ''
            while i < len(b_l):
                if b_l[i] == "\n":
                    break
                if b_l[i] == '(':
                    br, inc = eval_bracket(b_l[i+1:], 0)
                    if i == 0:
                        val = br
                    else:
                        val = simp_calc(val, op, br)
                    for j in range(inc):
                        i = b_l.index(')')
                        b_l.pop(b_l.index(')'))
                    continue

                if b_l[i] == '+' or b_l[i] == '*':
                    op = b_l[i]
                elif b_l[i].isnumeric():
                    if i != 0:
                        val = simp_calc(val, op, int(b_l[i]))
                    else:
                        val = int(b_l[i])
                i += 1
            print('solution:', val)
            solutions.append(val)


print(sum(solutions))
