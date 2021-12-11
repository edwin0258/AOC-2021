const fs = require('fs')


fs.readFile('sonarSweep.txt', (err, data) => {
    if (err) throw err;

    const lines = data.toString().split('\n');
    let [numGreater, prev] = [0, 0];

    lines.forEach(l => {
        numGreater += (prev < +l) ? 1 : 0;
        prev = +l;
    }) 

    console.log(numGreater - 1)
})
