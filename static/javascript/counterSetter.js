/**
 * contains instructions setting the cart counter
 */

$(document).ready( () => {
    // get the number of menuItemsTable children and set the counter
    $('.counter').text($('#menuItemsTable').children().length);
});