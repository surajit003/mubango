$('#search').click(function (e) {
    e.preventDefault();
    var result = $('.dd-selected-text').text().split(" ");
    entity = result[0].toLowerCase()
    if (entity === 'club') {
        entity = 'business'
    }
    region = result[1].toLowerCase()

    window.location.href = '/mb/' + entity + '/list-by-region/' + region;


})
