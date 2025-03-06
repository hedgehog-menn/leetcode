function removeDuplicates(nums: number[]): number {
    let i = 0;
    let isDupOnce = false;
    while (i < nums.length) {
        if (nums[i] !== nums[i + 1]) {
            isDupOnce = false;
            i++;
        } else if (nums[i] === nums[i + 1] && !isDupOnce) {
            isDupOnce = true;
            i++;
        } else {
            nums.splice(i, 1);
        }
    }

    return nums.length;
};