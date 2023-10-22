# Should pass all tests, however please note that there is a really annoying test on leetcode that it will not pass because it runs out of time
# According to a statement that Dr. Can made in class, I believe that this is acceptable

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def makeHashmap(s, k):
            hashmap = {}
            for i in range(len(s)):
                key = s[i]
                if key in hashmap:
                    hashmap[key] += 1
                else:
                    hashmap[key] = 1
            return hashmap


        def isValid(hashmap, k):
            for key in hashmap.keys():
                if hashmap[key] < k:
                    return False
            return True


        max_len = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                hashmap = makeHashmap(s[i:j], k)
                if isValid(hashmap, k):
                    max_len = max(max_len, j - i)

        return max_len