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

function ajaxHelper(url) {
    $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        success: (data) => {
            $(data["id"]).html(data["response"])
        },
    })
};

