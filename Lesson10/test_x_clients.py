import pytest
import allure
from Lesson10.Employee import Employer
from Lesson10.DataBase import DataBase



api = Employer("https://x-clients-be.onrender.com")
db = DataBase("postgresql://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")


@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Список сотрудников")
@allure.description("Получаем список сотрудников из БД и АПИ, после чего сравниваем их")
@allure.feature('Тест 1')
def test_get_list_of_employers():
    with allure.step("БД Создаем компанию"):
        db.create_company_db('Valentina testers','cool_company')
    with allure.step("БД Получаем ID последней созданной компании"):
        max_id=db.get_max_id()    
    with allure.step("БД Добавляем сотрудника в компанию"):
        db.db_create_employer(max_id,"Valentina","Andreeva",8002000600)
    with allure.step("БД Получаем список сотрудников из последней созданной компании"):
        db_employer_list = db.db_get_list_employer(max_id)
    with allure.step("API Получаем список сотрудников из последней созданной компании"):
        api_employer_list = api.get_list(max_id)
    with allure.step("Сравниваем сотрудников БД и АПИ"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("Удаляем последнюю созданную компанию"):
        db.delete_company(max_id)


@allure.epic("X-clients")
@allure.severity(severity_level='crtical')
@allure.title("Добавление сотрудников")
@allure.description("Добавляем сотрудников в БД, сравниваем с апи имя статус и фамилию")
@allure.feature('Тест 2')
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


@allure.epic("X-clients")
@allure.severity(severity_level='trivial')
@allure.title("Получение информации о сотруднике по ID")
@allure.description("Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании сотрудника в БД")
@allure.feature('Тест 3')
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


@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Обновление информации о сотруднике")
@allure.description("Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике")
@allure.feature('Тест 4')
def test_update_user_info():
    db.create_company_db('New updating company', 'test')
    max_id = db.get_max_id()
    db.db_create_employer(max_id, "Valentina", "Andreeva", 8002000600)
    employer_id = db.db_get_employer_id(max_id)
    db.update_employer_info("Valentina", employer_id)
    
    get_info = api.get_info(employer_id).json()
    assert get_info["firstName"] == "Valentina"
    assert get_info["lastName"] == "Andreeva"
    assert get_info["isActive"] == True
    
    db.db_delete_employer(employer_id)
    db.delete_company(max_id)