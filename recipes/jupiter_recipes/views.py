from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import Ingredient, Recipe, User
from .serializers import RecipeSerializer, IngredientSerializer
from django.http.response import JsonResponse
import requests

@api_view(['GET'])
def recipe_get(request, username):
    # Get all recipes created by a specific user
    if request.method == 'GET':
        user = User.objects.get(username=username)
        recipes = Recipe.objects.filter(user=user)
        recipes_serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(recipes_serializer.data, safe=False)


@api_view(['POST', 'GET'])
def recipe_create(request):
    # Get all Recipes created by the currently logged in user
    if request.method == 'GET':
        recipes = Recipe.objects.filter(user=request.user)
        recipes_serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(recipes_serializer.data, safe=False)

    # Create a new recipe with the currently logged in user
    elif request.method == 'POST':
        new_recipe = Recipe.objects.create(name=request.data.get('name'), user=request.user)
        for ingredient in request.data.get('ingredients'):
            quantity = ingredient.get('quantity')
            name = ingredient.get('name')
            product_id = ingredient.get('product_id')
            Ingredient.objects.create(name=name, quantity=quantity, recipe=new_recipe, product_id=product_id)

        return JsonResponse({})

@api_view(['GET'])
def product_get(request, keyword):
    # Query the Jupiter database for products matching the keyword specified. 
    query = "{search(query: \"" + keyword + "\", page: 1) {name productId{value}}}"
    url = 'https://graphql.jupiter.co'
    r = requests.post(url, json={'query': query})

    return JsonResponse(r.json())



        

