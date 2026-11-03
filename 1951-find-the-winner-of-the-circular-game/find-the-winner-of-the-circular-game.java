class Solution {
    public int Winner(int n,int k){
        if(n==1){
            return 0;
        }
        else{
            return (Winner(n-1,k)+k)%n;
        }
    }
    public int findTheWinner(int n, int k) {
        int res=Winner(n,k);
        return res+1;
    }
}