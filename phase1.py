import requests

base_url = "https://challenge.crossmint.io/api/polyanets"

candidate_id = "12d5280f-883a-4ed9-a819-53f2ba361bae"

coordinates = [
    (2, 2), (2, 8),
    (3, 3), (3, 7),
    (4, 4), (4, 6),
    (5, 5),
    (6, 4), (6, 6),
    (7, 3), (7, 7),
    (8, 2), (8, 8)
]

def create_polyanet(row, column):
    url = base_url
    data = {
        "row": row,
        "column": column,
        "candidateId": candidate_id
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Created at: ({row}, {column})")
    else:
        print(f"Failed to create: ({row}, {column})")

for row, column in coordinates:
    create_polyanet(row, column)
