$('#login').click(function (e) {
    username = $('#login_username').val();
    password = $('#login_password').val();
    $('#login_status').empty();
    if ((username) && (password)) {
        csrf_token = $("input[name=csrfmiddlewaretoken]").val()
        $.ajax({
            type: "POST",
            url: '/mb/account/login/',
            data: {
                'username': username,
                'password': password,
                csrfmiddlewaretoken: csrf_token
            },
            success: function (response) {
                //if request if made successfully then the response represent the data
                if (response['status'] === 200) {
                    $('#login_status').append(response['response'])
                    setTimeout(function () {
                        window.location.href = '/mb/home/';
                    }, 2000);
                } else {
                    console.log('res', response)
                    $('#login_status').append(response['response'])

                }

            }
        });
    } else {
        document.getElementById("error_login_username")
            .innerHTML = "Please enter a username";
        document.getElementById("error_login_username")
            .innerHTML = "Please enter a password";
    }


})

function logout() {
    $.ajax({
        url: '/mb/account/logout/',
        method: "GET",
        data: "logout",
        success: function () {
            console.log("logged out");
            window.location.href = '/mb/home/'
        },
        error: function () {
            console.log("nope, it didn't work");
            return false
        }
    });
}

function validate(phone) {
    if (phone.startsWith('+')) {
        phone = phone.slice(1, phone.length)
        if (phone.length <= 15) {
            let isnum = /^\d+$/.test(phone);
            return isnum
        }
    }
}

function send_signup_request(payload) {
    $.ajax({
        type: "POST",
        url: '/mb/account/signup/',
        data: {
            'username': payload['username'],
            'password': payload['password'],
            'csrfmiddlewaretoken': payload['csrf_token'],
            'email': payload['email'],
            'first_name': payload['first_name'],
            'last_name': payload['last_name'],
            'country': payload['country'],
            'state': payload['state'],
            'phone_number': payload['phone_number'],
            'address': payload['address']
        },
        success: function (response) {
            //if request if made successfully then the response represent the data
            if (response['status'] === 201) {
                $('#register_status').append(response['response'])
                setTimeout(function () {
                    window.location.href = '/mb/home/';
                }, 2000);
            } else {
                $('#register_status').append(response['response'])

            }

        }
    });

}

function validate_password(confirm_new_pass, new_pass) {
    if (confirm_new_pass === new_pass) {
        return true
    }
}

function update_profile_request(profile_id, payload) {
    $.ajax({
        type: "POST",
        url: '/mb/account/profile/' + profile_id + '/update/',
        data: {
            'csrfmiddlewaretoken': payload['csrfmiddlewaretoken'],
            'email': payload['email'],
            'first_name': payload['first_name'],
            'last_name': payload['last_name'],
            'phone_number': payload['phone_number'],
        },
        success: function (response) {
            //if request if made successfully then the response represent the data
            if (response['status'] === 204) {
                $('#profile_response').append(response['response'])
                setTimeout(function () {
                    window.location.href = '/mb/account/profile/' + profile_id;
                }, 2000);
            } else {
                $('#profile_response').append(response['response'])

            }

        }
    });

}

$('#signup_btn').click(function (e) {
    e.preventDefault();
    username = $('#signup_username').val();
    password = $('#signup_password').val();
    csrf_token = $("input[name=csrfmiddlewaretoken]").val();
    first_name = $('#signup_first_name').val();
    last_name = $('#signup_last_name').val();
    email = $('#signup_email').val();
    address = $('#signup_address').val();
    country = $('#country').val();
    state = $('#state').val();
    phone_number = $('#signup_phonenumber').val();

    if (country === '-1') {
        document.getElementById("error_country")
            .innerHTML = "Please select a country";
    } else {
        document.getElementById("error_country")
            .innerHTML = "";
        if (state) {
            document.getElementById("error_state")
                .innerHTML = "";
            if (username && password && email && first_name && last_name) {
                payload = {
                    "username": username,
                    "password": password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "csrf_token": csrf_token,
                    "email": email,
                    "address": address,
                    "country": country,
                    "state": state,
                    "phone_number": phone_number
                }
                send_signup_request(payload)

            } else {
                $('#register_status').empty();
                $('#register_status').append('Please fill in all required fields');
            }
        } else {
            document.getElementById("error_state")
                .innerHTML = "Please select a state";
        }
    }


});

