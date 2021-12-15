const fs = require('fs');

// len sort function
let sortFuncLen = arr => arr.sort((a, b) => a.length - b.length);
// character sort
let sortFunc = arr => arr.sort((a, b) => a > b);

function determineNums(patterns) {
    let nums = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    // translation of random pattern to normal display chars used (to be used later)
    let display = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''}
    patterns = sortFuncLen(patterns); // sort for simplier algo

    nums[1] = patterns[0].split('');
    nums[4] = patterns[2].split('');
    nums[7] = patterns[1].split('');
    nums[8] = patterns[9].split('');

    patterns.forEach(pattern => {
        if(nums[4].filter(x => pattern.includes(x)).length == 3 &&
           nums[1].filter(x => pattern.includes(x)).length == 2) {
            // determine 3 and 0
            if(pattern.length == 5) nums[3] = pattern.split('');
            else if(pattern.length == 6) nums[0] = pattern.split('');
        } else if(pattern.length == 5) {
            // 5 and 2
            if(nums[4].filter(x => pattern.includes(x)).length == 3)
                nums[5] = pattern.split('');
            else
                nums[2] = pattern.split('');
        } else if(pattern.length == 6) {
            // 6 and 9
            if(nums[4].filter(x => pattern.includes(x)).length == 4)
                nums[9] = pattern.split('');
            else
                nums[6] = pattern.split('');
        }
    })

    return nums
}

fs.readFile('data.txt', (err, data) => {
    if (err) throw err

    let lines = data.toString().split('\n');
    let totalOutput = 0;

    lines.forEach(line => {
        let lineDigitCount = 0;
        let decoded = ''; // decoded numbers

        if(line.length > 0) {
            let [patterns, output] = line.split('|');
            patterns = patterns.split(' ').filter(x => x.length > 0);
            output = output.split(' ').filter(x => x.length > 0);

            let nums = determineNums(patterns);

            // sort each and join for easier comparing against output
            Object.keys(nums).forEach(n => nums[n] = sortFunc(nums[n]).join(''));
            output = output.map(o => sortFunc(o.split('')).join(''));

            output.forEach(o => {
                for(n in nums) {
                    if(nums[n] == o) decoded += n;
                }
            })

            totalOutput += parseInt(decoded);
        }
    })


    console.log(totalOutput);
})
