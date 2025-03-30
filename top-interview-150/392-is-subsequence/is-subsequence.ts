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
    let t_revesed = t.split('').reverse().join('');
    const sList_reversed = s.split('').reverse();
    let reversedRound = true;

    for (let i = 0; i < sList_reversed.length; i++) {
        if (t_revesed.indexOf(sList_reversed[i]) < count) {
            reversedRound = false;
        } else {
            count = t_revesed.indexOf(sList_reversed[i]);
            t_revesed = t_revesed.slice(0, count) + t_revesed.slice(count + 1);

            sList_reversed.shift();
            --i;
        }
    }

    return directRound || reversedRound;
};