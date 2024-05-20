from repositories.mongorepo import MongoRepo

def test_repository_list_without_parameters(mg_database, mg_test_data):
    repo = MongoRepo()

    repo_menu = repo.list()

    assert repo_menu['name'] == mg_test_data['name']