# pip install marshmallow

from marshmallow import Schema, fields
from enum import Enum


class DistanceUnits(Enum):
    km = 'km'
    ml = 'ml'

class UserSchema(Schema):
    userId = fields.Int(required=True)
    distanceUnits = fields.Enum(enum=DistanceUnits, required=True)
    currency = fields.Str()
    photoFilename = fields.Str()

class CurrentSchema(Schema):
    status = fields.Str()
    data = fields.Nested(UserSchema)

# response = {'status': 'ok', 'data':
#     {'userId': 390050,
#      'currency': 'usd',
#      'distanceUnits': 'kmm',
#      'photoFilename': 'default-user.png'}}
#
# CurrentSchema().load(response)