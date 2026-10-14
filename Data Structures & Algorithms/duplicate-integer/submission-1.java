class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> uniqueValues = new HashSet<>();
        for (int i = 0; i < nums.length; i++){
            if(uniqueValues.contains(nums[i])){
                return true;
            }
            uniqueValues.add(nums[i]);
        }
        return false;
    }
}
