const fs = require('fs');

fs.readFile('data.txt', (err, data) => {
    if (err) throw err

    let rulesObj = {} // object with mappings of rules
    const steps = 10; // number of insertion pair steps

    let [template, ...rules] = data.toString().split('\n');

    rules.forEach(rule => {
        let [key, val] = rule.split(' -> ');
        rulesObj[key] = val;
    })

    let finalTemplate = insertInPairs(template, rulesObj, steps);
    // [element -> num occurences obj, sorted element keys]
    let [numElems, elemKeys] = getElemOccurences(finalTemplate);

    // print solution
    console.log(numElems[elemKeys[0]] - numElems[elemKeys[elemKeys.length - 1]]);
})

function getElemOccurences(finalTemplate) {
    let counts = {};
    finalTemplate.split('').forEach(elem => {
        if(elem in counts) counts[elem] += 1;
        else counts[elem] = 1;
    })
    // sort by num occurences
    let sortedKeys = Object.keys(counts).sort((a, b) => {
        return counts[b] - counts[a];
    })

    return [counts, sortedKeys];
}

function insertInPairs(template, rules, steps) {
    for(let n = 0; n < steps; n++) {
        let pair = [];
        let templateTemp = template;
        let count = 0; // how many successful elements inserted

        template.split('').forEach((elem, i) => {
            if(pair.length == 2) 
                pair[0] = pair[1];
            pair[1] = elem;
            let mappedElem = (Object.keys(rules).indexOf(pair.join('')) != -1) ? rules[pair.join('')] : '';

            templateTemp = templateTemp.slice(0, i+count) + mappedElem + templateTemp.slice(i+count); 

            if(mappedElem != '') count += 1;
        })

        template = templateTemp;
    }
    
    return template;
}
