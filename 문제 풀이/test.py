import collections
strs = ["eat","tea","tan","ate","nat","bat"]

a = collections.defaultdict(list)

for word in strs:
    a["".join(sorted(word))].append(word)

print(a.values())
