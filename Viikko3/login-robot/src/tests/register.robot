*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  paavo  h1lav1tkutin
    Output Should Contain  New user registered
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists
Register With Too Short Username And Valid Password
    Input Credentials  ak  h1lav1tkutin
    Output Should Contain  Username needs to be longer than 2 characters
Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  paavo69  h1lav1tkutin
    Output Should Contain  Username may only include characters a to z
Register With Valid Username And Too Short Password
    Input Credentials  paavo  h1lav1t
    Output Should Contain  Password needs to be longer than 7 characters
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  paavo  hilavitkutin
    Output Should Contain  Password must include characters other than a to z

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command