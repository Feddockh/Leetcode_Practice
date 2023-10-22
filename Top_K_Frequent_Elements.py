class Solution:
    def topKFrequent(self, nums, k):

        # Keep a hashmap with each value and the number of it's occurances
        hashmap = {}

        # Iterate through all of the elements in the list
        for i in range(len(nums)):

            # Store the value from the num array as a key in the hashmap and increment the number of occurances
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        # Create a list sorted by frequency
        frequency = list(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        # Return k most frequent elements
        return [item[0] for item in frequency[:k]]
