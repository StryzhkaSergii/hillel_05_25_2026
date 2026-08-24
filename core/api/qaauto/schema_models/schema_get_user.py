# pip install marshmallow

from marshmallow import Schema, fields
from marshmallow.fields import Enum


class DistanceUnit(Enum):
    KM = "km"
    ML = "ml"

class UserSchema(Schema):
    userId = fields.Int(required=True)
    # distanceUnits = fields.Enum(DistanceUnit, by_value=True)
    distanceUnits = fields.Str()
    currency = fields.Str()
    photoFilename = fields.Str()

class CurrentSchema(Schema):
    status = fields.Str()
    data = fields.Nested(UserSchema)

# response = {'status': 'ok', 'data':
#     {'userId': 390050,
#      'currency': 'usd',
#      'distanceUnits': 'km',
#      'photoFilename': 'default-user.png'}}
#
# CurrentSchema().load(response)