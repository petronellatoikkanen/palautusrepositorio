*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Register Credentials
    Register Should Succeed
    
Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Register Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Set Username  testi
    Set Password  testites
    Set Password Confirmation  testites
    Submit Register Credentials
    Register Should Fail With Message  Password can't only contain letters a-z

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi456
    Submit Register Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  testitesti
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Register Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  testitesti
    Set Password  testi123
    Click Button  Login
    Login Should Succeed
	
Login After Failed Registration
    Set Username  te
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Register Credentials
    Register Should Fail With Message  Username is too short
    Click Link  Login
    Set Username  te
    Set Password  testi123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password
    
*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open
    
Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    
Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Login Should Succeed
    Main Page Should Be Open
    
Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}


