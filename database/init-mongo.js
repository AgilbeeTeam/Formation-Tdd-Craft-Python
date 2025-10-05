// Besoin de s'authentifier ici ...
db.getSiblingDB('admin').auth(process.env.MONGO_INITDB_ROOT_USERNAME, process.env.MONGO_INITDB_ROOT_PASSWORD);

db.createUser({
  user: process.env.MONGO_USER,
  pwd: process.env.MONGO_PASSWORD,
  roles: [{ role: "readWrite", db: process.env.MONGO_DB }]
});

db = db.getSiblingDB(process.env.MONGO_DB);

db.createCollection("items");

db.items.insertMany([
    { name : "+5 Dexterity Vest", sell_in : 10, quality : 20 },
    { name : "Aged Brie", sell_in : 2, quality : 0 },
    { name : "Elixir of the Mongoose", sell_in : 5, quality : 7 },
    { name : "Sulfuras, Hand of Ragnaros", sell_in : 0, quality : 80 },
    { name : "Sulfuras, Hand of Ragnaros", sell_in : -1, quality : 80 },
    { name : "Backstage passes to a TAFKAL80ETC concert", sell_in : 15, quality : 20 },
    { name : "Backstage passes to a TAFKAL80ETC concert", sell_in : 10, quality : 49 },
    { name : "Backstage passes to a TAFKAL80ETC concert", sell_in : 5, quality : 49 },
    { name : "Conjured Mana Cake", sell_in : 3, quality : 6}
]);