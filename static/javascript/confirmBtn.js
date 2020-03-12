/**
 * contains event listeners for confirm buttons in the slide div
 */

 $(document).ready( () => {
     $('.confirmBtn').on('click', event => {
         // on click, get the containing slide row, and the row above
         const slide_row = $(event.target).parent().parent().parent();
         const table_row = $(event.target).parent().parent().parent().prev();

         // extract the number of toppings and which toppings from the toppings selection
        const topping_inputs = $(slide_row).children().children().children().children('button').children();
        const selected_topping_array = [];
        $(topping_inputs).each( i => {
            if ($(topping_inputs[i]).attr('checked') != undefined) {
                // if the topping is checked, get its name and put it into an array
                selected_topping_array.push($(topping_inputs[i]).attr('value'));
            }
        });

        //  extract the inner text of the textarea
        const textarea = $(slide_row).children().children().children('textarea');
        const textarea_text = $(textarea).val();
        console.log(textarea_text);

        // TODO extract the size of the dish
        console.log($(table_row).children().text());

        // TODO extract the price of the dish

     });
 });

