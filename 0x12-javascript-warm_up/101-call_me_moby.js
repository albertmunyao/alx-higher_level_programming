#!/usr/bin/node 

// Define the function that executes `theFunction` `x` times
function executeXTimes(x, theFunction) {
    // Ensure `x` is a positive integer
    if (typeof x !== 'number' || x <= 0 || !Number.isInteger(x)) {
        throw new Error('First argument must be a positive integer.');
    }
    // Ensure `theFunction` is actually a function
    if (typeof theFunction !== 'function') {
        throw new Error('Second argument must be a function.');
    }

    // Execute `theFunction` `x` times
    for (let i = 0; i < x; i++) {
        theFunction();
    }
}

