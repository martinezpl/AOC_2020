def simp_calc(x, o, y):
    if o == '+':
        return x+y
    elif o == '*':
        return x*y

def eval_bracket(b_l):
    val = 0
    i = 0
    op = ''
    while i < len(b_l):
        if b_l[i] == ')':
            return val
        
        if b_l[i] == '(':
            br = eval_bracket(b_l[i+1:])
            if i == 0:
                val = br
            else:
                val = simp_calc(val, op, br)
            i = b_l.index(')') + 1
        
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
            b_l = [ch for ch in line if ch != ' ']  
            val = 0
            i = 0
            op = ''
            while i < len(b_l):
                print(val, i)
                if b_l[i] == "\n":
                    break
                if b_l[i] == '(':
                    br = eval_bracket(b_l[i+1:])
                    if i == 0:
                        val = br
                    else:
                        val = simp_calc(val, op, br)
                    i = b_l.index(')') + 1

                if b_l[i] == '+' or b_l[i] == '*':
                    op = b_l[i]
                elif b_l[i].isnumeric():
                    if i != 0:
                        val = simp_calc(val, op, int(b_l[i]))
                    else:
                        val = int(b_l[i])
                i += 1
            solutions.append(val)


print(sum(solutions))
