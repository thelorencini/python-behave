# pylint: disable=no-name-in-module
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('que entrei no site do "{pagina}"')
def step_impl(context, pagina):
    page = ''
    if(pagina == 'Selenium Python'):
        page = 'https://selenium-python.readthedocs.io/'
    elif(pagina == 'Correios'):
        page = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaCepEndereco.cfm'
    else:
        raise Exception('Site não identificado')
    context.driver.get(page)






