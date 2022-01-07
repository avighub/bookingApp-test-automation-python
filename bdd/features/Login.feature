Feature: Login Page

  Background: Launch browser
    Given I navigate to swagLabs login page

  @sanity
  Scenario: Login to SwagLabs using valid credentials with params
#    Given I navigate to swagLabs login page
    When I enter "standard_user" and "secret_sauce"
    Then I should see Products Page

  @regression
  Scenario Outline: Login to SwagLabs using valid credentials with table params
#    Given I navigate to swagLabs login page
    When I enter "<username>" and "<password>"
    Then I should see Products Page
#    And I close the browser
    Examples:
      | username                | password     |  |
      | standard_user           | secret_sauce |  |
      | performance_glitch_user | secret_sauce |  |