from include.datasets import DATASET_COCKTAIL
from airflow.exceptions import AirflowFailException


def _get_cocktail(ti=None):
    import requests
    from airflow.models import Variable

    api = Variable.get('api')
    # api = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    
    response = requests.get(api)
    with open(DATASET_COCKTAIL.uri, "wb") as f:
        f.write(response.content)
    ti.xcom_push(key='request_size', value=len(response.content))

def _check_size(ti=None):
    size = ti.xcom_pull(key='request_size', task_ids='get_cocktail')
    print(size)
    if size <= 0:
        raise AirflowFailException  # simulate failed task
    
def _validate_cocktail_fields():
    """Validate that the cocktail JSON data has the expected structure."""
    import json
    
    required_fields = {
        'drinks': [
            'idDrink', 'strDrink', 'strDrinkAlternate', 'strTags', 'strVideo',
            'strCategory', 'strIBA', 'strAlcoholic', 'strGlass', 'strInstructions',
            'strInstructionsES', 'strInstructionsDE', 'strInstructionsFR',
            'strInstructionsIT', 'strInstructionsZH-HANS', 'strInstructionsZH-HANT',
            'strDrinkThumb'
        ] + [f'strIngredient{i}' for i in range(1, 16)] 
          + [f'strMeasure{i}' for i in range(1, 16)]
          + ['strImageSource', 'strImageAttribution', 'strCreativeCommonsConfirmed', 'dateModified']
    }
    
    with open(DATASET_COCKTAIL.uri, 'r') as f:
        data = json.load(f)
    
    if not isinstance(data, dict) or 'drinks' not in data:
        raise ValueError("JSON must have a 'drinks' array")
    
    if not isinstance(data['drinks'], list) or not data['drinks']:
        raise ValueError("'drinks' must be a non-empty array")
        
    drink = data['drinks'][0]
    missing_fields = [field for field in required_fields['drinks'] 
                     if field not in drink]
    
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

def _check_json_fields(ti=None):
    import json
    import os

    expected_fields = [
        "idDrink",
        "strDrink",
        "strDrinkAlternate",
        "strTags",
        "strVideo",
        "strCategory",
        "strIBA",
        "strAlcoholic",
        "strGlass",
        "strInstructions",
        "strInstructionsES",
        "strInstructionsDE",
        "strInstructionsFR",
        "strInstructionsIT",
        "strInstructionsZH-HANS",
        "strInstructionsZH-HANT",
        "strDrinkThumb",
        # ingredients 1..15
    ]
    # add ingredient and measure fields
    for i in range(1, 16):
        expected_fields.append(f"strIngredient{i}")
    for i in range(1, 16):
        expected_fields.append(f"strMeasure{i}")

    expected_fields += ["strImageSource", "strImageAttribution", "strCreativeCommonsConfirmed", "dateModified"]

    dataset_path = getattr(DATASET_COCKTAIL, "uri", None)
    if not dataset_path or not os.path.exists(dataset_path):
        raise AirflowFailException(f"Dataset file not found: {dataset_path}")

    with open(dataset_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "drinks" not in data or not isinstance(data["drinks"], list) or len(data["drinks"]) == 0:
        raise AirflowFailException("Invalid or empty 'drinks' in dataset JSON")

    first = data["drinks"][0]
    missing = [k for k in expected_fields if k not in first]
    if missing:
        raise AirflowFailException(f"Missing expected fields in cocktail JSON: {missing}")