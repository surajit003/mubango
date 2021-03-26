$('#btn_review').click(function (e) {
    e.preventDefault()
    $('#review_status').empty()
    experience = $('#experience').val();
    if (experience) {
        comment = $('#comment').val();
        csrf_token = $("input[name=csrfmiddlewaretoken]").val()
        business_slug = $('#business_slug').val()
        image_1 = document.getElementById('image_1').files[0];
        image_2 = document.getElementById('image_2').files[0];
        image_3 = document.getElementById('image_3').files[0];
        var formData = new FormData();
        formData.append("comment", comment);
        formData.append("experience", experience);
        formData.append('csrfmiddlewaretoken', csrf_token)
        formData.append('business_slug', business_slug)
        formData.append('image_1', image_1)
        formData.append('image_2', image_2)
        formData.append('image_3', image_3)
        submit_review(formData)

    } else {
        $('#review_status').append('You must fill in the review section before submitting enter')
    }

})

function submit_review(formdata) {
    $.ajax({
        type: "POST",
        url: '/mb/review/add-review/',
        data: formdata,
        contentType: false,
        processData: false,
        cache: false,
        enctype: 'multipart/form-data',
        success: function (response) {
            //if request if made successfully then the response represent the data
            if (response['status'] === 201) {
                $('#review_status').append(response['response'])
                setTimeout(function () {
                    location.reload();
                }, 2000);
            } else {
                $('#review_status').append(response['response'])

            }

        }
    });

}

function add_service_rating(formdata) {
    $.ajax({
        type: "POST",
        url: '/mb/review/service/rating/',
        data: formdata,
        contentType: false,
        processData: false,
        cache: false,
        success: function (response) {
            //if request if made successfully then the response represent the data

        }
    });

}

$('#food').on('change', function () {
    business_slug = $('#business_slug').val()
    rating = this.value;
    csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    service_name = 'Food'

    var formData = new FormData();
    formData.append("rating", rating);
    formData.append("service_name", service_name);
    formData.append('csrfmiddlewaretoken', csrf_token)
    formData.append('business_slug', business_slug)
    add_service_rating(formData)
});

$('#amenities').on('change', function () {
    business_slug = $('#business_slug').val()
    rating = this.value;
    csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    service_name = 'Amenities'

    var formData = new FormData();
    formData.append("rating", rating);
    formData.append("service_name", service_name);
    formData.append('csrfmiddlewaretoken', csrf_token)
    formData.append('business_slug', business_slug)
    add_service_rating(formData)
});
$('#pricing').on('change', function () {
    business_slug = $('#business_slug').val()
    rating = this.value;
    csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    service_name = 'Pricing'

    var formData = new FormData();
    formData.append("rating", rating);
    formData.append("service_name", service_name);
    formData.append('csrfmiddlewaretoken', csrf_token)
    formData.append('business_slug', business_slug)
    add_service_rating(formData)
});
$('#parking').on('change', function () {
    business_slug = $('#business_slug').val()
    rating = this.value;
    csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    service_name = 'Parking'

    var formData = new FormData();
    formData.append("rating", rating);
    formData.append("service_name", service_name);
    formData.append('csrfmiddlewaretoken', csrf_token)
    formData.append('business_slug', business_slug)
    add_service_rating(formData)
});
$('#music').on('change', function () {
    business_slug = $('#business_slug').val()
    rating = this.value;
    csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    service_name = 'Music'

    var formData = new FormData();
    formData.append("rating", rating);
    formData.append("service_name", service_name);
    formData.append('csrfmiddlewaretoken', csrf_token)
    formData.append('business_slug', business_slug)
    add_service_rating(formData)
});
$('#security').on('change', function () {
    business_slug = $('#business_slug').val()
    rating = this.value;
    csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    service_name = 'Security'

    var formData = new FormData();
    formData.append("rating", rating);
    formData.append("service_name", service_name);
    formData.append('csrfmiddlewaretoken', csrf_token)
    formData.append('business_slug', business_slug)
    add_service_rating(formData)
});

$('#service').on('change', function () {
    business_slug = $('#business_slug').val()
    rating = this.value;
    csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    service_name = 'Service'

    var formData = new FormData();
    formData.append("rating", rating);
    formData.append("service_name", service_name);
    formData.append('csrfmiddlewaretoken', csrf_token)
    formData.append('business_slug', business_slug)
    add_service_rating(formData)
});
