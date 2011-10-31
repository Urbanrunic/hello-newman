(function($) {
	// Matching regex with jQuery
	$.expr[':'].regex = function(elem, index, match) {
	    var matchParams = match[3].split(','),
	        validLabels = /^(data|css):/,
	        attr = {
	            method: matchParams[0].match(validLabels) ? 
	                        matchParams[0].split(':')[0] : 'attr',
	            property: matchParams.shift().replace(validLabels,'')
	        },
	        regexFlags = 'ig',
	        regex = new RegExp(matchParams.join('').replace(/^\s+|\s+$/g,''), regexFlags);
	    return regex.test($(elem)[attr.method](attr.property));
	}
	
	$(document).ready(function(){
        $('table tbody tr').css({ 'cursor': 'move' });
	
        $('table tbody').sortable({
            axis: 'y',
            update: function(){
            $('.footer').show();

            $.each($('table tbody tr'), function(i){
                $(this).find('input:regex(name, .*-order)').val(i + 1);
            });

            $(this).find('tr').removeClass('row1').removeClass('row2');
	
            $(this).find('tr:odd').addClass('row2');
                $(this).find('tr:even').addClass('row1');
            }
        });
    });
})(django.jQuery);
