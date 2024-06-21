from flask import Blueprint, request

from .data.search_data import USERS

# Define a Blueprint for search-related routes
bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return {"users": search_users(request.args.to_dict())}, 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Extract search parameters from the args dictionary
    search_id = args.get('id')
    search_name = args.get('name', '').lower()
    search_age = args.get('age')
    search_occupation = args.get('occupation', '').lower()

    # Convert search_age to an integer if it exists
    if search_age is not None:
        search_age = int(search_age)

    matched_users = []

    for user in USERS:
        if search_id and user['id'] == search_id:
            matched_users.append(user)
            continue

        if search_name and search_name in user['name'].lower():
            matched_users.append(user)
            continue

        if search_age and search_age - 1 <= user['age'] <= search_age + 1:
            matched_users.append(user)
            continue

        if search_occupation and search_occupation in user['occupation'].lower():
            matched_users.append(user)
            continue

    # Ensure unique results
    matched_users = {user['id']: user for user in matched_users}.values()

    return list(matched_users)
