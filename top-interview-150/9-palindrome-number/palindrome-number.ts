function isPalindrome(x: number): boolean {
    if (x < 0)
        return false;

    // Method 1
    // return x == Number(String(x).split("").reverse().join(""));

    // Method 2
    // const s = String(x)
    // return s == s.split("").reverse().join("");

    // Method 3
    const s = String(x);
    const len = s.length;

    for (let i = 0; i < len / 2; i++) {

        // Comparing i th character from starting
        //  and len-i th character from end
        if (s[i] !== s[len - i - 1])
            return false;
    }
    return true;
};