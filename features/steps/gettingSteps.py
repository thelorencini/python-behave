# pylint: disable=no-name-in-module
from behave import given, when, then
from wheel.signatures import assertTrue
from selenium.webdriver.common.by import By

menu = '//div[@class="sphinxsidebar"]/div/ul/li'

@when(u'eu acessar a página "{navigation}"')
def step_impl(context, navigation):
    print('teste')
    print('chegou menu_navigation')
    elements = context.driver.find_elements(
        By.XPATH, menu)

    print('elementos : ')
    print(elements)

    for item in elements:
        print('item texto : ')
        print(item.text)
        if navigation in item.text:
            item.click()
        break


@then(u'devo encontrar a palavra "{word}"')
def step_impl(context, word):
    assertTrue(word in context.driver.page_source)


@then(u'verificar se a palavra "{word}" possui caracteres repetidos')
def step_impl(context, word):
    caracters = []
    for item in list(word):
        if word.count(item) > 1:
            if(item not in caracters):
                caracters.append(item)

    for item in caracters:
        print('O caracter ' + item + ' possui mais de uma ocorrencia na string ' + word)










