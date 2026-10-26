import requests
import json
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_weather_data(url:str) -> list:
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        logging.error(
            "Request Error - Status: %s - Resposta: %s",
            response.status_code,
            response.text[:300]
            )
        return []

    if not data:
        logging.warn("No data found")
        return []

    output_path = 'data/weather_data.json'
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f"File saved to {output_path}")
    return data 


