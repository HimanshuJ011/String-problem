# String-problem(1)
# problem statement :-
Imagine you have a special keyboard with all keys in a single row. The layout of characters on a keyboard is denoted by a string keyboard of length 26. Initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is abs(j - i).


#Problem statement(2):-
[Problem 2] : a string that represents time in the format *hh:mm* . Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible. *Maximum time: 23:59* , *minimum time: 00:00* . You can assume that input string is always valid.

Example 1:

Input: "?4:5?"
Output: "14:59"
Example 2:

Input: "23:5?"
Output: "23:59"
Example 3:

Input: "2?:22"
Output: "23:22"
Example 4:

Input: "0?:??"
Output: "09:59"
Example 5:

Input: "??:??"
Output: "23:59"
