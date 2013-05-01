import datetime
from haystack.indexes import *
from haystack import site
from Recipe.models import Recipe

class RecipeIndex(SearchIndex):

    text        = CharField(document=True, use_template=True)
    name        = CharField(model_attr='name')
    user_name   = CharField(model_attr='user_id')
    yeast_id    = CharField(model_attr='yeast_id')
    #parent_id   = CharField(model_attr='parent_id')
    style_id    = CharField(model_attr='style_id')
    description = CharField(model_attr='description')
    url         = CharField()

    def prepare_url(self, obj):
        return "%s%d" % ("http://66.169.77.204:8001/recipe/view_recipe/", obj.id)

    def index_queryset(self):
        #Used when the entire index for this model is updated.
        return Recipe.objects.all()


site.register(Recipe, RecipeIndex)
