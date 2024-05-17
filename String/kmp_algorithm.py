def suffix_table(s: str)-> list:
    """Returns an array arr of length |s| whose each position i contains the length of the longest proper prefix of s that is also its suffix."""
    arr = [0]*len(s)
    length = 0

    for i in range(1, len(s)):
        if s[i] == s[length]:
            length += 1
            arr[i] = length
        else:
            while length > 0 and s[i] != s[length]:
                length = arr[length-1]
            if s[i] == s[length]:
                length += 1
            arr[i] = length
        

    return arr

def string_match(t: str, s: str) -> list:
    """
    param: t - Text that is to be searched for appearance of string s.
    param: s - String pattern that is searched in text t.
    """

    assert len(s) <= len(t), "Input error: Pattern string must be shorter than text string."

    traceback = suffix_table(s)
    pattern_pos = []

    m = 0
    while m <= len(t) - len(s):
        i = 0
        while i < len(s) and t[m+i] == s[i]:
            i += 1
        
        if i == len(s):
            pattern_pos.append(m)
            i-=1

        m += i - traceback[i-1] if i >= 1 else 1

    return pattern_pos


ans = string_match("ABCABABDABCDABDABCDABD ABCDABD", "ABCDABD")
print(ans)