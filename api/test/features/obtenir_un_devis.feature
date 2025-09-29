Feature: CRUD Item - Test API
Scenario: lister les items
  Given je suis à la recherche d'un item pour ma guilde
  When j'appel l'api
  Then la liste doit être : 9