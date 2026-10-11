class Solution {
    List<List<Integer>> output = new ArrayList<>();

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        if (nums.length == 0)
            return output;
        Arrays.sort(nums);
        findConbinationsSum(nums, new ArrayList<>(), 0);
        return output;
    }

    public void findConbinationsSum(int[] nums, List<Integer> tmp, int index) {
        if (index == nums.length) {
            output.add(new ArrayList<>(tmp));
            return;
        }

        tmp.add(nums[index]);
        findConbinationsSum(nums, tmp, index + 1);
        tmp.remove(tmp.size() - 1);

        while (index < nums.length - 1 && nums[index] == nums[index + 1]) {
            index++;
        }
        findConbinationsSum(nums, tmp, index + 1);
    }
}