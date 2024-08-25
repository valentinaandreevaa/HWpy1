import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""

def test_capytalize():
    """positive"""
    assert utils.capitilize("hello world") == "Hello world"
    assert utils.capitilize("2201") == "2201"
    """negative"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("123qwerty") == "123qwerty"

@pytest.mark.parametrize("input_string, expected_output", {
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("123", "123"),
        ("", ""),
        ("12345test", "12345test"),
    })
def test_capitalize(input_string, expected_output):
        assert utils.capitilize(input_string) == expected_output

"""trim"""

    
def test_trim():
        """positive"""
        assert utils.trim("  Hello") == "Hello"
        assert utils.trim(" Hello,world ") == "Hello,world "
        assert utils.trim(" HELLO ") == "HELLO "
        """negative"""
        assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
        assert utils.trim(12345) == "12345"

@pytest.mark.xfail()
def test_trim_with_numbers_input():
        assert utils.trim(" Hello ") == "   Hello "


"""to_list"""

@pytest.mark.parametrize('string, delimeter, result', [
    ("яблоко,банан,апельсин", ",", ["яблоко", "банан", "апельсин"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    ("", None, []),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


"""contains"""

@pytest.mark.parametrize('string, symbol, result', [
      
    ("банан", "б", True),
    ("гвоздь", "д", True),
    ("мир  ", "р", True),
    ("диван-кровать", "-", True),
    ("145", "1", True),
    ("", "", True),
    ("Москва", "h", False),
    ("привет", "з", False),
    ("кот", "М", False),
    ("Москва", "2", False),  
])
def test_contains(string, symbol, result):
      res = utils.contains(string, symbol)
      assert res == result

"""delete_symbol"""

@pytest.mark.parametrize('string, symbol, result', [
      
    ("слово", "с", "лово"),
    ("учеба", "у", "чеба"),
    ("домашка", "д", "омашка"),
    ("123", "1", "23"),
    ("слово", "п", "слово"),
    ("учеба", "п", "учеба"),
    ("", "", ""),
    ("", "а", "")
])
def test_delete_symbol(string, symbol, result):
      res = utils.delete_symbol(string, symbol)
      assert res == result


"""starts_with"""

@pytest.mark.parametrize('string, symbol, result', [
      
    ("слово", "с", True),
    ("учеба", "у", True),
    ("домашка", "д", True),
    ("123", "1", True),
    ("слово", "п", False),
    ("учеба", "п", False),
    ("", "3", False),
    ("", "а", False)
])
def test_starts_with(string, symbol, result):
      res = utils.starts_with(string, symbol)
      assert res == result

"""end_with"""

@pytest.mark.parametrize('string, symbol, result', [
      
    ("слово", "о", True),
    ("учеба", "а", True),
    ("домашка", "а", True),
    ("123", "3", True),
    ("слово", "п", False),
    ("учеба", "п", False),
    ("", "3", False),
    ("", "а", False)
])
def test_end_with(string, symbol, result):
      res = utils.end_with(string, symbol)
      assert res == result


"""is_empty"""

@pytest.mark.parametrize('string, result', [
      
    ("", True),
    (" ", True),
    ("  ", True),
    
    ("слово", False),
    ("уче ба", False),
    ("123", False),
])
def test_is_empty(string, result):
      res = utils.is_empty(string)
      assert res == result


"""list_to_string"""

@pytest.mark.parametrize('lst, joiner result', [
      
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["H", "e", "l", "l", "o"], ",", "H,e,l,l,o"),
    (["one", "two"], "-", "one-two"),
    
    ([], None, ""),
    ([], ",", ""),
    ([], "-", ""),
])
def list_to_string(lst, joiner, result):
      if joiner == None:
          res = utils.list_to_string(lst)
      else:
            res = utils.list_to_string(lst, joiner)
      assert res == result










        
           
