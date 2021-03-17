import sys
sys.path.append(".")

import pytest
import app.modules.MerchantsGuide as mg
import app.app_creator as tests_setup

test_configs = {}
app_instance = tests_setup.get_new_app_instance(test_configs)
merchantsGuide = mg.MerchantsGuide()

@pytest.fixture
def client():
    app_instance.config['TESTING'] = True
    client = app_instance.test_client()
    return client


def test_is_valid_unit():
    isUnit = merchantsGuide.is_valid_unit('prok')
    assert isUnit is True


def test_is_not_a_valid_unit():
    isUnit = merchantsGuide.is_valid_unit('xoxo')
    assert isUnit is False


def test_is_valid_dialect():
    isUnit = merchantsGuide.is_valid_dialect('pish prok Gold')
    assert isUnit is True


def test_is_invalid_dialect():
    isUnit = merchantsGuide.is_valid_dialect('foo prok Gold')
    assert isUnit is False


def test_get_roman_value():
    isUnit = merchantsGuide.get_roman_value('V')
    assert isUnit == 5

    isUnit = merchantsGuide.get_roman_value('VI')
    assert isUnit == 6

    isUnit = merchantsGuide.get_roman_value('IV')
    assert isUnit == 4
