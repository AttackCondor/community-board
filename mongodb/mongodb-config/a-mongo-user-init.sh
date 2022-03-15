# Scripts will be executed in alphabetical order. To use env variables, it is necessary to use a shell script rather than a js script.

set -e

mongo <<EOF
use admin

db.createUser({
  user: '$MONGO_USERNAME',
  pwd:  '$MONGO_PASSWORD',
  roles: [{
    role: 'readWrite',
    db: 'communityBoard'
  }]
})
EOF