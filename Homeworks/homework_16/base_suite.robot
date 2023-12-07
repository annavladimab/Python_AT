*** Settings ***
Variables         variabels.py
Resource          common_keywords.resource
Test Teardown    Close Browser
Library           SeleniumLibrary


*** Test Cases ***
User Registration and Login Test
    [Setup]   Open Browser Test
    Log In

Product Category Test
    [Setup]   Common Suite
    Click on Monitors Category
    Click on Product with Highest Price
    ${product_verification} =    Run Keyword And Return Status    Verify Product Name    ${PRODUCT_NAME}
    Run Keyword If    ${product_verification}    Log    Product verification failed!
    ${product_verification2} =    Run Keyword And Return Status    Verify Product Price    ${PRODUCT_PRICE}
    Run Keyword If    ${product_verification2}    Log    Product verification failed!
    Add product
    Click on Cart
    ${added_product_verification} =    Run Keyword And Return Status    Verify Added Product    ${PRODUCT_NAME}    ${ADDED_PRODUCT_PRICE}
    Run Keyword If    ${added_product_verification}    Log    Product verification failed!
