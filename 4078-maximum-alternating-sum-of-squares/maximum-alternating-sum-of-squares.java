class Solution {
    public long maxAlternatingSum(int[] nums) {
        //square every number (long, so it cannot overflow)
        long[] a = new long[nums.length];
        for (int i = 0; i < nums.length; i++)
            a[i] = (long) nums[i] * nums[i];

        //sort — smallest on the left, biggest on the right
        Arrays.sort(a);

        long ans = 0;
        int k = nums.length / 2;   // number of minus places

        //subtract the k smallest squares
        for (int i = 0; i < k; i++)
            ans -= a[i];

        //add all the bigger squares
        for (int i = k; i < nums.length; i++)
            ans += a[i];

        return ans;
    }
}