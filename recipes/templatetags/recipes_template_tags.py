from django import template
from django.urls import reverse

from recipes.models import Recipe

register = template.Library()

@register.inclusion_tag('recipes/confirm.html')
def confirm_account_deletion():
    return {"button_message": "Delete Account",
            "message": "delete your account",
            "action": f"location.href = '{reverse('recipes:delete_account')}'",
            "modal_id": "accountDeletionModal"}

@register.inclusion_tag('recipes/confirm.html')
def confirm_recipe_deletion(recipe, ajax=True):
    url = f"('{reverse('recipes:delete_recipe', args=[recipe.id])}')"
    if not ajax:
        action = f"location.href = {url}"
    else:
        action = f"ajaxHelper('{url}')" 


    return {"button_message": "Delete Recipe",
            "message": f"delete the recipe titled \"{recipe.title}\"",
            "action": action,
            "modal_id": f"recipeDeletionModal{recipe.id}"}

@register.inclusion_tag('recipes/confirm.html')
def confirm_review_deletion(review):
    return {"button_message": "Delete Review",
            "message": f"delete your review for \"{review.recipe.title}\"",
            "action": f"ajaxHelper('{reverse('recipes:delete_review', args=[review.id])}')",
            "modal_id": f"reviewDeletionModal{review.id}"}
