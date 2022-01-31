import axios from "axios";

function validateField(formElement, fieldElement) {
  let formData = new FormData(formElement);
  formData.append('__field_name__', fieldElement.name);

  axios.post(formElement.action, formData).then(function (response) {
    let errors = response.data.errors;
    let errorsWrapperElement = document.getElementById(`error-wrapper-${fieldElement.name}`);
    if (errors.length === 0) {
      if (errorsWrapperElement) {
        errorsWrapperElement.innerHTML = "";
      }
      fieldElement.classList.remove('is-invalid');
      fieldElement.classList.add('is-valid');
    } else {
      if (errorsWrapperElement) {
        let errorsHtml = '';
        for (let i = 0; i < errors.length; i++) {
          errorsHtml += `<span class="invalid-feedback">${errors[i]}</span>`;
        }
        errorsWrapperElement.innerHTML = errorsHtml;
      }
      fieldElement.classList.remove('is-valid');
      fieldElement.classList.add('is-invalid');
    }
  });
}

export default function initFormValidation() {
  document.querySelectorAll("form").forEach(function (formElement) {
    formElement.querySelectorAll("[name]").forEach(fieldElement => {
      fieldElement.addEventListener("change", event => {
        validateField(formElement, fieldElement);
      });
    });
  });
}
