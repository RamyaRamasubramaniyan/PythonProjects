# HACKER RANK SOLUTION - MINION GAME
# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# 
# Scoring -
# A player gets +1 point for each occurrence of the substring in the string S.
# 
# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# Input Format :
# A single line of input containing the string S.
# Note: The string S will contain only uppercase letters:[A - Z] .
# 
# Constraints :
# 0 < len(s) <= 10^6
# 
# Output Format :
# Print one line: the name of the winner and their score separated by a space.
# If the game is a draw, print Draw.
# Note :
# Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.

def minion_game(string):
    # your code goes here
    vowel = 'aeiou'.upper()
    str_len = len(string)
    
    kevin = sum(str_len-i for i in range(str_len) if string[i] in vowel)
    stuart = str_len*(str_len + 1)/2 - kevin
    
    result = 'Draw' if kevin == stuart else 'Kevin %d' % kevin if kevin > stuart else 'Stuart %d' % stuart
    print(result)
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
# SAMPLE INPUT : BANANA
# SAMPLE OUTPUT : STUART 12
