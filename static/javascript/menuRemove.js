/**
 * contains instructions for removing an item from the menu 
 */

function menuRemove(button){
    // get the info to send along with the delete request, so that the database knows which item to delete
    var dish_title = $(button).parent().parent().children('td[data-title]').text();
    var dish_type = $(button).parent().parent().children('td[data-type]').text();
    var dish_size = $(button).parent().parent().children('td[data-size]').text();
    var dish_instructions = $(button).parent().parent().children('td[data-instructions]').text();
    var dish_extra_toppings = $(button).parent().parent().children('td[data-toppings]').text();
    var dish_price = $(button).parent().parent().children('td[data-price]').text();

    $.ajax({
        url: "deleteOrder",
        method: "POST",
        data: {
            "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
            "dish_title": dish_title,
            "dish_price": dish_price,
            "dish_size": dish_size,
            "dish_type": dish_type,
            // using .split() in order to match the database search method
            "selected_topping_array": dish_extra_toppings.split(", "),
            "textarea_text": dish_instructions
        }
    });
    
    // remove the row from the table
    $(button).parent().parent().remove();

    // decrement the cart counter
    var counter = $('.counter').text();
    counter = parseInt(counter) - 1;
    $('.counter').text(counter);
};