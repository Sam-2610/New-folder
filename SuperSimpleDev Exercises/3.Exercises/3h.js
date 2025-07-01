/* Do the same thing as 3g, but use a template string and interpolation. */

let coffee = 5.99;
let bagel = 2.95;
let total = (coffee + bagel) * 100; // Calculate in cents
let message = `Total cost: $${(total / 100).toFixed(2)}`;
console.log(message); // Output: Total cost: $8.94
