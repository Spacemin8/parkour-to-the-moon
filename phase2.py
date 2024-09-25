import requests

BASE_URL = "https://challenge.crossmint.io/api"
CANDIDATE_ID = "12d5280f-883a-4ed9-a819-53f2ba361bae"

POLYANET = 'POLYANET'
SOLOON = 'SOLOON'
COMETH = 'COMETH'
SPACE = 'SPACE'

def get_goal_map():
    response = requests.get(f"{BASE_URL}/map/{CANDIDATE_ID}/goal")
    if response.status_code == 200:
        return response.json()['goal']
    else:
        print(f"Error fetching: {response.status_code}")
        return None

def create_polyanet(row, col):
    data = {'candidateId': CANDIDATE_ID, 'row': row, 'column': col}
    response = requests.post(f"{BASE_URL}/polyanets", json=data)
    if response.status_code == 200:
        print(f"Polyanet created at: ({row}, {col}).")
    else:
        print(f"Failed to create Polyanet at: ({row}, {col}): {response.status_code}")

def create_soloon(row, col, color):
    data = {'candidateId': CANDIDATE_ID, 'row': row, 'column': col, 'color': color}
    response = requests.post(f"{BASE_URL}/soloons", json=data)
    if response.status_code == 200:
        print(f"{color} Soloon created at ({row}, {col}).")
    else:
        print(f"Failed to create Soloon at: ({row}, {col}): {response.status_code}")

def create_cometh(row, col, direction):
    data = {'candidateId': CANDIDATE_ID, 'row': row, 'column': col, 'direction': direction}
    response = requests.post(f"{BASE_URL}/comeths", json=data)
    if response.status_code == 200:
        print(f"Cometh ({direction}) created at ({row}, {col}).")
    else:
        print(f"Failed to create Cometh at: ({row}, {col}): {response.status_code}")

def build_map(goal_map):
    for row_idx, row in enumerate(goal_map):
        for col_idx, cell in enumerate(row):
            if POLYANET in cell:
                create_polyanet(row_idx, col_idx)
            elif 'SOLOON' in cell:
                color = cell.split('_')[0].lower()
                create_soloon(row_idx, col_idx, color)
            elif 'COMETH' in cell:
                direction = cell.split('_')[0].lower()
                create_cometh(row_idx, col_idx, direction)

def main():
    goal_map = get_goal_map()

    if goal_map:
        build_map(goal_map)

main()
