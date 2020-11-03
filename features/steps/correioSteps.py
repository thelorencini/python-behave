# pylint: disable=no-name-in-module
from telnetlib import EC

from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from wheel.signatures import assertTrue
from selenium.webdriver.common.by import By


field_cep = '//div[@class="contentform"]/span/label/input'
button_buscar = '//div[@class="btnform"]/input'
message = '//div[@class="ctrlcontent"]'

@when(u'eu realizar a busca pelo cep "{cep}"')
def step_impl(context, cep):
     context.driver.find_element_by_xpath(field_cep).send_keys(cep)
     context.driver.find_element_by_xpath(button_buscar).click()




@then(u'página apresentará a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    elements = context.driver.find_element(
        By.XPATH, message)
    if(mensagem not in elements.text):
        raise Exception('Mensagem não encontrada no site, ' + mensagem)




