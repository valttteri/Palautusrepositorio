*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input New Command
    Input  new

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
