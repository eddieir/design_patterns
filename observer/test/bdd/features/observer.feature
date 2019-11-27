Feature: Application to add, remove and notify the observers

	 As a customer I wish to be able to subscribe in a certain subject
	 and to be able to unsubscribe any time
	 and to be notified by my subcribed subject
	 
	
	@tag1 
	Scenario: Subscribe in a certain subject
	Given I have a subject
	When I "'lorie'" subcribe in the subject 
	Then I will be notified

	@tag2
	Scenario: Unsubscribe in a certain subject
	Given I have a subject where I subcribed
	When I unsubscribe in the subject
	Then I will not receive any notifications