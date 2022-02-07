*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Register With Valid Username And Password
    Create Valid User
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Create Invalid User
    Page Should Contain  Invalid username
    

Register With Valid Username And Too Short Password
    Click Link  /register
    Input Text  username  rasmus
    Input Password  password  rasmus6
    Input Password  password_confirmation  rasmus6
    Click Button  Register
    Page Should Contain  Invalid password

Register With Nonmatching Password And Password Confirmation
    Click Link  /register
    Input Text  username  rasmus
    Input Password  password  rasmus666
    Input Password  password_confirmation  rasmus667
    Click Button  Register
    Page Should Contain  Passwords must match

Login After Successful Registration
    Create Valid User
    Go To Login Page
    Input Text  username  rasmus
    Input Password  password  rasmus666
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Create Invalid User
    Go To Login Page
    Input Text  username  ra
    Input Password  password  rasmus666
    Click Button  Login

*** Keywords ***
Reset Application And Go To Home Page
    Reset Application
    Go To Home Page

Create Valid User
    Click Link  /register
    Input Text  username  rasmus
    Input Password  password  rasmus666
    Input Password  password_confirmation  rasmus666
    Click Button  Register

Create Invalid User
    Click Link  /register
    Input Text  username  ra
    Input Password  password  rasmus666
    Input Password  password_confirmation  rasmus666
    Click Button  Register