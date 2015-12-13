Feature: Snapshot rates
	As user
	I want to know FX rates for a particular currency
	So that I know how much money I need to exchange for that currency

	Scenario: Get a sell rate for USD/THB
		Given I have money in THB
		And I want money in USD
		When I open the FX rates page
		Then I see the sell rate for USD/THB on the page

	Scenario: Get a buy rate for USD/THB
		Given I have money in USD
		And I want money in THB
		When I open the FX rates page
		Then I see the buy rate for USD/THB on the page


FX Rates Service Specification
==============================

The users must be able to see FX rates for a particular currency therefore; 
they know how much money they need to exchange for that currency.

Tags: FX rates

* User must open the FX Rates page

Successful retrieve
-------------------

Tags: successful

For existing currencies, the FX Rates page will show their rates.

* "USD/THB" should show up in the page with a buy rate is "35.989" and a sell rate is "35.890"
