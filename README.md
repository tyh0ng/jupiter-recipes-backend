# jupiter-recipes-backend

Backend for the Jupiter Recipes take home challenge using Django REST framework.

## Steps:
1. Activate virtual environment (in folder with `env`): `source env/bin/activate`
2. Start the local server (in folder with `manage.py`): python3 manage.py runserver

## URLS:
1. `recipes/<username>/`: `GET` request will get all recipes created by the specified user.
2. `recipes/`: `GET` request will get all recipes created by the currently logged in user. `POST` request will create a new recipe. The JSON object send should be in the format: `{"name": <recipe_name>, "ingredients": [{"quantity": <ingredient_quantity>, "name": <ingredient_name>, "product_id": <jupiter_product_id>}]}`
3. `products/<keyword>/`: `GET` request will query `https://graphql.jupiter.co` for the keyword specified and return the first page of products found, along with their corresponding product ids.
4. `rest_auth/login/`: `POST` request will log the user in and authenticate them appropriately. JSON object should be in the format `{"username": <username>, "password": <password>}`
5. `rest_auth/logout/`: `GET`request will log the user out appropriately.
