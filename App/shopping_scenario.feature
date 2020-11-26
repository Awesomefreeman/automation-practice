Feature: Shopping
  Scenario: Buying item
    Given open main page
    When quick view first item
    And add item to cart
    And proceed to checkout
    Then i should see "Your order on My Store is complete."