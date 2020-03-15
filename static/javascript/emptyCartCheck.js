/**
 * contains checkers for empty cart contents
 */

function CheckEmptyCart(){
    console.log($('.menuItemsTable').children());
    // if cart contents are empty, display an error
    if ($('#menuItemsTable').children().length == 0){
        console.log('carts empty');
        // TODO display an error
        $('.error').text('Please add an item to the cart')

    }
    // otherwise, open a request to the /checkout route
    else {
        window.location.href = "/checkout";
    }
}