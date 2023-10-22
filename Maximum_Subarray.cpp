class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        // Keep a running total of the sum subarray and the max sum of the subarray
        int subarraySum = nums[0];
        int maxSubarraySum = nums[0];

        // Interate through each of the values in the array
        for (int i=1;i<nums.size();i++) {

            // If the sum of the subarray with the next element is greater than the next element alone, add the element to the sum, otherwise set the current subarray sum to the next element
            if (subarraySum + nums[i] > nums[i]) {
                subarraySum += nums[i];
            } else {
                subarraySum = nums[i];
            }

            // If the new subarray sum is greater than the max, then reassign the max subarray value to that of the current subarray sum
            if (maxSubarraySum < subarraySum) {
                maxSubarraySum = subarraySum;
            }
        }

        return maxSubarraySum;
    }
};