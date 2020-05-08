
// Clear the console after 1 sec to get rid to errors spamming me
setTimeout(() => {
    console.clear()
}, 3000);

// Get all the inputs
$(".addbtndone").click(function (e) { 
    e.preventDefault();
    let taskname = $("#first_name2").val();
    let taskdesc = $("#textarea1").val();

    console.log(`name = ${taskname} and desc = ${taskdesc}`)

    let custom_card = `<div class="col s12 m3">
        <div class="card">
        <div class="card-image">
            <img src="https://source.unsplash.com/lUaaKCUANVI/600x400">
            <span class="card-title">${taskname}</span>
            <a class="btn-floating halfway-fab waves-effect waves-light red"><i class="material-icons">done</i></a>
        </div>
        <div class="card-content">
            <p>${taskdesc}</p>
        </div>
        </div>
    </div>`



    // Append the card to ALL id
    // $("#all").html(custom_card);
    document.querySelector("#rowall").innerHTML += custom_card

    // Remove empty boxes icon
    document.querySelectorAll(".emptybox-wrapper")[0].style.display = "none";

    // Write to minidb.txt
    eel.writetofile()()
    

});



// create a reavel card


