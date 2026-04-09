class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        unique_char_list = set(list(ransomNote))
        num_char_dict = { char: ransomNote.count(char) for char in unique_char_list }
        
        for char in unique_char_list:
            if num_char_dict[char] > magazine.count(char):
                return False

        return True
        