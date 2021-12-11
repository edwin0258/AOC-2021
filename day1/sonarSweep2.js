const fs = require('fs')

fs.readFile('sonarSweep.txt', (err, data) => {
    if (err) throw err;

    let [numGreater, prev, windowSize] = [0, 0, 3];

    const lines = data.toString().split('\n').map(x => parseInt(x));

    // Windowing lines
    let winLines = lines.map((x, i, arr) => {
        if(i + 2 <= arr.length)
            return arr.slice(i, i + windowSize).reduce((total, x) => total + x)
        return Infinity
    })

    winLines.forEach(l => {
        numGreater += (prev < l) ? 1 : 0;
        prev = l;
    }) 

    console.log(numGreater - 1)
})
