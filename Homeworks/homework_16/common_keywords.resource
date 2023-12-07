*** Settings ***
Library           SeleniumLibrary
Library	          Screenshot


*** Keywords ***
Open Browser Test
    [Tags]    Screenshot
    Open Browser    ${BASE_URL}    ${BROWSER}

Log In
    [Tags]    Screenshot
    Open Login Modal
    User Registration
    Login Test

Common Suite
    [Tags]    Screenshot
    Open Browser Test
    Log In

Open Login Modal
    [Tags]    Screenshot
    Wait Until Element Is Visible    id=login2
    Click Element    id=login2
    Wait Until Element Is Visible    id=logInModalLabel

User Registration
    [Tags]    Screenshot
    Wait Until Element Is Visible    id=loginusername
    Wait Until Element Is Visible    id=loginpassword
    Input Text    id=loginusername    ${USERNAME}
    Input Text    id=loginpassword    ${PASSWORD}
    Click Element    xpath=//button[@type='button' and contains(@onclick, 'logIn') and contains(@class, 'btn-primary')]

Login Test
    [Tags]    Screenshot
    Wait Until Element Is Visible    xpath=//a[@id='logout2' and text()='Log out']
    Wait Until Page Contains Element    xpath=//a[@id='nameofuser' and contains(text(),'Welcome ${USERNAME}')]

Click on Monitors Category
    [Tags]    Screenshot
    Click Element    xpath=//a[@onclick="byCat('monitor')"]

Click on Product with Highest Price
    [Tags]    Screenshot
    Wait Until Page Contains Element    xpath=//a[@href="prod.html?idp_=10" and contains(text(),'Apple monitor 24')]
    Click Element    xpath=//a[@href="prod.html?idp_=10" and contains(@class, "hrefch")]


Verify Product Name
    [Tags]    Screenshot
    [Arguments]    ${expected_text}
    Wait Until Page Contains Element    xpath=//h2[@class="name" and contains(text(),"${expected_text}")]    timeout=10s
    [Return]    ${expected_text} in page source

Verify Product Price
    [Tags]    Screenshot
    [Arguments]    ${expected_text}
    Wait Until Page Contains Element    xpath=//h3[@class="price-container" and contains(text(),"${expected_text}")]    timeout=10s
    [Return]    ${expected_text} in page source


Add Product
    [Tags]    Screenshot
    Wait Until Location Contains    https://www.demoblaze.com/prod.html?idp_=10    timeout=10s
    Wait Until Element Is Visible    xpath=//img[@src='imgs/apple_cinema.jpg']     timeout=10s
    Click Element    xpath=//a[contains(@onclick, "addToCart(10)")]
    Sleep    5s
    ${alert_occurred} =    Run Keyword And Return Status    Handle Alert    action=accept
    Run Keyword If    ${alert_occurred}    Log    Alert occurred
    Wait Until Element Is Visible    xpath=//img[@src='imgs/apple_cinema.jpg']     timeout=10s


Click on Cart
    [Tags]    Screenshot
    Click Element    id=cartur
    Wait Until Location Contains    https://www.demoblaze.com/cart.html    timeout=10s
    Sleep    5s


Verify Added Product
    [Tags]    Screenshot
    [Arguments]    ${expected_name}    ${expected_price}
    Wait Until Element Is Visible    xpath=//tr[@class='success']//td[contains(text(), 'Apple monitor 24')]    timeout=10s
    Wait Until Element Is Visible    xpath=//tr[@class='success']//td[contains(text(), '400')]    timeout=10s
    Wait Until Element Is Visible    xpath=//a[contains(@onclick, 'deleteItem')]    timeout=20s
    Run Keyword If    not Verify Product Name    ${expected_name}
    Run Keyword If    not Verify Product Price    ${expected_price}
    [Return]    ${expected_name} and ${expected_price} in page source