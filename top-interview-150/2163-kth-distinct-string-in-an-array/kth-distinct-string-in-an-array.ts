function kthDistinct(arr: string[], k: number): string {
    const distinctString = arr.filter((val) => arr.indexOf(val) === arr.lastIndexOf(val));
    return distinctString[k - 1] || "";
};