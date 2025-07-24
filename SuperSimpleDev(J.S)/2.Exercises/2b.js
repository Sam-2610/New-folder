/* You're at a restaurant with 2 friends (3 people in total) and make the
same order as 2a. Calculate how much each person pays. */

const soupPrice = 10;
const burgerPrice = 8;
const iceCreamPrice = 5;

const totalCost = soupPrice * 1 + burgerPrice * 3 + iceCreamPrice * 1;
const numberOfPeople = 3;
const costPerPerson = totalCost / numberOfPeople;
console.log("Each person pays: $" + costPerPerson);