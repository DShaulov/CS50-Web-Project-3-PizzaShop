/**
 * contains a function that calculates total cost of checkout menu items
 */
$(document).ready( () => {
    totalCost();
});

function totalCost(){
    // getting the table that has the price
    const table = $("table[data-checkout_table]");

    // if there is a sub in the menu, count the amount of toppings and add 0.50$ to the total
    const all_titles = $(table).children().children().children('td[data-title]');
    for (let i = 0; i < all_titles.length; i++) {
        if ($(all_titles[i]).text() == "Sub") {
            // count number of extra's
            const num_of_extras = $(all_titles[i]).siblings('td[data-extra]').text().split(", ").length;
            console.log(num_of_extras);
            // multiply number of extra's by 0.50, and add it to the price td
            const current_price = $(all_titles[i]).siblings('td[data-price]').text();
            const new_price = parseFloat(current_price) + (0.50 * num_of_extras);
            console.log(new_price);
            $(all_titles[i]).siblings('td[data-price]').text(new_price.toFixed(2) + "$");
        };
    };

    const price_text = $(table).children().children().children('td[data-price]').text();
    const price_array = price_text.slice(0, price_text.length - 1).split('$');

    // calculating the sum of the array members
    var total_sum = 0;
    for (let i = 0; i < price_array.length; i++){
        total_sum = total_sum + parseFloat(price_array[i]);
    };
    // adding a zero to the end
    total_sum = total_sum.toFixed(2);

    // insert total_sum to the last row
    $('td[data-price_total]').text('Total: ' + total_sum + '$');
}