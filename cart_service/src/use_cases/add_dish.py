def add_dish(repo,dish,session_id):
    return repo.post(dish,session_id)