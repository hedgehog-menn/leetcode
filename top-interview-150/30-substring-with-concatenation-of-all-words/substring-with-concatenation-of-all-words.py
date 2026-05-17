class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        total_length = word_length * len(words)
        res = []
        word_count = {}

        for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        
        for i in range(word_length):
            start = i
            sub_count = {}
            count = 0

            for j in range(i, len(s) - word_length + 1, word_length):
                sub_word = s[j:j + word_length]
                if sub_word in word_count:
                    sub_count[sub_word] = sub_count.get(sub_word, 0) + 1
                    count += 1

                    while sub_count[sub_word] > word_count[sub_word]:
                        sub_count[s[start:start + word_length]] -= 1
                        count -= 1
                        start += word_length
                    
                    if count == len(words):
                        res.append(start)

                else:
                    sub_count.clear()
                    count = 0
                    start = j + word_length
        return res