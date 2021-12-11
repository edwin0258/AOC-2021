const fs = require('fs');

fs.readFile('data.txt', (err, data) => {
    if (err) throw err;

    let lines = data.toString().split('\n').map(x => x.split(' '));
    let [hor, vert, aim] = [0, 0, 0];

    lines.forEach(l => {
        let [dir, amount] = [l[0], parseInt(l[1])]
        let funcs = {'forward': (() => {
                                    hor += amount;
                                    vert += (aim * amount);
                                }), 
                     'down':    (() => aim += amount), 
                     'up':      (() => aim -= amount)}

        if(dir in funcs)
            funcs[dir]();
    })

    console.log(hor * vert);
})
