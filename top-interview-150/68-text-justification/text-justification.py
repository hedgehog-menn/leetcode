class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                # Line complete
                extra_spaces = maxWidth - length
                spaces, remaining = divmod(extra_spaces, max(1, len(line) - 1)) # prevent divided by zero

                for j in range(max(1, len(line) - 1)): # max-1 for in case of only 1 word
                    line[j] += " " * spaces
                    if remaining:
                        line[j] += " "
                        remaining -= 1

                result.append("".join(line))
                line, length = [], 0

            line.append(words[i])
            length += len(words[i])
            i += 1

        # Handle the last line
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        result.append(last_line + " " * trail_space)

        return result