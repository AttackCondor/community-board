db = new Mongo().getDB("community-board");

db.createCollection('boardMapping', { capped: false });
for(let i = 0; i<2048; i++){
  let row = Math.floor(i / 64)
  let col = i % 64
  db.boardMapping.insert([{
    "index" : i , 
    "rgbR" : 255 , 
    "rgbG" : 255 , 
    "rgbB" : 255 ,
    "row" : row ,
    "col" : col
  }]);
}