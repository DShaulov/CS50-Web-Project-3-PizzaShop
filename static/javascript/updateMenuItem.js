/**
 * contains instructions for updating existing menu items
 */

$(document).ready( () => {
    // add an event listener to the input boxes, in order to store 
    $('.update_btn').on('click', () => {
        // getting the item info
        var inputs = $(event.target).parent().parent().children().children("input");
        var update_name = $(inputs).filter('.type').val();
        var update_topping = $(inputs).filter('.toppings').val();
        var update_price = $(inputs).filter('.price').val();
        var update_category = $(inputs).filter('.category').val();

        $(event.target).filter('.type').prev
        // send POST request to server to delete the edited item
        $.ajax({
            url: "removeMenuItem",
            method: "POST",
            data: {
                "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
                "remove_id": $(inputs).filter('.id').val(),
                "remove_category": $(inputs).filter('.category').val()
            },

            // once the old item has been deleted, create the new item
            success: () => {
                console.log('old itemd deleted')
                $.ajax({
                    url: "addNewItem",
                    method: "POST",
                    data: {
                        "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
                        "new_item_name": update_name,
                        "new_item_toppings": update_topping,
                        "new_item_price": update_price,
                        "new_item_category": update_category
                    },
        
                    // on success, reload the page
                    success: () => {
                        window.location.reload();
                    }
                })
            }
        })
    });
});