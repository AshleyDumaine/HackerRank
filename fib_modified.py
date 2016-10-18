# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = map(int, raw_input().strip().split(' '))
res = [inp[0], inp[1]]
for i in range(2, inp[2]):
    res.append(res[i - 1]**2 + res[i - 2])
print(res[inp[2] - 1])
