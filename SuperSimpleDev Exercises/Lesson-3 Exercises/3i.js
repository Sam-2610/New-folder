/* Display the text from 3h in a popup. */
let coffee = 5.99;
let bagel = 2.95;
let total = (coffee + bagel) * 100; 
let message = `Total cost: $${(total / 100).toFixed(2)}`;
alert(message); 