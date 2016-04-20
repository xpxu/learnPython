from jsonschema import validate

myschema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Product",
    "description": "A product from Acme's catalog",
    "type": "object",
    "properties": {
        "id": {
            "description": "The unique identifier for a product",
            "type": "integer"
        },
        "name": {
            "description": "Name of the product",
            "type": "string"
        },
        "price": {
            "type": "number",
            "minimum": 0,
            "exclusiveMinimum": True
        }
    },
    "required": ["id", "name", "price"]
}

myjson = {
    "id": 2,
#    "name": "An ice sculpture",
    "price": 12.50,
}

validate(myjson, myschema)
