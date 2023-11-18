*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  sami
    Set Password  sami1234
    Submit Login Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  sami
    Set Password  sami4567
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  paavo
    Set Password  kalle123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Create User And Go To Login Page
    Create User  sami  sami1234
    Go To Login Page
    Login Page Should Be Open
