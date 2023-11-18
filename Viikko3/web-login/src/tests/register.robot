*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register New User Page And Check If On It

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Fail With Message  Username needs to be longer than 2 characters

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  hilavitkutin
    Set Password Confirmation  hilavitkutin
    Submit Credentials
    Registration Should Fail With Message  Password must include characters other than a to z

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Credentials
    Registration Should Fail With Message  Password does not match the password confirmation

Login After Successful Registration
    Set Username  jakke
    Set Password  jakke123
    Set Password Confirmation  jakke123
    Submit Credentials
    Registration Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  jakke
    Set Password  jakke123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  eionnistu
    Set Password  hilavitkutin
    Set Password Confirmation  hilavitkutin
    Submit Credentials
    Registration Should Fail With Message  Password must include characters other than a to z
    Go To Login Page
    Login Page Should Be Open
    Set Username  eionnistu
    Set Password  hilavitkutin
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Registration Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

Go To Register New User Page And Check If On It
    Go To Register Page
    Register Page Should Be Open