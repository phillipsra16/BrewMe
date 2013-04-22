//Global variables

//Recipe that builds up as the user adds ingredients
recipe = {
    hop : [], //List of Dictionaries of hop ingredients
    yeast : {}, //Dictionary of yeast ingredients
    fermentable : [] //List of Dictionaries of fermentable ingredients
};


//Dictionaries that store the currently worked on ingredients
current_yeast = {};
current_hop = {};
current_fermentable = {};


//Sends a post request to recipe/design view and redirects to view recipe page
function post_recipe() {
    $.post(
        "/recipe/design/",
        {msg: JSON.stringify(recipe)},
        function (data) {
            ret_JSON = JSON.parse(data)
            window.location.href = ret_JSON['url'];    
        }
    );
}


//Parses the name of the ingredient from the id
function id_from_name(object_name) {
    switch(object_name) {
        case 'hop_box':
            return 'hop';
        case 'fermentable_box':
            return 'fermentable';
        case 'yeast_box':
            return 'yeast';
        case 'recipe_box':
            return 'recipe';
        default:
            console.log(object_name);
            return 'nothing found';
    }
}


function update_ingredient(selector) {
    // We are forming our get request name and id here
    //TODO: Clean this up!
    var ingredient = selector.target;
    //This will return the ingredient from the ingredient_box html element
    //I have to go this far up the chain in order to decouple the submit button from the form
    //it is associated with. Otherwise the Django interperter will try to redirect on submit.
    var ingre_type = id_from_name($(ingredient).parent().parent().parent().attr('id'));
    //if (ingre_type == 'nothing found') //Something went wrong
    //    return;
    var ingre_id = $(ingredient).children(':selected').val();
    url_base = 'http://66.169.77.204:8001/recipe/';
    $.ajax({
        type:'GET',
        url: url_base + ingre_type + '/' + ingre_id + '/',
        success: function(data) {
            //TODO: Parse data dict and display beautifully. Here would be a good place to re-use some of the code from the project last semester
            //TODO: save the ingredient in a global var. This will make parsing it and adding to dict much easier
            $('#current_template').html(data);
            $('#current_template').css("visibility", "visible");
            $('#sub_' + ingre_type).css("visibility", "visible");
            var ret_json = JSON.parse(data);
            $('#id_alpha_acid').val(ret_json.alpha_acid + "");
        },
    });
}


function update_recipe(data) {
    //Dictionary containing all recipe information
    target = data.target;
    var type = id_from_name($(target).parent().attr('id'));
    //Call method to actually post recipe if need be
    if (type == 'recipe')
        post_recipe();
    //Create an empty ingredient dict to be filled
    var ingredient = {};
    //For each box in the ingredient div..
    //I.E. for each attribute describing this ingredient, fill out the ingredient dict with the value
    _.each($(target).parent().children('form').children('p').children('input'), function (data) {
        if ($(data).val() == null) {
            console.log("Please fill in all of the data" + $(data).val());
            return;
        }
        var label = $(data).attr('name');
        console.log(label + " " + $(data).val())
        ingredient[label] = $(data).val();
        //$(ingredient).extend({label : $(data).val()});
    });
    var val = $(target).parent().children('form').children('p').children('select').children(':selected').html();

    // ******************************************************************
    // make sure hop time is recorded
    ingredient.time = $('#id_time').val();
    // record hop usage
    ingredient.use = $('#id_use').val();
    // ******************************************************************
    
    if (val == null) {
        return;
    }
    ingredient.name = val;
    if (type == 'yeast')
        recipe['yeast'] = ingredient;
    else
        recipe[type].push(ingredient);
    console.log(recipe);
}


$(document).ready(function() {
    // make the time select field from being too large
    $('#id_time').css('width','55px');
    $('#id_amount').css('width','45px');
    $('#id_use').css('width','100px');
    $('#id_alpha_acid').css('width','55px');
    $('#id_hop_name,#id_time,#id_use,#id_alpha_acid,#id_amount').
            css('margin-right','5px');


    //Register event listeners
    $('.selector').on('change', update_ingredient);
    $('input[type=submit]').on('click', update_recipe);
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
