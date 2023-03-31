# Question

Program 2: Given a text string containing characters only from lowercase alphabetic characters and a pattern string containing characters only from lowercase alphabetic characters and two other special characters '.' and '\*'.

Write a Python program for pattern matching that returns true if pattern is matched with text otherwise returns false. The matching must be exact, not partial.

Explanation of the special characters:

'.' - Matches a single character from lowercase alphabetic characters.
'' - Matches zero or more preceding character. It is guaranteed that '' will have one preceding character which can be any lowercase alphabetic character or special character '.'. But '' will never be the preceding character of ''. (That means "_" will never occur in the pattern string.)\ '.' = "a", "b", "c", ... , "z"\ a = "a", "aa", "aaa", "aaaa",... or empty string("")\ ab_ = "a", "ab", "abb", "abbb", "abbbb", ...

Example One
{
"text": "abbbc",
"pattern": "ab\*c"
}
Output:

1
Given pattern string can match: "ac", "abc", "abbc", "abbbc", "abbbbc", ...

Example Two
{
"text": "abcdefg",
"pattern": "a.c..\*gg"
}
Output:
1

Example Three
{
"text": "abc",
"pattern": ".ab\*.."
}
Output:

0
