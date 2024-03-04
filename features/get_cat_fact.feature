Feature: Get and send cat facts

  Scenario: Requesting a cat fact successfully
    Given the server is running
    When I request a cat fact
    Then I receive a cat fact with status code 200

  Scenario: Posting a cat fact successfully
    Given the server is running
    When I post a cat fact
    Then I receive a success message with status code 200 or 201

  Scenario: Updating a cat fact successfully
    Given the server is running
    When I update a cat fact
    Then I receive a success message with status code 200 or 201
