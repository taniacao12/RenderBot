Feature: File is valid

  Scenario: Verify the specified text file contains at least 3 walls and 1 door, with at least 1 door being and exit
    Given the name of a file
    When I read the file
    Then it should have at least 3 walls
    And it should have at least 1 door
    And at least 1 door should be an exit
    And I should say the file is valid
  
  Scenario: Verify width of exits
    Given list of exits
    Then each should be between 34 to 48 inches
    And I should say all exits are valid