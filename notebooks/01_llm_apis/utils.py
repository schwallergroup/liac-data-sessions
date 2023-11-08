import requests
from IPython.core.display import HTML
from IPython.display import display


def cdk(smiles):
    """
    Get a depiction of some smiles.
    """
    
    url = "http://liacpc11.epfl.ch:8081/depict/bot/svg"
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        url,
        headers=headers,
        params={
            "smi": smiles,
            "annotate": "colmap",
            "zoom": 2,
            "w": 250,
            "h": 50,
            "abbr": "off",
        }
    )

    display(HTML(response.text))
    