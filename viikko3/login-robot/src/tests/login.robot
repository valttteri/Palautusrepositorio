*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials    kalle    kalle321
    Output Should Contain    Invalid username or password

Login With Nonexistent Username
    Input Credentials    ville    ville123
    Output Should Contain    Invalid username or password

