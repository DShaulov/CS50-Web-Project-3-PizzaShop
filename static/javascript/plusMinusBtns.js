/**
 * contains event listeners for menu plus button
 */

 // on click of plus button, slide down the slide div
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
});

