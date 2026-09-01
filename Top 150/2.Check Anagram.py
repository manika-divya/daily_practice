#2.Check Anagram

def CheckAnagram():
    s = input()
    t = input()
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

CheckAnagram()