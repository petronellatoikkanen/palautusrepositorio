*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testi  testi123
    Output Should Contain  New user registered
    
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists
    
Register With Too Short Username And Valid Password
    Input Credentials  te  testi123
    Output Should Contain  Username is too short
    
Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  testi1  testi123
    Output Should Contain  Username can only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  testi  testi12
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testi  testites
    Output Should Contain  Password can't only contain letters a-z

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123

Submit Credentials
    Click Button  Register

