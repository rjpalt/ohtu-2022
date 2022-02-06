# A new user account can be created if a proper unused username and a proper password are given
*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  rasmus  rasmuspasmus85
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  samu  samuk4kk4
    Output Should Contain  User with username samu already exists

Register With Too Short Username And Valid Password
    Input Credentials  la  B4n4n4Meccana
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  lauri  B4n4n4
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  lauri  BananaMeccana
    Output Should Contain  Invalid password

*** Keywords ***
Create User And Input New Command
    Create User  samu  samuk4kk4
    Input New Command