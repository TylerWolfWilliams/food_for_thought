from django import template
from django.urls import reverse

from recipes.models import Recipe

register = template.Library()

@register.inclusion_tag('recipes/confirm.html')
def confirm_account_deletion():
    return {"button_message": "Delete Account", "message": "delete your account", "action": reverse('recipes:delete_account'), "modal_id": "accountDeletionModal"}

@register.inclusion_tag('recipes/confirm.html')
def confirm_recipe_deletion(recipe):
    return {"button_message": "Delete Recipe", "message": f"delete the recipe titled \"{recipe.title}\"", "action": reverse('recipes:delete_recipe', args=[recipe.id]), "modal_id": f"recipeDeletionModal{recipe.id}"}

@register.inclusion_tag('recipes/confirm.html')
def confirm_review_deletion(review):
    return {"button_message": "Delete Review", "message": f"delete your review for \"{review.recipe.title}\"", "action": reverse('recipes:delete_review', args=[review.id]), "modal_id": f"reviewDeletionModal{review.id}"}

@register.inclusion_tag('recipes/confirm.html')
def confirm_recipe_unsave(recipe):
    return {"button_message": "Unsave", "message": f"unsave recipe \"{recipe.title}\"", "action": reverse('recipes:unsave_recipe', args=[recipe.id]), "modal_id": f"recipeUnsaveModal{recipe.id}"}

@register.inclusion_tag('recipes/recipe_card.html')
def recipe_card(recipe, user):
    return {"recipe": recipe, "user": user}

@register.inclusion_tag('recipes/category_card.html')
def category_card(category):
    return {"category": category}

@register.inclusion_tag('recipes/card_grid.html')
def categories_grid(categories):
    return {"cards": categories, "categories": True}
    
@register.inclusion_tag('recipes/card_grid.html')
def recipes_grid(recipes, user):
    return {"cards": recipes, "user": user}
