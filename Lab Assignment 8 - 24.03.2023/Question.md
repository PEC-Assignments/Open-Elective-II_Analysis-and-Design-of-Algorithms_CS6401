# Question

Program 2:

## Edit Distance

Medium

41.1% Success

Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:

    Insert a character

    Delete a character

    Replace a character

## Input Format

The first argument of input contains a string, A. The second argument of input contains a string, B.

## Output Format

Return an integer, representing the minimum number of steps required.

Constraints:

1 <= length(A), length(B) <= 450

## Examples

Input 1:

    A = "abad"
    B = "abac"

Output 1:

    1

`Explanation 1: Operation 1: Replace d with c.`

Input 2:

    A = ""
    B = "Antihuman"

Output 2:

    2

`Explanation 2: => Operation 1: Replace s with t. => Operation 2: Insert i.`
