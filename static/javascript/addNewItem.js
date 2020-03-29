/**
 * contains instructions for adding new items to the menu
 */

$(document).ready( () => {
    // add an event listener for clicking the create buttons
    $('.addNewItem').on('click', (element) => {
        // get the input values
        var inputs = $(element.target).parent().siblings().children();
        $(inputs).each( (index) => {
            // check that inputs arent empty
            if ($(inputs[index]).val() == "") {
                $(inputs[index]).attr('placeholder', 'Field cannot be empty');
                return false;
            }

            // send the new menu item to the server
            $.ajax({
                url: "addNewItem",
                method: 'POST',
                success: ( () => {

                }),
                // add the input data the post request
                data: {
                    "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
                    
                }
            })
        });
    });
});