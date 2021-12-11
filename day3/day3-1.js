const fs = require('fs');

fs.readFile('data.txt', (err, data) => {
    if (err) throw err;

    let lines = data.toString().split('\n').map(x => x.split(''));
    // we are looking at columns, not rows in this challenge.
    let linesTransposed = lines[0].map((_, colIndex) => lines.map(row => row[colIndex]));
    let [gamma, epsilon] = ['', '']; 
    
    linesTransposed.forEach(col => {
        let [ones, zeros] = [0, 0];

        // count number of 1's and 0's in col
        col.forEach(x => {
            if(x == '1') ones += 1
            else if(x == '0') zeros += 1
        })
        
        // gamma = 1 if more 1's and 0 if more 0's. Epsilon is opposite.
        gamma += Number(ones > zeros);
        epsilon += Number(zeros > ones);
    })

    // log solution 
    console.log(parseInt(gamma, 2) * parseInt(epsilon, 2));
})
