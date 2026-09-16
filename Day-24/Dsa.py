#anagrams
class Solution(object):
    def isAnagram(self, s, t):

        dit={}
        ana = True

        if len(t) != len(s):
            ana = False
        else:
            for i in range(len(s)):
                if s[i] in dit:
                    dit[s[i]] += 1

                else:
                    dit[s[i]] = 1

            for j in range(len(t)):
                if t[j] in dit:
                    dit[t[j]] -= 1

                else:
                    dit[t[j]] = -1

            for k in dit.values():
                if k != 0:
                    ana = False

        return ana