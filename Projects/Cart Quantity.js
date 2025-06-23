let cartQuantity = 0;

function showCartQuantity() {
    console.log("Cart Quantity:", cartQuantity);
}

function addToCart() {
    cartQuantity++;
    console.log("Added to cart. Cart Quantity:", cartQuantity);
}

function updateCartQuantity(amount) {
    cartQuantity += amount;
    console.log("Updated cart quantity. Cart Quantity:", cartQuantity);
}

function resetCartQuantity() {
    cartQuantity = 0;
    console.log("Cart quantity reset. Cart Quantity:", cartQuantity);
}
