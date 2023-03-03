Feature: Apollo24/7 Login
Background:
      Given Chrome is opened and Apollo24/7 app is opened
      When user click on later button

  Scenario: To validate the login button is clickable
      When User clicks on login button
      Then It navigates to Mobile Number window

  Scenario: To Validate Login Mobile Number window
      When User clicks on login button
      Then It navigates to Mobile Number window
      When User enter "7416531809"
      And User clicks on Next button
      Then It navigates to OTP window

  Scenario: To Validate Login of OTP window
      When User clicks on login button
      Then It navigates to Mobile Number window
      When User enter "7416531809"
      When User clicks on Next button
      Then It navigates to OTP window
      When User enter otp
      And User clicks on Next button
      Then It navigates to Home page

Scenario Outline: To Validate Login Mobile Number with Valid data
      When User clicks on login button
      Then It navigates to Mobile Number window
      When User enter Mobile Number <MobileNumber>
      And User clicks on Next button
      Then It navigates to OTP window
      When User enter otp
      And User clicks on Next button
      Then It navigates to Home page
    Examples:
      |MobileNumber|
      |7416531809  |


  Scenario Outline: To Validate Login OTP with Invalid data
      When User clicks on login button
      Then It navigates to Mobile Number window
      When User enter Mobile Number <MobileNumber>
      Then User cannot click on Next button
    Examples:
      |MobileNumber|
      |1234567890  |
      |0000000000  |
