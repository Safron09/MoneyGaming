# Created by Y.Safronnynov at 8/12/2021

Feature: Test Scenarios for a new moneygaming.com player

  Scenario: Register a new user
    Given Open Moneygaming page
    When Search for "Join Now" button and Click
    And Enter First Name
    And Enter Bob
    Then Check tickbox
    And Press "Join Now" button
    And Result contains This field is required