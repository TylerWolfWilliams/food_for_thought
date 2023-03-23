$(document).ready(function() {
    $('#authorInput').select2({
        theme: 'bootstrap-5',
        placeholder: 'None',
        ajax: {
            url: '/recipes/fetch_author/',
            dataType: 'json'
        }
    });
    $('#categoryInput').select2({
        placeholder: 'None',
        theme: 'bootstrap-5',
        ajax: {
            url: '/recipes/fetch_cats/',
            dataType: 'json'
        }
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
