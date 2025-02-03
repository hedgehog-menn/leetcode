function removeDuplicates(nums: number[]): number {
    /*
    let i = 0;
    while (i < nums.length) {
        if (nums[i] === nums[i + 1]) {
            nums.splice(i, 1);
        } else {
            i++;
        }
    }
    */

    const noDupArr = [];
    nums.forEach(item => {
        if (!noDupArr.includes(item)) {
            noDupArr.push(item);
        }
    });
    nums.splice(0, nums.length);
    nums.push(...noDupArr);

    return nums.length;
};