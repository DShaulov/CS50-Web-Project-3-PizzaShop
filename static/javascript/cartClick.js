/**
 * contains onclick event handlers for the cart icon
 */

 $(document).ready( () => {
     // hide the button on load so
     // it wont be open when the page is loaded for the first time
    $('.cartDropMenu').hide();

    $('.shoppingCartImg').click( () => {
        $('.cartDropMenu').slideToggle(1000);
    });
 });




 