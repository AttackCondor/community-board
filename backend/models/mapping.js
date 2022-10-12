const mongoose = require('mongoose');
const Schema = mongoose.Schema;
// Define collection and schema
let Mapping = new Schema({
   index: {
      type: Number
   },
   rgbR: {
      type: Number
   },
   rgbG: {
      type: Number
   },
   rgbB: {
      type: Number
   },
   row: {
      type: Number
   },
   col: {
      type: Number
   }
}, {
   collection: 'boardMapping'
})
module.exports = mongoose.model('Mapping', Mapping)