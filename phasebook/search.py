from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return {"users": search_users(request.args)}, 200

def search_users(args):
    """Search users database

    Parameters:
        args: a MultiDict containing the search parameters from request.args

    Returns:
        a list of users that match the search parameters
    """

    
    search_id = args.get('id')
    search_name = args.get('name', '').lower()
    search_age = args.get('Age')
    search_occupation = args.get('occupation', '').lower()

   
    if search_age is not None:
        search_age = int(search_age)

    matched_users = []

    for user in USERS:
        if search_id and user['id'] == search_id:
            matched_users.append(user)
            continue

        if search_age is not None and search_age - 1 <= user['age'] <= search_age + 1:
            matched_users.append(user)
            continue

        if search_name and search_name in user['name'].lower():
            matched_users.append(user)
            continue

        if search_occupation and search_occupation in user['occupation'].lower():
            matched_users.append(user)
            continue

   
    matched_users = list({user['id']: user for user in matched_users}.values())

    return matched_users
