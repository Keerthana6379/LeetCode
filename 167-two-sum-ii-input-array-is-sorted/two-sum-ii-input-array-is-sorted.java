class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l=0;
        int r=numbers.length-1;
        int curSum;
        while(l<r){
            curSum=numbers[l]+numbers[r];
            if(curSum==target){
                return new int[]{l+1,r+1};
            }
            if(curSum<target){
                l+=1;
            }
            else{
                r-=1;
            }
        }
        return new int[]{};
    }
}