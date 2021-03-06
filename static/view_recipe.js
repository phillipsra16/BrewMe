// global for recipe holding
var recipe = {{ recipe_dict|safe }}; // safe gets rid of &quot

// jQuery.ready 
$(function() {
    $('#recipe_name').text(recipe.recipe_name);
    display_hop_schedule();
    display_grain_bill();
    display_yeast();
    display_misc();
    display_stats();
}); // end jQuery.ready

// fills a hop entry template
function fill_hop_template(hop, $template) {
    $template.find('#hop_name').append(hop.name);
    $template.find('#hop_time').append(hop.time);
    $template.find('#hop_alpha').append(hop.alpha_acid);
    $template.find('#hop_amount').append(hop.amount);
    $template.find('#hop_use').append(function(hop) {
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
    $.get({{ STATIC_URL }} + 'hop_entry.htm', function(template) {
        $.each(recipe.hop_schedule, function(i, hop) {
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
    $template.find('#grain_ppg').append(grain.ppg);
    $template.find('#grain_amount').append(grain.amount);
    $template.find('#grain_use').append(function(grain) {
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
    $.get({{ STATIC_URL }} + 'grain_entry.htm', function(template) {
        $.each(recipe.grain_bill, function(i, grain) {
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
    $.get({{ STATIC_URL }} + 'yeast_entry.htm', function(template) {
        var $tpl = $('<div />').html(template); // make detached DOM node
        fill_yeast_template(recipe.yeast, $tpl);
        $('#yeast_container').append($tpl.html());
    });
}

function fill_misc_template(misc, $template) {
    $template.find('#misc_name').append(misc.name);
    $template.find('#misc_desc').append(misc.description);
}

function display_misc() {
    $.get({{ STATIC_URL }} + 'misc_entry.htm', function(template) {
        var $tpl = $('<div />').html(template); // make detached DOM node
        fill_yeast_template(recipe.misc, $tpl);
        $('#misc_container').append($tpl.html());
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
    recipe.grain_bill.forEach(function(grain) {
        var pts = grain.ppg.slice(-2);
        var tmp = parseFloat(grain.amount) * parseInt(pts) * 0.75 / 5.5;
        SG += tmp;
    });
    if (og < 100) {
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
    recipe.hop_schedule.forEach(function(hop) {
        var tmp = hop.amount * hop.alpha_acid * hop_util(hop.time) * 75 / 5.5;
        ibu += tmp;
    });
    return Math.round(ibu);
}

function calc_color() {
    var color = 0;
    recipe.grain_bill.forEach(function(grain) {
        var tmp = grain.amount * grain.color / 5.5;
        color = 1.4922 * Math.pow(tmp, 0.6859);
    });
    return Math.round(color);
}

