/**
 * contains instructions for retrieving cart contents from local storage
 */

$(document).ready( () => {
    const previous_cart_counter = localStorage.getItem('previous_cart_counter');
    $('.counter').text(parseInt(previous_cart_counter));
});