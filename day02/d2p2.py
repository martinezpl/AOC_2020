data = {}
passwords = []
with open('input.txt', 'r') as f:
    for line in f:
        if line != '\n':
            policy = line[:line.find(':')]
            password = line[line.find(':') + 2:]
            password = password.strip()
            # if dict key already exists, add : at the beginning
            if data.get(password) is not None:
                password = ":" + password
            passwords.append(password)
            data[password] = policy

howManyCorrectPasswords = 0

for entry in passwords:
    if ':' in entry:
        entry = entry[1:]

    policy = data[entry]
    keyLetter = policy[len(policy) - 1]
    nums = policy[:len(policy) - 1]
    pos1 = int(nums[:nums.find('-')])
    pos2 = int(nums[nums.find('-') + 1:])
    
    i = 0

    if entry[pos1 - 1] == keyLetter:
        i += 1
    if entry[pos2 - 1] == keyLetter:
        i += 1

    if i == 1:
        howManyCorrectPasswords += 1

print(howManyCorrectPasswords)

