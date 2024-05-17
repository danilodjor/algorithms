def longestPalindrome(s: str) -> str:
    """Finds and prints the longest palindromic substring of string s.

    Args:
        s (str): Input string that is searched for palindromes.

    Returns:
        str: Longest found palindrome in s.
    """
    
    maxLen = 0
    maxStr = ''

    for i in range(len(s)):
        # odd substrings
        l,r = i,i
        if 2*(len(s) - l) < maxLen:
            break
            
        while l>=0 and r<len(s) and s[l] == s[r]:
            if r-l+1 > maxLen:
                maxLen = r-l+1
                maxStr = s[l:r+1]
            l -= 1
            r += 1

        # even substrings
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l] == s[r]:
            if r - l + 1 > maxLen:
                maxLen = r-l+1
                maxStr = s[l:r+1]
            l -= 1
            r += 1

    return maxStr


def main():
    s = 'asdnkasndasaaaaaaaajsiwoaoas'
    ans = longestPalindrome(s)
    print(ans)


if __name__ == '__main__':
     main()