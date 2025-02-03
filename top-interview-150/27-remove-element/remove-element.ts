function removeElement(nums: number[], val: number): number {
    // let index = nums.indexOf(val);
    // while (index > 0) {
    //     nums.splice(index, 1);
    //     // nums.push(_);
    //     index = nums.indexOf(val);
    // }
    // return nums.indexOf(_) - 1;

    let i = 0;
    while (i < nums.length) {
        if (nums[i] === val) {
            nums.splice(i, 1);
        } else {
            i++;
        }
    }
    return nums.length;
};