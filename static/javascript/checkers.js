/**
 * Contains functions that check for correct user usage
 */

 // checks for correct usage on form input fields
function checkRegister () {
    const inputs = document.querySelectorAll('input');
    for (let i = 0; i < inputs.length; i++) {
        if (inputs[i].value == '') {
            inputs[i].placeholder = 'cant be empty';
            return false;
        }
    }
    // checks that password and cofirmation match

    if (document.querySelector('#password').value != document.querySelector('#confirmation').value) {
        document.querySelector('#errorMessage').innerHTML = "*passwords dont match";
        return false;
    }
    return true;
}

// checks for empty fields
function checkLogin () {
    const inputs = document.querySelectorAll('input');
    for (let i = 0; i < inputs.length; i++) {
        if (inputs[i].value == '') {
            inputs[i].placeholder = 'cant be empty';
            return false;
        }
    }

    return true;
}