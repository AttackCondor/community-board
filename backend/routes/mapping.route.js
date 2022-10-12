const express = require('express');
const app = express();
const mappingRoute = express.Router();
// Mapping model
let Mapping = require('../models/Mapping');
// Get All Mappings
mappingRoute.route('/').get((req, res) => {
  Mapping.find((error, data) => {
    if (error) {
      return next(error)
    } else {
      res.json(data)
    }
  })
})
// Update mapping
mappingRoute.route('/update/:id').put((req, res, next) => {
  Mapping.findByIdAndUpdate(req.params.id, {
    $set: req.body
  }, (error, data) => {
    if (error) {
      console.log(error)
      return next(error)
    } else {
      res.json(data)
      console.log('Mapping updated successfully')
    }
  })
})
module.exports = mappingRoute;