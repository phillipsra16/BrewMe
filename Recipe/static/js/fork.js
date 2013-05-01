// Forked recipe
// add the recipe information to the recipe that is being designed
$(function() {
    if (recipe_dict) {
        _.each(recipe_dict.hop_schedule, function(hop) {
            recipe.hop.push(hop);
        });
        _.each(recipe_dict.grain_bill, function(grain) {
            recipe.fermentable.push(grain);
        });
        recipe.yeast = recipe_dict.yeast;
    }
});
