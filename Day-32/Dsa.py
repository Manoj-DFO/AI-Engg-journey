#group anagrams
class Solution(object):
    def groupAnagrams(self, strs):

        dit = {}
        a = ''

        for i in strs:

            a = ''.join(sorted(i))

            if a in dit:
                dit[a].append(i)

            else:
                dit[a] = [i]
        
        return list(dit.values())
                
#424 longest repeating character replacement
class Solution(object):
    def characterReplacement(self, s, k):

        dit = {}
        left = 0
        max_len = 0
        ans = 0
        
        for i in range(len(s)):

            dit[s[i]] = dit.get(s[i], 0) + 1

            max_len = max(max_len, dit[s[i]])

            while (i - left + 1) - max_len > k:
                dit[s[left]] -= 1 
                left += 1

            ans = max(ans, i - left + 1) 

        return ans 