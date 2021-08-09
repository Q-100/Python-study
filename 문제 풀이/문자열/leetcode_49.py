from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(list)
# defaultdict : list형식으로 선언하면 value값들이 리스트로 들어가짐
for str in strs:
    anagrams["".join(sorted(str))].append(str)

print(anagrams.values())

