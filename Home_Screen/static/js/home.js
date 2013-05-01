function fill_user_recipes() {
    $.get('/home/user_recipes', function(data) {
        json_data = JSON.parse(data);
        //Create detached DOM node
        //Iterate over key, value pairs using underscore.js
        _.each(json_data['recipes'], function(recipe_dict) {
            $.get( STATIC_URL + 'recipe_entry.htm', function(template) {
            var $tpl = $('<a ><div /></a>').html(template);
            //Build up our identifier into the template and append the value
            _.each(recipe_dict, function(value, key){ 
                    //Handle id => href url
                    if (key == 'id') {
                        console.log($tpl);
                        $tpl.prop('href','http://66.169.77.204:8000/recipe/view_recipe/' + value);
                        console.log(value);
                    }
                    else { 
                        var identifier = '#recipe_' + key;
                        console.log('value = ' + value);
                        console.log('key = ' + key);
                        //console.log(identifier + ' ' + value);
                        $tpl.find(identifier).html('<p><b>' + key + '</b>: ' + value);
                    }
                    //Match this class of the template with the rest of our spans
                    $tpl.css('clear', 'left'); 
                    //Plop that shit in there
                    $('#user_recipes_table').append($tpl);
                });
            });
        });
    });
}


$(document).ready(function () {
    fill_user_recipes();
});


//Django provided ajax send
$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

