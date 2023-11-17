*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset App And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Credentials
    Register Should Fail With Message  Password is valid but username is too short


Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalleeee
    Set Password Confirmation  kalleeee
    Submit Credentials
    Register Should Fail With Message  Username is valid but password can't contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle12345
    Submit Credentials
    Register Should Fail With Message  Password doesn't match to password confirmation

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}