const express = require('express')
const path = require('path')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')

//Connect to the mongo database
mongoose
    .connect(concat('mongodb://', process.env.MONGO_USER, ':', process.env.MONGO_PASS, '@', process.env.MONGO_CONTAINER, ':27017/', process.env.MONGO_DB_NAME,'?authSource=admin'))
    .then((x) => {
        console.log(`Connected to Mongo! Database name: "${x.connections[0].name}"`)
    })
    .catch((err) => {
        console.error('Error connecting to mongo', err.reason)
    })

const mappingRoute = require('./routes/mapping.route')
const app = express()
app.use(bodyParser.json())
app.use(
    bodyParser.urlencoded({
        extended: false,
    }),
)
app.use(cors())
app.use(express.static(path.join(__dirname, 'dist/mean-stack-crud-app')))
app.use('/', express.static(path.join(__dirname, 'dist/mean-stack-crud-app')))
app.use('/api', mappingRoute)
// Create port
const port = process.env.PORT || 4000
const server = app.listen(port, () => {
  console.log('Connected to port ' + port)
})
// Find 404 and hand over to error handler
app.use((req, res, next) => {
  next(createError(404))
})
// error handler
app.use(function (err, req, res, next) {
  console.error(err.message) // Log error message in our server's console
  if (!err.statusCode) err.statusCode = 500 // If err has no specified error code, set error code to 'Internal Server Error (500)'
  res.status(err.statusCode).send(err.message) // All HTTP requests must have a response, so let's send back an error with its status code and message
})