$('#update_profile').click(function (e) {
    e.preventDefault();
    first_name = $('#profile_first_name').val();
    last_name = $('#profile_last_name').val();
    csrf_token = $("input[name=csrfmiddlewaretoken]").val();
    phone = $('#profile_phone').val();
    email = $('#profile_email').val();
    profile_id = $('#profile_id').val();
    profile_image = $('#profile_image')[0].files[0];
    var fd = new FormData();
    fd.append('image', profile_image)

    console.log(profile_image)

    if (profile_id) {
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone,
            'csrfmiddlewaretoken': csrf_token,

        }
        update_profile_request(profile_id, payload)

    } else {

    }


});

$("#signup_username").change(function () {
    var username = $(this).val();

    $.ajax({
        url: '/mb/account/ajax/validate_username/',
        data: {
            'username': username
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                document.getElementById('signup_btn').disabled = true;
                document.getElementById("error_username")
                    .innerHTML = "A user with this username already exists";
                document.getElementById('signup_btn').disabled = true;
                $("#signup_btn").css("background-color", "#595959");

            } else {
                document.getElementById('signup_btn').disabled = false;
                $("#signup_btn").css("background-color", "#28b8dc");
                document.getElementById("error_username")
                    .innerHTML = "";
            }
        }
    });

});

$("#signup_phonenumber").change(function () {
    var phonenumber = $(this).val();
    if (validate(phonenumber)) {
        $.ajax({
            url: '/mb/account/ajax/validate_phonenumber/',
            data: {
                'phonenumber': phonenumber
            },
            dataType: 'json',
            success: function (data) {
                if (data.is_taken) {
                    document.getElementById("error_phonenumber")
                        .innerHTML = "A user with this phonenumber already exists";
                    document.getElementById('signup_btn').disabled = true;
                    $("#signup_btn").css("background-color", "#595959");


                } else {
                    document.getElementById('signup_btn').disabled = false;
                    $("#signup_btn").css("background-color", "#28b8dc");
                    document.getElementById("error_phonenumber")
                        .innerHTML = "";
                }
            }
        });


    } else {
        document.getElementById("error_phonenumber").innerHTML = "That phonenumber is not in " +
            "right format e.g +254*********";
        document.getElementById('signup_btn').disabled = true;
        $("#signup_btn").css("background-color", "#595959");
    }


});

$("#signup_email").change(function () {
    var email = $(this).val();
    $.ajax({
        url: '/mb/account/ajax/validate_email/',
        data: {
            'email': email
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                document.getElementById('signup_btn').disabled = true;
                document.getElementById("error_email")
                    .innerHTML = "A user with this email already exists";
                $("#signup_btn").css("background-color", "#595959");


            } else {
                document.getElementById('signup_btn').disabled = false;
                $("#signup_btn").css("background-color", "#28b8dc");
                document.getElementById("error_email")
                    .innerHTML = "";
            }
        }
    });

});

$('#update_password').click(function (e) {
    e.preventDefault();
    current_password = $('#current_password').val();
    new_password = $('#new_password').val();
    confirm_password = $('#confirm_new_password').val()
    profile_id = $('#profile_id').val();
    csrf_token = $("input[name=csrfmiddlewaretoken]").val();

    if (validate_password(confirm_password, new_password)) {
        document.getElementById('password_response').innerHTML = ''
        $.ajax({
            url: '/mb/account/password/' + profile_id + '/update/',
            type: 'POST',
            data: {
                'profile_id': profile_id,
                'current_password': current_password,
                'new_password': new_password,
                'csrfmiddlewaretoken': csrf_token,
            },
            dataType: 'json',
            success: function (data) {
                console.log(data)
                if (data['status'] === 204) {
                    $('#password_response').append(data['response'])
                    setTimeout(function () {
                        logout();
                    }, 2000);
                } else {
                    $('#password_response').append(data['response'])

                }

            }
        });
    }
    else{
        $('#password_response').append('')
        document.getElementById('password_response').innerHTML = 'Passwords Dont Match'
    }


})
