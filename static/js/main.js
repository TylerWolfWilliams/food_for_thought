$(document).ready(function() {
    $('.select2-fancy-choice').select2({
        theme: 'bootstrap-5'
    });
    $('#categoryInput').select2({
        placeholder: 'None',
        theme: 'bootstrap-5'
    });
});

function confirmAJAX(url) {
    $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        success: (data) => {
            console.log(data["response"])
            $(data["id"]).replaceWith(data["response"])
        },
    })
};


function toggleSaveAJAX(url) {
    $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        success: (data) => {
            console.log(data["response"])
            $(data["id"]).replaceWith(data["response"])
        },
    })
};
