s = 'azcbobobegghaklbobbob'
count = 0
verb = 'bob'
verb_l = len(verb)
for i in range(len(s)):
    if s[i:i+verb_l] == verb:
        count += 1
print("NUmber of times bob occurs is: " +str(count))