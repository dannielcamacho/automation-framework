import requests


def test_mercadolibre_departments():
    response = requests.get(
        "https://www.mercadolibre.com.ar/menu/departments"
    )

    assert response.status_code == 200

    data = response.json()

    assert "departments" in data
    assert len(data["departments"]) > 0
