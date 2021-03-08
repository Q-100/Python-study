from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(list)
for str in strs:
    anagrams["".join(sorted(str))].append(str)

print(anagrams.values())

