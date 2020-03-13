/**
 * contains functions that help with persisting the users cart after he closes the window
 */

$(document).ready( () => {
    $(window).on('beforeunload', () => {
        // get the cart counter
        const cart_counter = $('.counter').text();
        localStorage.setItem('previous_cart_counter', cart_counter);
    });
});