# 17. Longest Common Prefix


def longestPrefix(strings):
    s = ""
    for i in range(0, len(min(strings, key=len))):
        char = strings[0][i]
        if all(string[i] == char for string in strings):
            s += char
        else:
            return s
