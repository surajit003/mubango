$(document).on('ready',function(){
    "use strict";


    /* =============== Ajax Contact Form ===================== */
    $('#contactform').submit(function(){
        var action = $(this).attr('action');
        $("#message").slideUp(750,function() {
        $('#message').hide();
            $('#submit')
            .after('<img src="images/ajax-loader.gif" class="loader" />')
            .attr('disabled','disabled');
        $.post(action, {
            name: $('#name').val(),
            email: $('#email').val(),
            comments: $('#comments').val(),
            verify: $('#verify').val()
        },
            function(data){
                document.getElementById('message').innerHTML = data;
                $('#message').slideDown('slow');
                $('#contactform img.loader').fadeOut('slow',function(){$(this).remove()});
                $('#submit').removeAttr('disabled');
                if(data.match('success') != null) $('#contactform').slideUp('slow');

            }
        );
        });
        return false;
    });

    var tabs =  $(".ctabs li a");
    tabs.on('click', function(){
        var content = this.hash.replace('/','');
        tabs.removeClass("active");
        $(this).addClass("active");
    $("#content").find('.accountform').hide();
    $(content).fadeIn(200);
    });


    $('.accountbtn').on('click', function(){
        $('.popupsec').fadeIn();
        $('html').addClass('no-scroll');
    });
    $('.closepopup').on('click', function(){
        $('.popupsec').fadeOut();
        $('html').removeClass('no-scroll');
    });

    $('a.scrollup, .scrolldown, .listingnav a').on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({ scrollTop: $($(this).attr('href')).offset().top}, 500, 'linear');
    });

    // Get Header Height //
    var stick = $('header').height();
    $('.openfilters, .mlfilter-sec, .half-map, .ml-listings').css({
        "padding-top": stick
    });

    // Filter Open Close //
    $('.openfilters').on('click', function(){
        $(this).addClass("active");
        $('.mlfilter-sec').addClass('active');
        $('.ml-listings').addClass('active');
    });
    $('.closefilter').on('click', function(){
        $('.openfilters').removeClass("active");
        $('.mlfilter-sec').removeClass('active');
        $('.ml-listings').removeClass('active');
    });

    // Filter Open Close //
    $('.openfilterbtn').on('click', function(){
        $('.mlfilter-sec').addClass('active');
        $('html').addClass('no-scroll');
        $(this).addClass('active');
    });
    $('.closefilter').on('click', function(){
        $('.openfilterbtn').removeClass("active");
        $('.mlfilter-sec').removeClass('active');
        $('html').removeClass('no-scroll');
    });

    // Grids Filter Active //
    $('.ml-filterbar ul li').on('click', function(){
        $('.ml-filterbar ul li').removeClass('active');
        $(this).addClass('active');
    });
    $('.doubleplaces').on('click', function(){
        $('.ml-listings').addClass('godouble');
        $('.ml-placessec').addClass('godouble');
        $('.ml-placessec').removeClass('golist');
        $('.ml-listings').removeClass('golist');
        $('.places').removeClass('makelist');
    });
    $('.listingplaces').on('click', function(){
        $('.ml-listings').addClass('golist');
        $('.ml-placessec').addClass('golist');
        $('.ml-listings').removeClass('godouble');
        $('.places').addClass('makelist');
    });
    $('.singleplaces').on('click', function(){
        $('.ml-listings').removeClass('golist');
        $('.ml-listings').removeClass('godouble');
        $('.ml-placessec').removeClass('golist');
        $('.ml-placessec').removeClass('godouble');
        $('.places').removeClass('makelist');
    });

    /* Dropdowns Custom */
    $(".customdropdown").on("click",function(e){
        e.stopPropagation();
    });
    $('.customdropdown > span').on('click', function(){
        $('.customdropdown').removeClass('active');
        $('.customdrops').fadeOut();
        $(this).parent().addClass('active');
        $(this).parent().find('.customdrops').fadeIn();
        return false;
    });
    $('body').on('click', function(){
        $('.customdrops').fadeOut();
        $('.customdropdown').removeClass('active');
    });

    (function ($) {
    $('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');

    $('.tab ul.tabs li a').on('click', function(g){
         var tab = $(this).closest('.tab'),
        index = $(this).closest('li').index();

        tab.find('ul.tabs > li').removeClass('current');
        $(this).closest('li').addClass('current');

        tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
        tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();

    g.preventDefault();
    } );
    })(jQuery);


    var tabss =  $(".ctabss li a");
    tabss.on('click', function(){
        var contents = this.hash.replace('/','');
        tabss.removeClass("active");
        $(this).addClass("active");
    $("#contents").find('div.ccontents').hide();
    $(contents).fadeIn(200);
    });

    $('.slistingoption .slisting').on('click', function(){
        $('.slisting').removeClass('selected');
        $(this).addClass('selected');
    });


    /* Minimal Menu Dropdown */
    $(".userdropsec").on("click",function(e){
        e.stopPropagation();
    });
    $('.userdropsec > span').on('click', function(){
        $(this).parent().addClass('active');
    });
    $('body').on('click', function(){
        $('.userdropsec').removeClass('active');
    });

    /* Minimal Menu Dropdown */
    $(".rnaver").on("click",function(e){
        e.stopPropagation();
    });
    $(".rnaver li.menu-item-has-children > a").on("click",function(){
        $(this).parent().siblings().children("ul").slideUp();
        $(this).parent().siblings().removeClass("active");
        $(this).parent().children("ul").slideToggle();
        $(this).parent().toggleClass("active");
        return false;
    });

    /* Skip Loading */
    $('.page-loading > span').on('click', function(){
        $(this).parent().fadeOut();
    });

    /* Responsive Header */
    $('.rheader > span').on('click', function(){
        $('.responsiveheader').addClass('active');
    });
    $('.closeresmenu').on('click', function(){
        $('.responsiveheader').removeClass('active');
    });

    /*** FIXED Menu APPEARS ON SCROLL DOWN ***/
    $(window).on('scroll', function(){
        var scroll = $(window).scrollTop();
        if (scroll >= 50) {
        $(".ml-filterslide").addClass("scrollclass");
        }
        else{
        $(".ml-filterslide").removeClass("scrollclass");
        $("ml-filterslide").addClass("");
        }
    });


});



$(window).on('load',function(){
    "use strict";

    $('.page-loading').fadeOut();

    var full_height = $(window).height();
    $(".half-map .map").css({"height":full_height});

});
