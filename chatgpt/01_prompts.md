#### Prompts

- Explain code behind the API to GET Product By ID
- Explain the code structure
- Create a new API endpoint for Orders: Get Orders and Create Order and do not forget the swagger on the views
    - continue in this: Next, create the views for Orders inside the api/order_management/orders/views.py directory:
- Create a new endpoint for getting, updating, patching, and deleting a single order
- Document the api for getting products based on the code that Ive provided



#### Commands for Generating this chatgpt context
```
tree -d -L 2 -I "*.pyc|__pycache__|venv" -P "*api*|*domain*|*project*"
```

### Better Prompts
- Create a new Order Models following this code pattern: <Paste the code for all the models as the code pattern>
- Create a new Order Services following this code pattern: <Paste the code for all the services as the code pattern>
- Create a new Order API following this code pattern: <Paste the code for all the API Endpoints and Serializers>