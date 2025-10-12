Feature: CRUD Item - Test API
Scenario: lister les items
  Given je suis à la recherche d'un item pour ma guilde
  When je récupère les articles disponible de la taverne
  Then la liste doit être de 9