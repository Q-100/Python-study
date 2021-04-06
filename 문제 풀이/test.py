import re

s = "A man, a plan, a canal: Panama"
s = s.lower()
tmp = re.sub("[^a-z0-9]","",s)

