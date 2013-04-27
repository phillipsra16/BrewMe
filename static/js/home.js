function fill_user_recipes() {
    $.get( STATIC_URL + 'recipe_entry.htm', function(template) {
        console.log('here');
        //Create detached DOM node
        var $tpl = $('<div />').html(template);
        //Iterate over key, value pairs using underscore.js
        _.each(recipes.u_recipes, function(value, key) {
            //Build up our identifier into the template and append the value
            var identifier = '#recipe_' + key;
            console.log(identifier + ' ' + value);
            $tpl.find(identifier).html('<p><b>' + key + '</b>: ' + value);
        });
        //Match this class of the template with the rest of our spans
        $tpl.css('clear', 'left'); 
        //Plop that shit in there
        $(add_to).append($tpl);
    });
}


$(document).ready(function () {
    fill_user_recipes();
});
