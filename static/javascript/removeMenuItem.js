/** 
 * contains instructions for removing items from the menu
 */

$(document).ready( () => {
    $(".remove_btn").on('click', () => {
        // get the item info
        var inputs = $(event.target).parent().parent().children().children("input");
        var remove_id = $(inputs).filter('.id').val();
        var remove_category = $(inputs).filter('.category').val();
        console.log(remove_id)
        
        // make an ajax request to the server with the item info
        $.ajax({
            url: "removeMenuItem",
            method: "POST",
            data: {
                "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
                "remove_id": remove_id,
                "remove_category": remove_category
            },

            // on success, refresh the page so that the item is removed
            success: () => {
                window.location.reload();
            }
        })
    })
});