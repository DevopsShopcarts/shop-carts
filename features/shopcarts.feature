Feature: The shopcarts service back-end
    As a Shopcarts Manager 
    I need a RESTful catalog service
    So that I can keep track of all the shopcarts

Background:
    Given the following shopcarts 
        | customer_id | id | name           | quantity | price |
        | 1           | 1  | Apple Watch    | 1        | 100   |
        | 1           | 2  | Macbook Pro    | 15       | 520   |
        | 2           | 3  | iPhone13       | 14       | 250   |
        | 2           | 4  | Apple Watch    | 5        | 130   |
        | 3           | 5  | iPad           | 7        | 150   |
        | 3           | 6  | Apple Belt     | 9        | 12    |

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "Shop Cart Demo RESTful Service" in the title
    And I should not see "404 Not Found"

Scenario: Add a Product
    When I visit the "Home Page"
    And I set the "Product Name" to "Water"
    And I set the "Product Quantity" to "12"
    And I set the "Customer ID" to "1"
    And I set the "Product Price" to "2.75"
    And I press the "Add" button
    Then I should see the message "Success"
    When I copy the "Customer ID" field
    And I press the "Clear-Form" button
    Then the "Product ID" field should be empty 
    And the "Product Name" field should be empty
    And the "Product Price" field should be empty
    And the "Product Quantity" field should be empty
    And the "Customer ID" field should be empty
    When I paste the "Customer ID" field
    And I press the "List" button
    Then I should see the message "Success"
    And I should see "Water" in the results
    And I should see "Apple Watch" in the results
    And I should see "Macbook Pro" in the results