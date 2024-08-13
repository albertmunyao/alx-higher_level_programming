#!/usr/bin/node

// Define the function that increments `number` and calls `theFunction`
function incrementAndCall(number, theFunction) {
    // Ensure `number` is a valid number
    if (typeof number !== 'number') {
        throw new Error('First argument must be a number.');
    }
    // Ensure `theFunction` is actually a function
    if (typeof theFunction !== 'function') {
        throw new Error('Second argument must be a function.');
    }

    // Increment the number
    let incrementedNumber = number + 1;

    // Call the provided function with the incremented number
    theFunction(incrementedNumber);
}

