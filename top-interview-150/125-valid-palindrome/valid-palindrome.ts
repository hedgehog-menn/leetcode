function isPalindrome(s: string): boolean {
    const str =  s.toLowerCase().replace(/[^a-z0-9]+/g, '');
    // return str == str.split('').reverse().join('');

    const len = str.length;
    for (let i = 0; i < len / 2; i++) {

        // Comparing i th character from starting
        //  and len-i th character from end
        if (str[i] !== str[len - i - 1])
            return false;
    }
    return true;
};