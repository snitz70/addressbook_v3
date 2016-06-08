# Created by Brian Snyder at 6/8/2016
Feature: Addressbook
  As a user I want to create or use an addressbook to
  store contacts and addresses

  @wip
  Scenario: create a new addressbook
    Given I have no addressbooks in database
    When I create a new addressbook called 'one'
    Then the addressbook should be saved to the database

  @wip
  Scenario: create a duplicate addressbook
    Given I already have addressbook 'one' saved
    When I create a new addressbook called 'one'
    Then I should receive a warning

  @todo
  Scenario: create an addressbook with empty name
    When I create a new addressbook with no name
    Then I should receive a warning


  Scenario: Get a listing of existing addressbooks
    When I ask for a list of existing addressbooks
    Then I should get a list


  Scenario: Delete addressbook
    When I ask to delete addressbook 'one'
    And the addressbook contains no contacts
    Then the addressbook should be deleted

  Scenario: Delete non empty addressbook
    When I ask to delete an addressbook
    And the addressbook contains contacts
    Then the addressbook should not be deleted

  Scenario: Use existing addressbook
    When I ask to use addressbook 'one'
    Then addressbook 'one' should be selected
