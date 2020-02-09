s = 'azcbobobegghakl'
count = 0
st = 'bob'
sub_len = len(st)
for i in range(len(s)):
    if s[i:i+sub_len] == st:
        count += 1
    
print("Number of times bob occurs is: " + str(count))