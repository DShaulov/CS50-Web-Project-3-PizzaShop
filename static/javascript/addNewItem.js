/**
 * contains instructions for adding new items to the menu
 */

$(document).ready( () => {
    // add an event listener for clicking the create buttons
    $('.addNewItem').on('click', (element) => {
        // get the input values
        var inputs = $(element.target).parent().siblings().children();
        var empty_input = false;
        $(inputs).each( (index) => {
            // check that inputs arent empty
            if ($(inputs[index]).val() == "") {
                $(inputs[index]).attr('placeholder', 'Field cannot be empty');
                empty_input = true;
                // exit the loop
                return false;
            }
        });

        // if there was an empty input, dont send the request
        if (empty_input == true){
            return false;
        }

        // check that price is exactly 2 digits past decimal point
        var price = $(inputs).filter('.new_item_price').val();
        
        // check that there is a price
        if (price != undefined){
            var price_text = price.toString();
            var decimal_index = price_text.indexOf('.');
            console.log(price_text.length - decimal_index);
            // check that the length of the 
            if (price_text.length - decimal_index != 3) {
                $(inputs).filter('.new_item_price').val('');
                $(inputs).filter('.new_item_price').attr('placeholder', 'invalid price');
                return false;
        }
        }
        

        // send the new menu item to the server
        $.ajax({
            url: "addNewItem",
            method: 'POST',
            // add the input data the post request
            data: {
                "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
                "new_item_name": $(inputs).filter('.new_item_type').val(),
                "new_item_toppings": $(inputs).filter('.new_item_toppings').val(),
                "new_item_price": $(inputs).filter('.new_item_price').val(),
                // send along the type of dish
                "new_item_category": $(inputs).filter('.new_item_category').val()
            },
            // upon success, empty the input fields
            success: () => {
                $(inputs).filter('.new_item_type').val(''),
                $(inputs).filter('.new_item_toppings').val(''),
                $(inputs).filter('.new_item_price').val('')

                // refresh page upon success, so that new items are visible
                window.location.reload();
                // TODO add a success message?
            }
        });
    });
});