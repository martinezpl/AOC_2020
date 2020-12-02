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
    atLeast = int(nums[:nums.find('-')])
    atMost = int(nums[nums.find('-') + 1:])
    
    i = 0
    for letter in entry:
        if letter == keyLetter:
            i += 1

    if i >= atLeast and i <= atMost:
        howManyCorrectPasswords += 1

print(howManyCorrectPasswords)


