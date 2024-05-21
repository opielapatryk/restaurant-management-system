# Local modules
from repositories.mongorepo import MongoRepo
from domain.menu.Menu import Menu

def test_repository_list_without_parameters(mg_database, mg_test_data):
    repo = MongoRepo()

    repo_menu = repo.list()

    assert repo_menu[0]['name'] == mg_test_data['name']

def test_repository_get(mg_database, mg_test_data):
    repo = MongoRepo()

    db, document_id = mg_database

    repo_menu = repo.get(document_id)

    assert repo_menu['name'] == mg_test_data['name']

def test_repository_post(mg_database, mg_test_post_data):
    repo = MongoRepo()

    repo_menu = repo.post(mg_test_post_data)

    assert repo_menu[0]['name'] == 'Polish Jadło!'
    assert repo_menu[1]['name'] == 'Polish Jadło2!'

def test_repository_put(mg_database, mg_test_post_data):
    db, document_id = mg_database
    repo = MongoRepo()

    repo_menu = repo.put(mg_test_post_data, document_id)

    assert repo_menu['Updated menu:']['name'] == 'Polish Jadło2!'

def test_repository_patch(mg_database, mg_test_post_data):
    db, document_id = mg_database
    repo = MongoRepo()

    repo_menu = repo.patch(mg_test_post_data, document_id)

    assert repo_menu['Updated menu:']['name'] == 'Polish Jadło2!'

def test_repository_delete(mg_database):
    db, document_id = mg_database
    repo = MongoRepo()

    repo.delete(document_id)

    assert len(repo.list()) == 1