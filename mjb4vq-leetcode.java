class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i=0; i<nums.length; i++){
            for(int j=1; j<nums.length; j++){
               if(j!=i){
                    int sol = nums[i] + nums[j];
                    if(sol==target){
                        int[] output = {i, j};
                        return output;
                    }
                }
            }
        }
        return null;
    }
}