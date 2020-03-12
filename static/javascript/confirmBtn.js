/**
 * contains event listeners for confirm buttons in the slide div
 */

 $(document).ready( () => {
     $('.confirmBtn').on('click', event => {
         // on click, get the containing slide row, and the row above
         const slide_row = $(event.target).parent().parent().parent();
         const table_row = $(event.target).parent().parent().parent().prev();

         // get the title of the dish
        const dish_title =  $(slide_row).parent().parent().prev().text();

         // extract the number of toppings and which toppings from the toppings selection
        const topping_inputs = $(slide_row).children().children().children().children('button').children();
        const selected_topping_array = [];
        $(topping_inputs).each( i => {
            if ($(topping_inputs[i]).attr('checked') != undefined) {
                // if the topping is checked, get its name and put it into an array
                selected_topping_array.push($(topping_inputs[i]).attr('value'));
            }
        });

        //  get the type of dish (name/topping num)
        const dish_type = $(table_row).children('td[data-type]').text();

        //  extract the inner text of the textarea
        const textarea = $(slide_row).children().children().children('textarea');
        const textarea_text = $(textarea).val();

        //  extract the size of the dish
        const dish_size = $(table_row).children('td[data-size]').text();

        //  extract the price of the dish
        const dish_price = $(table_row).children('td[data-price]').text();

        // get the the hook to the checkout cart
        const checkout_cart_table = $('#menuItemsTable');
        
        // create a new row
        const new_row = $('<tr></tr>');

        // add to row title, size, price, type
        $('<td></td>', {
            "class": "formLabel",
            "text": dish_title
        }).appendTo(new_row);

        $('<td></td>', {
            "class": "formLabel",
            "text": dish_type
        }).appendTo(new_row);

        $('<td></td>', {
            "class": "formLabel",
            "text": dish_size
        }).appendTo(new_row);

        $('<td></td>', {
            "class": "formLabel",
            "text": dish_price
        }).appendTo(new_row);

        // adding a minus button to the cart
        const minus_btn = createImg();
        const new_td = $('<td></td>', {
            "class": "formLabel"
        });
        $('<img>', {
            "src": minus_btn.src,
            "class": "minusImg",
            // add event listener to image, onclick remove row, and delete item from database
            "click": () => {
                // TODO open a new ajax request to delete item from database
                $.ajax({
                    url: "deleteOrder",
                    method: "POST",
                    data: {
                        "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
                        "dish_title": dish_title,
                        "dish_price": dish_price,
                        "dish_size": dish_size,
                        "dish_type": dish_type,
                        "selected_topping_array": selected_topping_array,
                        "textarea_text": textarea_text
                    }
                });

                // on minus click, remove row
                new_row.remove();
            }
        }).appendTo(new_td);


        $(new_td).appendTo(new_row);

        // add new row to the table
        checkout_cart_table.append(new_row);


        //  open a new request to post the cart data to the database
        $.ajax({
            url: "logOrder",
            method: "POST",
            success: () => {
            },
            data: {
                "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
                "dish_title": dish_title,
                "dish_price": dish_price,
                "dish_size": dish_size,
                "dish_type": dish_type,
                "selected_topping_array": selected_topping_array,
                "textarea_text": textarea_text
            }
        });


     });
 });

