const fs = require('fs');

fs.readFile('data.txt', (err, data) => {
    if (err) throw err

    let lines = data.toString().split('\n');
    let totalDigitCount = 0;

    lines.forEach(line => {
        let lineDigitCount = 0;

        if(line.length > 0) {
            let [patterns, output] = line.split('|');
            patterns = patterns.split(' ').filter(x => x.length > 0);
            output = output.split(' ').filter(x => x.length > 0);

            output.forEach(out => {
                if([2,3,4,7].includes(out.length)) {
                    lineDigitCount += 1;
                }
            })
        }

        totalDigitCount += lineDigitCount;
    })

    console.log(totalDigitCount);
})
