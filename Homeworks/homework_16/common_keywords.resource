*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Open Browser and Log In
    Open Browser    ${BASE_URL}    ${BROWSER}
    Open Login Modal
    User Registration
    Login Test

Open Login Modal
    Sleep    20s
    Click Element    id=login2
    Wait Until Element Is Visible    id=logInModalLabel

User Registration
    Sleep    10s
    Wait Until Element Is Visible    id=loginusername
    Wait Until Element Is Visible    id=loginpassword
    Input Text    id=loginusername    ${USERNAME}
    Input Text    id=loginpassword    ${PASSWORD}
    Sleep    10s
    Click Element    xpath=//button[@type='button' and contains(@onclick, 'logIn') and contains(@class, 'btn-primary')]

Login Test
    Sleep    20s
    Wait Until Element Is Visible    xpath=//a[@id='logout2' and text()='Log out']
    Wait Until Page Contains Element    xpath=//a[@id='nameofuser' and contains(text(),'Welcome ${USERNAME}')]

Click on Monitors Category
    Sleep    10s
    Click Element    xpath=//a[@onclick="byCat('monitor')"]

Click on Product with Highest Price
    Sleep    10s
    Click Element    xpath=//a[@href="prod.html?idp_=10" and contains(@class, "hrefch")]
    Sleep    10s

Verify Product Name
    [Arguments]    ${expected_text}
    Wait Until Page Contains Element    xpath=//h2[@class="name" and contains(text(),"${expected_text}")]    timeout=10s
    [Return]    ${expected_text} in page source

Verify Product Price
    [Arguments]    ${expected_text}
    Wait Until Page Contains Element    xpath=//h3[@class="price-container" and contains(text(),"${expected_text}")]    timeout=10s
    [Return]    ${expected_text} in page source

Add Product
    Sleep    10s
    Click Element    xpath=//a[contains(@onclick, "addToCart(10)")]
    Sleep    20s
    ${alert_occurred} =    Run Keyword And Return Status    Handle Alert    action=accept
    Run Keyword If    ${alert_occurred}    Log    Alert occurred
    Sleep    20s
    Click Element    id=cartur
    Sleep    20s

Verify Added Product
    [Arguments]    ${expected_name}    ${expected_price}
    Run Keyword If    not Verify Product Name    ${expected_name}
    Run Keyword If    not Verify Product Price    ${expected_price}
    [Return]    ${expected_name} and ${expected_price} in page source