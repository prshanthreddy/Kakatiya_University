function space(object) {
    if (object.value != "Approved") {
        document.getElementById('txt').innerHTML = "<textarea name='rstat' placeholder='Reason for Rejection' class='area' ></textarea>";
    }
    else {
        document.getElementById('txt').innerHTML = "";
    }
}