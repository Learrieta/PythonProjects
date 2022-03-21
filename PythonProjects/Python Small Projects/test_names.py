from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():

    assert make_full_name("Betty", "Brown") == "Brown; Betty"
    assert make_full_name("Luis", "Hidalgo") == "Hidalgo; Luis"
    assert make_full_name("Giancarlo", "Lapadula") == "Lapadula; Giancarlo"
    assert make_full_name("","") == "; "


def test_extract_family_name():
     assert extract_family_name("Brown; Betty") == "Brown"
     assert extract_family_name("Hidalgo; Luis") == "Hidalgo"
     assert extract_family_name("Lapadula; Giancarlo") == "Lapadula"
     assert extract_family_name("; ") == ""



def test_extract_given_name():
     assert extract_given_name("Brown; Betty") == "Betty"
     assert extract_given_name("Hidalgo; Luis") == "Luis"
     assert extract_given_name("Lapadula; Giancarlo") == "Giancarlo"
     assert extract_given_name("; ") == ""

pytest.main(["-v", "--tb=line", "-rN", __file__])