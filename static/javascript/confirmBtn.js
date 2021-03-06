/**
 * contains event listeners for confirm buttons in the slide div
 */

 $(document).ready( () => {
     $('.confirmBtn').on('click', event => {
         // clear out the empty cart error message
         $('.error').text("");
         //  if user is not logged in, take him to the login page
        console.log($('a[data-login]'));
        if ($('a[data-login').length != 0) {
            window.location.replace('/login');
            return;
        };

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
                // decrement cart counter
                var counter = $('.counter').text();
                counter = parseInt(counter) - 1;
                $('.counter').text(counter);

                //  open a new ajax request to delete item from database
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

        // increment cart counter
        var counter = $('.counter').text();
        counter = parseInt(counter) + 1;
        $('.counter').text(counter);

        //  if this was a special pizza, pick toppings at random!
        if (event.target.id == "specialPizzaConfirm") {
            var all_toppings = [];
            $('.toppingHook').each( function() {
                all_toppings.push($(this).text());
            });

            console.log(all_toppings);

            // pick 5 random toppings at random from the topping array
            for (let i = 0; i < 5; i++) {
                var random_num = Math.ceil(Math.random() * all_toppings.length) - 1;
                var random_topping = all_toppings[random_num];

                // if topping already in array, pick another one
                var includes = selected_topping_array.includes(random_topping);
                
                if (includes == true){
                    i = i - 1;
                    continue;
                }
                selected_topping_array.push(random_topping);
            }
        }
        
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

 
