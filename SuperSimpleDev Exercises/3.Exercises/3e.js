/* Do the same thing as 3d, but use a template string and interpolation. */

let coffee = 5;
let bagel = 3;
let total = coffee + bagel;
let message = `Total cost: $${total}`;
console.log(message); // Output: Total cost: $8

alert(message); // Optional: Show the message in an alert box