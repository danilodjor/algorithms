def suffix_table(s: str)-> list:
    """
    Args:
        s (str): Input string for which the suffix list is computed.

    Returns:
        list: Array of length |s| whose each position i contains the length of the longest proper prefix of s that is also its suffix.
    """

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


def kmp_match(t: str, s: str) -> list:
    """Finds the starting indices of pattern s found in text s.

    Args:
        t (str): Text that is to be searched for appearance of string s. 
        s (str): String pattern that is searched in text t.

    Returns:
        list: List of indices in text t where pattern s begins.
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


def main():
    text = "ABCABABDABCDABDABCDABD ABCDABD"
    pattern = "ABCDABD"
    ans = kmp_match(text, pattern)
    print(ans)


if __name__ == '__main__':
    main()