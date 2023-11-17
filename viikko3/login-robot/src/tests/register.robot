*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    mikko    salasana123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    kalle    salasana123
    Output Should Contain    Password is valid but username is taken

Register With Too Short Username And Valid Password
    Input Credentials    ab    salasana123
    Output Should Contain    Password is valid but username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    kalle1    salasana123
    Output Should Contain    Password is valid but username can only contain letters

Register With Valid Username And Too Short Password
    Input Credentials    mikko    sala1
    Output Should Contain    Username is valid but password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    mikko    huonosalasana
    Output Should Contain    Username is valid but password can't only contain letters