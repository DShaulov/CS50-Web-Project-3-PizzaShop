/**
 * contains event listeners for menu plus and minus buttons
 */

document.addEventListener('DOMContentLoaded', () => {
    const plusBtns = document.querySelectorAll('.plusBtn');
    plusBtns.forEach( element => {
        element.addEventListener('click', () => {
            const td = element.parentElement.parentElement.nextElementSibling.childNodes;

            for (let i = 0; i < td.length; i++){
                if (td[i].tagName == "TD") {
                    const slideDiv = td[i].lastChild;
                    $(slideDiv).slideToggle(1000);
                }
            }
        });
    });


    //! need to change it to confirm button
    // set event listeners for confirm buttons

    /* plusBtns.forEach( element => {
        element.addEventListener('click', () => {
            // when plus is clicked, take the table row associated with the plus,
            // and copy it to the cart
            const tableRow = element.parentElement.parentElement;
            const title = tableRow.parentElement.parentElement.dataset['title'];

            // create a new table row
            const row = document.createElement('tr');
            row.className = "formLabel myRow";

            // add minus image to the table row
            const tableData = document.createElement('td');
            const minusImage = createImg();
            
            // add event listener on click, that deletes the row, and lowers cart item counter
            minusImage.addEventListener('click', element => {
                console.log(element.toElement.parentElement.parentElement);
                const delRow = element.toElement.parentElement.parentElement;
                delRow.remove();

                // lower the cart item counter by one
                var counter = parseInt(document.querySelector('.counter').innerHTML);
                counter = counter - 1;
                document.querySelector('.counter').innerHTML = counter;
            });
            minusImage.style = "curser: pointer;";
            tableData.append(minusImage);
            tableData.className = "myTD";
            row.append(tableData);

            // adding title to the table row
            const tableDataTwo = document.createElement('td');
            tableDataTwo.className = "myTD";
            tableDataTwo.append(title);
            row.append(tableDataTwo);

            // add item info to the table row
            for (let i = 0; i < tableRow.childElementCount - 1; i++) {
                const tableData = document.createElement('td');
                tableData.innerHTML = tableRow.children[i].innerHTML;
                tableData.className = 'myTD';
                row.append(tableData);
            }; */




            // ! see later if needed
            // add event listeners to all confirm buttons
            /* const confirmBtns = document.querySelectorAll('.confirmBtn');
            confirmBtns.forEach( element => {
                element.addEventListener('click', () => {
                    // when confirm is clicked, increment the cart counter
                    var counter = parseInt(document.querySelector('.counter').innerHTML);
                    counter = counter + 1;
                    document.querySelector('.counter').innerHTML = counter;

                    // once confirm is clicked, add the row to the menu items table 
                    document.querySelector('#menuItemsTable').append(row);
                });
            }); */
            


            //! if no use, delete later
            // send a post request to add item to cart
            /* const request = new XMLHttpRequest();
            request.open('POST', '/addToCart')
            request.onload = () => {
                console.log('im loaded')
            };
            var csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value
            const data = new FormData();
            data.append('csrfmiddlewaretoken', csrf);
            request.send(data);
        });
    }); */
});

