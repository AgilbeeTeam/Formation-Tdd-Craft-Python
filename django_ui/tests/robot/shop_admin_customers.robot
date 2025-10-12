*** Settings ***
Library           SeleniumLibrary
Library           Process
Library           OperatingSystem
Suite Setup       Load Fixture Data
Suite Teardown    Flush Database
Test Setup        Open Admin Customers Page
Test Teardown     Close All Browsers

*** Variables ***
${PROJECT_DIR}             ${CURDIR}/../..                 # ajustez selon votre arborescence
#${PROJECT_DIR}             ${CURDIR}                # ajustez selon votre arborescence
${CWD}                     ${CURDIR}
${MANAGE_PY}               ${PROJECT_DIR}/manage.py
${FIXTURE_PATH}            ${PROJECT_DIR}/tests/fixtures/clients.json
${BASE_URL}                http://127.0.0.1:8000
${ADMIN_CUSTOMERS_URL}     ${BASE_URL}/shop_admin/clients/
${BROWSER}                 chrome
${TIMEOUT}                 5s


${CLIENT_FR_NAME}          Jean Dupont
${CLIENT_FR_ADDR}          10 rue de la Paix, Paris, France
${CLIENT_CA_NAME}          Marie Tremblay
${CLIENT_CA_ADDR}          123 Rue Sainte-Catherine, Montréal, QC, Canada
${CLIENT_US_NAME}          John Smith
${CLIENT_US_ADDR}          45 Wall Street, New York, NY, USA

*** Keywords ***
Run Python Process
    [Arguments]    ${args_1}  ${args_2}

    Run Process    python    ${MANAGE_PY}   ${args_1}  ${args_2}    cwd=${CWD}    stdout=${CWD}/out.log    stderr=${CWD}/err.log    timeout=120s

Load Fixture Data
    # Base propre puis chargement de la fixture
    Run Python Process    flush  --noinput
    Run Python Process    loaddata   ${FIXTURE_PATH}

Flush Database
    Run Python Process    flush  --noinput

Open Admin Customers Page
    Open Browser    ${ADMIN_CUSTOMERS_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    ${TIMEOUT}
    Wait Until Page Contains Element    css:table.customers-table    timeout=10s

Row Text Should Contain
    [Arguments]    ${name}    ${expected}
    ${row}=    Set Variable    xpath=//table[contains(@class,'customers-table')]//tr[td[contains(., "${name}")]]
    Wait Until Element Is Visible    ${row}    timeout=5s
    ${text}=    Get Text    ${row}
    Should Contain    ${text}    ${expected}

*** Test Cases ***
Admin Customers Lists Three Buyers With Totals And Cart State
    [Documentation]    Vérifie noms, adresses, total US=30,00 et panier Plein/Vide.
    # Noms + adresses
    Row Text Should Contain    ${CLIENT_FR_NAME}    ${CLIENT_FR_ADDR}
    Row Text Should Contain    ${CLIENT_CA_NAME}    ${CLIENT_CA_ADDR}
    Row Text Should Contain    ${CLIENT_US_NAME}    ${CLIENT_US_ADDR}

    # Total US = 30.00 € (tolère , ou . selon formatage)
    ${us_row}=    Set Variable    xpath=//table[contains(@class,'customers-table')]//tr[td[contains(., "${CLIENT_US_NAME}")]]
    ${us_text}=   Get Text      ${us_row}
    Should Match Regexp         ${us_text}    .*30[.,]00.*

    # Panier CA = Plein
    ${ca_row}=    Set Variable    xpath=//table[contains(@class,'customers-table')]//tr[td[contains(., "${CLIENT_CA_NAME}")]]
    ${ca_text}=   Get Text        ${ca_row}
    Should Contain                ${ca_text}    Plein

    # Panier FR = Vide
    ${fr_row}=    Set Variable    xpath=//table[contains(@class,'customers-table')]//tr[td[contains(., "${CLIENT_FR_NAME}")]]
    ${fr_text}=   Get Text        ${fr_row}
    Should Contain                ${fr_text}    Vide