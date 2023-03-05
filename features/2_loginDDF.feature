Feature: Apollo Login
  Scenario: Validate Apollo login functionality on chrome
    Given Chrome is opened and Apollo app is opened
    When user clicks on later button
    When User click on login button
    Then It navigate to Mobile Number window
    And User enters mobile number number
    Then It shows error message

