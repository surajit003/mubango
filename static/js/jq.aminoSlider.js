//Custom amino plugin
(function($) {
    "use strict";

    //amino slider plugin
    $.fn.aminoSlider = function () {

        return this.each(function() {

            //amino slider component
            var $aminoSliderComponent = $(this);
            var $min = ($aminoSliderComponent.attr('data-min') || 0);
            var $max = ($aminoSliderComponent.attr('data-max') || 1000);
            var $step = ('step', $aminoSliderComponent.attr('data-step') || 0);
            var $value = ($aminoSliderComponent.attr('data-value') || 50);

            //slider template
            var $aminoSlider = $('<input class="am-slider" type="range"/>');

            //slider thumb
            var $aminoThumb = $('<div class="am-thumb"></div>');

            //slider tooltip template
            var $aminoTooltip = $('<div class="am-tooltip"></div>');

            //slider configuration
            $aminoSlider.attr('min', $min);
            $aminoSlider.attr('max', $max);
            $aminoSlider.attr('step', $step);
            $aminoSlider.val($value);


            /*set state on event triggers*/
            var setRangePostions = function(event) {

                var rangeVal = $aminoSlider.val();
                var offsetWidth = $aminoSlider[0].offsetWidth;
                var offsetTop = $aminoSlider[0].offsetTop;
                var leftPostion = rangeVal/$max * (offsetWidth - 37) + 'px';

                //on all states set thumb position range
                $aminoThumb.css({'left': leftPostion});

                //on active state set tooltip top position
                if(event === 'mousedown') {
                    $aminoTooltip.css({'top': offsetTop-70});
                }

                //on normal state set thumb range value
                if(event === 'mouseup' || event === 'init') {
                    $aminoThumb.html(rangeVal);
                }

                //on drag or active state set tooltip range.
                if(event === 'change' || event === 'mousedown') {
                    $aminoTooltip.css({
                        'left': leftPostion,
                        'margin-left': $aminoSlider[0].offsetLeft - 10 + 'px'
                    });
                }
            }

            //on active state
            $aminoSlider.on('mousedown touchstart', function() {
                $aminoTooltip.addClass('am-tooltip-active-state');
                $aminoThumb.html('');
                $aminoTooltip.html(this.value);
                setRangePostions('mousedown');
            });

            //on normal state
            $aminoSlider.on('mouseup touchend', function() {
                $aminoTooltip.removeClass('am-tooltip-active-state');
                setRangePostions('mouseup');
            });

            //on drag state
            $aminoSlider.on('input change touchmove', function() {
                //set value
                $aminoSliderComponent.attr('data-value', this.value);
                $aminoTooltip.html(this.value);
                setRangePostions('change');
            });

            //on window rezise
            $(window).on('resize', function(e) {
                setRangePostions();
            });

            //append slider template into amino component
            $aminoSliderComponent.append($aminoThumb, $aminoSlider, $aminoTooltip);

            //init
            setRangePostions('init');
        });
    };

})(jQuery);

(function($) {
    "use strict";

    //Select the slider element.
    var $slider = $('.slider');

    $slider.aminoSlider();

})(jQuery);
