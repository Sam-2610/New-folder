/* At a restaurant, you order 1 coffee ($5) and 1 bagel ($3). Using math,
calculate the total cost, and using concatenation, create the text:
'Total cost: $_' (replace _ with the total you calculated). */

let coffee = 5;
let bagel = 3;
let total = coffee + bagel;
let message = 'Total cost: $' + total;
console.log(message); // Output: Total cost: $8