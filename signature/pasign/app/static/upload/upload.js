document.addEventListener("DOMContentLoaded", function () {
    var successMessage = document.getElementById('success-message');
    if (successMessage) {
        setTimeout(function () {
            successMessage.style.display = 'none';
        }, 3000);
    }

    var selDiv = "";
    document.querySelector('#id_signature_files').addEventListener('change', handleFileSelect, false);
    selDiv = document.querySelector("#selectedFiles");

    function handleFileSelect(e) {
        if (!e.target.files) return;

        selDiv.innerHTML = "";

        var files = e.target.files;
        for (var i = 0; i < files.length; i++) {
            var f = files[i];

            selDiv.innerHTML += f.name + "<br/>";
        }
    }
});
