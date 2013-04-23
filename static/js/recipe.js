    //Global variables

//Recipe that builds up as the user adds ingredients
recipe = {
    hop         : [], //List of Dictionaries of hop ingredients
    yeast       : {}, //Dictionary of yeast ingredients
    fermentable : [], //List of Dictionaries of fermentable ingredients
    meta        : {}, //Recipe metadata
};


//Dictionaries that store the id of the currently worked on ingredients
current = {
    yeast : '',
    hop : '',
    fermentable : ''
};

        //\Global Variables

    
        //POST methods and helpers
        
//Validates that a recipe is ready to send
function validate_recipe() {
    return recipe.hop.length > 0 && recipe.yeast != null && recipe.fermentable > 0;
}


//Sends a post request to recipe/design view and redirects to view recipe page
function post_recipe() {
    //Error checkign
    if (validate_recipe()) {
        //Set the name and send it. Upon success, go to it's view_recipe page
        recipe.meta['recipe_name'] = $('#recipe_name').val();
        $.post(
            "/recipe/design/",
            {msg: JSON.stringify(recipe)},
            function (data) {
                ret_JSON = JSON.parse(data)
                window.location.href = ret_JSON['url'];    
            }
        );
    } else {
        feedback('error', $('#main_body'), 'Recipe is not completed');
    }
}


        //\POST methods and helpers

        
        //Ingredient methods and helpers


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
            return 'nothing found';
    }
}


//Fill out the ingredient template with data from server
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
            //TODO: Make this more agnostic of the type
            $('#id_alpha_acid').val(ret_json.alpha_acid + "");
            current[ingre_type] = ret_json.id;
        },
    });
}


//Display the next addition to the global recipe
function add_read_only_template(ingredient, type) {
    //Get this first because we will need to change the type immediately if
    //the type is fermentable. Yay consistency!!!!
    var add_to = '#' + type + '_box';
    if (type == 'fermentable') 
        type = 'grain';
    console.log(type);
    //Grab the template
    $.get( STATIC_URL + type + '_entry.htm', function(template) {
        //Create detached DOM node
        var $tpl = $('<div />').html(template);
        //Iterate over key, value pairs using underscore.js
        _.each(ingredient, function(value, key) {
            //Build up our identifier into the template and append the value
            var identifier = '#' + type + '_' + key;
            console.log(identifier + ' ' + value);
            $tpl.find(identifier).html('<p><b>' + key + '</b>: ' + value);
        });
        console.log(add_to);
        //Match this class of the template with the rest of our spans
        $tpl.addClass('span12 well');
        //Plop that shit in there
        $tpl.insertBefore(add_to);
    });
}


//Update the global recipe with the latest data from templates
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
    add_ingredient = true;
    _.each($(target).parent().children('form').children('p').children('input'), function (data) {
        //Error checking. If we don't have a value we need, provide feedback and 
        //set condition to break out of method
        if ($(data).val() == '' && add_ingredient) {
            feedback('error', $(target).parent(), 'Please fill out all of the data');
            add_ingredient = false;
            return;
        }
        //If we pass error condition above, add this label and value to the dict
        var label = $(data).attr('name');
        ingredient[label] = $(data).val();
    });
    //For Quality of life on backend
    ingredient.id = current[type]; 
    //First off, i apologize
    //Secondly, grab the name of the ingredient from the selector. I did it this way
    //to make this method agnostic to the ingredient type calling it
    var val = $(target).parent().children('form').children('p').children('select').children(':selected').html();


    //TODO Make this agnostic
    // ******************************************************************
    // make sure hop time is recorded
    ingredient.time = $('#id_time').val();
    // record hop usage
    ingredient.use = $('#id_use').val();
    // ******************************************************************
    
    if (val == null) return;

    ingredient.name = val;
    //If error condition in _.each loop wasn't triggered, we can add the yeast and send
    //this bad boy off and provide feedback
    if (add_ingredient) {
        if (type == 'yeast')
            recipe['yeast'] = ingredient;
        else
            recipe[type].push(ingredient);
        feedback('added', $(target).parent(), 'Ingredient was added');
        add_read_only_template(ingredient, type);
    }
    console.log(recipe);
}


/*Creates a message and binds a focus event to remove the message
                                    --------------------- Object calling this
                                    |       ------------- Message to display
                                    |       |       ----- Button to hide
                                    |       |       |   */
function feedback_message_factory(object, message, button) {
    //TODO Finish button bullshit
    $(button).hide();
    var element = $('<label>')
        .attr('id', 'id_message')
        .html(message);
    $(object).prepend(element);
    $(object).on('focus', 'input, select', function () {
        $(button).show();
        $('#id_message').remove();
    });
}


/*Provides user feedback
 *                  ------------------- Type of method ('error', 'added')
 *                  |       ----------- Object calling this
 *                  |       |       --- Message to display
 *                  |       |       |   */ 
function feedback(type, object, message) {
    focus_time = 2500;
    var initial_color = $(object).css('background-color');
    sub_button = $(object).children('submit');
    switch (type) {
        case 'added':
            $(object).css('background-color', 'green');
            feedback_message_factory(object, message, sub_button);
            $(object).animate({
                'background-color' : initial_color
            }, focus_time);
            break;
        case 'error':
            $(object).css('background-color', 'red');
            feedback_message_factory(object, message, sub_button);
            $(object).animate({
                'background-color' : initial_color
            }, focus_time);
            break;
        default:
            console.log(type + " " + object + " " + message);
    }

}


        //\Ingredient methods and helpers
        

        //Boilerplate stuff


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
