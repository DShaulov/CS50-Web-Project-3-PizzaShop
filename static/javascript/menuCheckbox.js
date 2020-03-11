/**
 * contains event listeners for the topping/extra checkboxes
 */

// if topping button is clicked, its equal to clicking its checkbox
$(document).ready( () => {
    $('.toppingBtn').on('click', event => {
        var inputChildren = $(event.target).children();
        // if trying to deselect, allow to click regardless of max toppings exceeded
        var myInput = $(inputChildren[0]);
        if ($(myInput[0]).attr('checked') == 'checked') {
            $(inputChildren[0]).click();
            return;
        }
        
        // check to see what the max toppings allowed are:
        var max_toppings = $(event.target).children().attr('data-toppingNum');

        // check to see how mnay toppings have already been clicked:
        var parentCollection = event.target.parentElement.parentElement.children;
        var allInputs = $(parentCollection).children().children();
        var total_checked = 0;

        $(allInputs).each( index => {
            if ($(allInputs[index]).attr('checked') != undefined) {
                total_checked = total_checked + 1;
            };
        }); 

        // if number of checked toppings lower than max allowed,
        // allow to click another topping
        if (max_toppings > total_checked) {
            $(inputChildren[0]).click();
        }
    });
});




 // changes the checked state of the input checkboxes
$(document).ready( () => {
    $('input[type="checkbox"]').on('click', event => {
        // if not checked before, onclick set to checked
        console.log("im in second");
        if ($(event.target).attr('checked') == undefined) {
            $(event.target).attr('checked', true);
            $(event.target).parent().attr('style', 'background-color: green;');
        }

        else {
            // if clicked before, onclick set checked to null
            $(event.target).attr('checked', null);
            $(event.target).parent().attr('style', 'background-color: #ffa500;')
        }
    });
});