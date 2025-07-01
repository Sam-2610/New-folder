/* Calculate the total cost of a toaster ($18.50) and 2 shirts ($7.50 each). */

const toasterPrice = 1850;
const shirtPrice = 750 * 2;
const totalCost = toasterPrice + shirtPrice;
console.log("Total Cost to be paid: $", (totalCost / 100).toFixed(2));

/* Calculate a 10% tax for the total. */
const tax = totalCost * 0.10;
console.log("Total Cost with  10% Tax: $", ((totalCost + tax) / 100).toFixed(2));

/* Calculate a 20% tax for the total. */
const addTax = totalCost * 0.20;
console.log("Total Cost with 20% Tax: $", ((totalCost + addTax) / 100).toFixed(2));