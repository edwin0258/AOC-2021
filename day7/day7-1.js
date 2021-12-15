const fs = require('fs');

fs.readFile('data.txt', (err, data) => {
    if (err) throw err

    let positions = {}; // store positions in groups
    let maxPos = 0;
    let minFuel = Infinity;
    
    data.toString().split('\n')[0].split(',').map(x => +x).forEach(pos => {
        maxPos = (pos > maxPos) ? pos : maxPos; // used for for loop later
        (pos in positions) ? positions[pos] += 1 : positions[pos] = 1;
    })

    // test how much fuel all crabs need to reach each i pos 
    for(let i = 0; i <= maxPos; i++) {
        let fuelNeeded = 0;
        Object.keys(positions).forEach(pos => {
            let distBetween = (pos > i) ? (pos - i) : (i - pos);
            fuelNeeded += (distBetween * positions[pos]); // dist * all crabs at pos
        })
        // Does pos offer min fuel required or not
        if(minFuel > fuelNeeded) minFuel = fuelNeeded;
    }

    console.log(minFuel);
})
