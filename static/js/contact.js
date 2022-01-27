

let btn = document.getElementById("btn");

btn.addEventListener("click", (e) => {

    e.preventDefault();

    let name = document.getElementById("name");
    let email = document.getElementById("email");
    let branch = document.getElementById("branch");
    let session = document.getElementById("session");
    let subject = document.getElementById("subject");
    let text_area = document.getElementById("text_area");

    let message = {

        name: name.value,
        email: email.value,
        branch: branch.value,
        session: session.value,
        subject: subject.value,
        text_area: text_area.value
    }

    

    if (name.value == "" && email.value == "" && branch.value == "" && session.value == "" && subject.value == "" && text_area.value == "") {

        let alert = document.getElementById("alert");
        alert.innerHTML = `<div class="alert alert-danger alert-dismissible fade show mb-0" role="alert">
                        <strong>Error!</strong> Your message is not send successfully please fill the form carefully.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                       </div>`;

        setTimeout(function () {
            alert.innerHTML = "";
        }, 3000);

    }
    else {


        let alert = document.getElementById("alert");
        alert.innerHTML = `<div class="alert alert-success alert-dismissible fade show mb-0" role="alert">
                        <strong>Success!</strong> Your message is send successfully.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                       </div>`;

        setTimeout(function () {
            alert.innerHTML = "";
        }, 3000);

    }


    name.value = "";
    email.value = "";
    branch.value = "";
    session.value = "";
    subject.value = "";
    text_area.value = "";

});
