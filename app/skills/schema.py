from marshmallow import Schema, fields

class employeeSchema(Schema):
  id = fields.Int(required=True)
  firstName = fields.Str()
  lastName = fields.Str()
  contactEmail = fields.Str()
  companyEmail = fields.Str()
  hiredDate = fields.URL()