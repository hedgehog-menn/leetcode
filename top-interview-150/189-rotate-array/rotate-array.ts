/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
    if (k == 0)
        return;

    // handle k larger that nums size
    const lastK = k % nums.length;

    // const tail = nums.splice(-lastK);
    // nums.unshift(...tail);

    nums.unshift(...nums.splice(-lastK));
};