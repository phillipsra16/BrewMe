// jQuery.ready 
$(function() {
    $('#recipe_name').text(recipe_dict.recipe_name);
    display_hop_schedule();
    display_grain_bill();
    display_yeast();
    display_misc();
    display_stats();
    display_comments();

    $('input[type=submit]').on('click', post_comment);
    $('#fork_btn').on('click', function() {
        var data = {'fork' : true};
        console.log(data);
        $.get(
            document.URL,   // the view_recipe function will respond with
                            //      the fork page
            {'fork' : true},
            function(data) {
                var newDoc = document.open("text/html", "replace");
                newDoc.write(data);
                newDoc.close();
            }
        );
    });
    console.log(recipe_dict);
}); // end jQuery.ready

function post_comment() {
    $.post(
        "/recipe/view_recipe/" + recipe_dict.rec_id + '/',
        {comm : $('#id_comm_text').val()},
        // callback appends the new comment
        function(data) {
            posted_comment();
            ret_json = JSON.parse(data);
            $.get(STATIC_URL + 'comment_entry.htm', function(template) {
                var $tpl = $('<div />').html(template); // make detached DOM node
                fill_comment_template(data, $tpl);
                $('#comment_entry_container').append($tpl.html());
            });
        }
    );
}

function posted_comment() {
    $('#posted_comment').slideDown(2000, function() {
        $('#posted_comment').slideUp('slow');
    });
}

// fills a hop entry template
// TODO: Abstract and make agnostic
function fill_hop_template(hop, $template) {
    $template.find('#hop_name').append(hop.name);
    $template.find('#hop_time').append(hop.time);
    $template.find('#hop_alpha').append(hop.alpha_acid);
    $template.find('#hop_amount').append(hop.amount);
    $template.find('#hop_use').append(function() {
        switch(hop.use) {
            case 1:
                return 'First Wort';
            case 2:
                return 'Boil';
            case 3:
                return 'Whirlpool';
            case 4:
                return 'Dry Hop';
            default:
                return 'Boil';
        }
    });
}

// loops over all of the hops in a hop schedule and inserts them into the page
function display_hop_schedule() {
    $.get(STATIC_URL + 'hop_entry.htm', function(template) {
        _.each(recipe_dict.hop_schedule, function(hop) {
            var $tpl = $('<div />').html(template); // make detached DOM node
            fill_hop_template(hop, $tpl);
            $('#hop_container').append($tpl.html());
        });
    });
}

// fills a grain entry template
function fill_grain_template(grain, $template) {
    $template.find('#grain_name').append(grain.name);
    $template.find('#grain_color').append(grain.color);
    $template.find('#grain_ppg').append(grain.potential_extract);
    $template.find('#grain_amount').append(grain.amount);
    $template.find('#grain_use').append(function() {
        switch(grain.use) {
            case 1:
                return 'Mash';
            case 2:
                return 'Boil';
            case 3:
                return 'Post-Boil';
            case 4:
                return 'Primary';
            case 5:
                return 'Secondary';
            default:
                return 'Boil';
        }
    });
}

// loops over all of the hops in a hop schedule and inserts them into the page
function display_grain_bill() {
    $.get(STATIC_URL + 'grain_entry.htm', function(template) {
        _.each(recipe_dict.grain_bill, function(grain) {
            var $tpl = $('<div />').html(template); // make detached DOM node
            fill_grain_template(grain, $tpl);
            $('#fermentable_container').append($tpl.html());
        });
    });
}

// fills a yeast_entry template
function fill_yeast_template(yeast, $template) {
    $template.find('#yeast_name').append(yeast.name);
    $template.find('#flocculation').append(yeast.flocculation);
    $template.find('#attenuation').append(yeast.attenuation);
}

// loops over all of the hops in a hop schedule and inserts them into the page
function display_yeast() {
    $.get(STATIC_URL + 'yeast_entry.htm', function(template) {
        var $tpl = $('<div />').html(template); // make detached DOM node
        fill_yeast_template(recipe_dict.yeast, $tpl);
        $('#yeast_container').append($tpl.html());
    });
}

function fill_misc_template(misc, $template) {
    $template.find('#misc_name').append(misc.name);
    $template.find('#misc_desc').append(misc.description);
}

function display_misc() {
    $.get(STATIC_URL + 'misc_entry.htm', function(template) {
        var $tpl = $('<div />').html(template); // make detached DOM node
        fill_misc_template(recipe_dict.misc, $tpl);
        $('#misc_container').append($tpl.html());
    });
}

function fill_comment_template(comm, $template) {
    $template.find('#username').append(comm.username);
    $template.find('#comment_text').append(comm.comment_text);
}

function display_comments() {
    $.get(STATIC_URL + 'comment_entry.htm', function(template) {
        $.each(recipe_dict.comments, function(i, comment) {
            var $tpl = $('<div />').html(template); // make detached DOM node
            fill_comment_template(comment, $tpl);
            $('#comment_entry_container').append($tpl.html());
        });
    });
}

function display_stats() {
    var og = calc_og();
    var ibu = calc_ibu();
    var color = calc_color();

    $('#og span').append(og);
    $('#ibu span').append(ibu);
    $('#color span').append(color);
}

// Malt SG = (Malt weight) x (Malt ppg) x (Brewhouse efficiency) / (Solution Volume)
function calc_og() {
    var og = 0.0;
    var SG = 0;
    _.each(recipe_dict.grain_bill, function(grain) {
        var pts = grain.potential_extract.slice(-2);
        var tmp = parseFloat(grain.amount) * parseInt(pts) * 0.75 / 5.5;
        SG += tmp;
    });
    if (SG < 100) {
        og = "1.0" + Math.round(SG);
    } else {
        og = "1." + Math.round(SG);
    }      
    return og;
}

function hop_util(time) {
    switch(time) {
        case 90: return 0.226;
        case 80: return 0.222;
        case 70: return 0.218;
        case 60: return 0.211;
        case 55: return 0.206;
        case 50: return 0.200;
        case 45: return 0.194;
        case 40: return 0.185;
        case 35: return 0.175;
        case 30: return 0.162;
        case 25: return 0.147;
        case 20: return 0.128;
        case 15: return 0.105;
        case 10: return 0.076;
        case 5:  return 0.042;
        case 0:  return 0.000;
    }
}

function calc_ibu() {
    var ibu = 0;
    _.each(recipe_dict.hop_schedule, function(hop) {
        var tmp = hop.amount * hop.alpha_acid * hop_util(hop.time) * 75 / 5.5;
        ibu += tmp;
    });
    return Math.round(ibu);
}

function calc_color() {
    var color = 0;
    _.each(recipe_dict.grain_bill, function(grain) {
        var tmp = grain.amount * grain.color / 5.5;
        color = 1.4922 * Math.pow(tmp, 0.6859);
    });
    return Math.round(color);
}

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
