/**
 * contains event listeners for the topping/extra checkboxes
 */

 // changes the checked state of the input checkboxes
$(document).ready( () => {
    $('input[type="checkbox"]').click( event => {
        if ($(event.target).attr('checked') == undefined) {
            // if not checked before, onclick set to checked
            $(event.target).attr('checked', true);
        }

        else {
            // if clicked before, onclick set checked to null
            $(event.target).attr('checked', null);
        }
    });
});