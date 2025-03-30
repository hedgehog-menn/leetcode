function isSubsequence(s: string, t: string): boolean {
    let count = 0;
    let tDup = t;
    const sList = s.split('');
    let directRound = true;

    for (let i = 0; i < sList.length; i++) {
        if (tDup.indexOf(sList[i]) < 0) {
            return false;
        }

        if (tDup.indexOf(sList[i]) < count) {
            directRound = false;
        } else {
            count = tDup.indexOf(sList[i]);
            tDup = tDup.slice(0, count) + tDup.slice(count + 1);

            sList.shift();
            --i;
        }
    }

    count = 0;
    let tRevesed = t.split('').reverse().join('');
    const sListReversed = s.split('').reverse();
    let reversedRound = true;

    for (let i = 0; i < sListReversed.length; i++) {
        if (tRevesed.indexOf(sListReversed[i]) < count) {
            reversedRound = false;
        } else {
            count = tRevesed.indexOf(sListReversed[i]);
            tRevesed = tRevesed.slice(0, count) + tRevesed.slice(count + 1);

            sListReversed.shift();
            --i;
        }
    }

    return directRound || reversedRound;
};