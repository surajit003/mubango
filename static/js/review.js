$('#btn_review').click(function (e) {
    e.preventDefault()
    comment = $('#comment').val();
    experience = $('#experience').val();
    csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    business_slug = $('#business_slug').val()
    $('#review_status').empty();
    submit_review(comment, experience, csrf_token, business_slug)

})

function submit_review(comment, experience, csrf_token, business_slug) {
    $.ajax({
        type: "POST",
        url: '/mb/review/add-review/',
        data: {
            'comment': comment,
            'experience': experience,
            'csrfmiddlewaretoken': csrf_token,
            'business_slug': business_slug,
        },
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
