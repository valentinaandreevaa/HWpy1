from Lesson7.Shopmain import ShopmainPage
from Lesson7.Shopcontainer import ShopContainer



def test_shop(chrome_browser):
    expected_total = "58.29"
    
    shopmain = ShopmainPage(chrome_browser)
        
    shopmain.registration_fields()
      
    shopmain.buy_issue()
     
    shopmain.click_issue()
    
    shopmain.into_container()
    container = ShopContainer(chrome_browser)
    
    
    container.checkout()
    
    container.info()
    
    container.price()
    
    assert expected_total in container.price() 
    print("Итоговая сумма равна $58.29")  