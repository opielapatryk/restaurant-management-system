def update_dish_qt(repo,updated_dish,dish_id,session_id):
    return repo.put(updated_dish,dish_id,session_id)