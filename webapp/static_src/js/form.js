import axios from "axios";

const updateEvent = new Event('update');
const changeSavedEvent = new Event('change-saved');

class Form {
    constructor (config) {
    }
}

export default () => {
    document.querySelectorAll(".js-form-config").forEach(function(element) {
        new Form(JSON.parse(element.innerHTML));
    });
}
