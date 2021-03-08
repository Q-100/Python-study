class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = [word for word in re.sub(r'[^\w]', " ", paragraph).split() if word not in banned]

        return Counter(words).most_common(1)[0][0]


