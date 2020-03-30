/** 
 * contains instructions for removing items from the menu
 */

$(document).ready( () => {
    $(".remove_btn").on('click', () => {
        // get the item info
        var inputs = $(event.target).parent().parent().children().children("input");
        var remove_name = $(inputs).filter('.type').val();
        var remove_topping = $(inputs).filter('.toppings').val();
        var remove_price = $(inputs).filter('.price').val();
        var remove_category = $(inputs).filter('.category').val();
        
        // make an ajax request to the server with the item info
        $.ajax({
            url: "removeMenuItem",
            method: "POST",
            data: {
                "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
                "remove_name": remove_name,
                "remove_toppings": remove_topping,
                "remove_price": remove_price,
                "remove_category": remove_category
            },

            // on success, refresh the page so that the item is removed
            success: () => {
                window.location.reload();
            }
        })
    })
});