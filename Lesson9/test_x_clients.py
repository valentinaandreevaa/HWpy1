import pytest
from Lesson9.Employee import Employer
from Lesson9.DataBase import DataBase


api = Employer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")



def test_get_list_of_employers():
    db.create_company_db('Valentina testers', 'cool_company')
    
    max_id = db.get_max_id()
    print(max_id)
    
    db.db_create_employer(max_id, "Valentina", "Andreeva", 8002000600)
   
    db_employer_list = db.db_get_list_employer(max_id)
    
    api_employer_list = api.get_list(max_id)
    
    assert len(db_employer_list) == len(api_employer_list)
   
    db.delete_company(max_id)



def test_add_new_employer():
    db.create_company_db('Valentina adding new employer', 'employer')
    max_id = db.get_max_id()
    db.db_create_employer(max_id, "Valentina", "Andreeva", 8002000600)
    resp = api.get_list(max_id)
    employer_id = resp[0]["id"]
    
    assert resp[0]["companyId"] == max_id
    
    assert resp[0]["firstName"] == "Valentina"
    
    assert resp[0]["isActive"] == True
    
    assert resp[0]["lastName"] == "Andreeva"
    
    db.db_delete_employer(employer_id)
    
    db.delete_company(max_id)



def test_get_employer_by_id():
    db.create_company_db('Employer get id company', 'new')
    max_id = db.get_max_id()
    db.db_create_employer(max_id, "Valentina", "Andreeva", 8002000600)
    employer_id = db.db_get_employer_id(max_id)
    
    get_info = api.get_info(employer_id).json()
    assert get_info["firstName"] == "Valentina"
    assert get_info["lastName"] == "Andreeva"
    
    db.db_delete_employer(employer_id)
    
    db.delete_company(max_id)



def test_update_user_info():
    db.create_company_db('New updating company', 'test')
    max_id = db.get_max_id()
    db.db_create_employer(max_id, "Valentina", "Andreeva", 8002000600)
    employer_id = db.db_get_employer_id(max_id)
    db.update_employer_info("Valya", employer_id)
    
    get_info = api.get_info(employer_id).json()
    assert get_info["firstName"] == "Valya"
    assert get_info["lastName"] == "Andreeva"
    assert get_info["isActive"] == True
    
    db.db_delete_employer(employer_id)
    
    db.delete_company(max_id)


