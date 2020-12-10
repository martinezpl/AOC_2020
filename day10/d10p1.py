inp = '''8
131
91
35
47
116
105
121
56
62
94
72
13
82
156
102
12
59
31
138
46
120
7
127
126
111
2
123
22
69
18
157
75
149
88
81
23
98
132
1
63
142
37
133
61
112
122
128
155
145
139
66
42
134
24
60
9
28
17
29
101
148
96
68
25
19
6
67
113
55
40
135
97
79
48
159
14
43
86
36
41
85
87
119
30
108
80
152
158
151
32
78
150
95
3
52
49'''

ads = [] #adapters
for a in inp.split('\n'):
    ads.append(int(a))

ads.append(max(ads) + 3)
ads.append(0)

ads.sort()

ojd = 0
tjd = 0 #one/three jolt diff
for i in range(len(ads) - 1):
    if ads[i+1] - ads[i] == 1:
        ojd += 1
    elif ads[i+1] - ads[i] == 3:
        tjd += 1

print(ojd*tjd)

