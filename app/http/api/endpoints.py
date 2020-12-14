from flask import Flask, json, g, request
from app.skills.service import Service as Service
from app.skills.schema import employeeSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/employee", methods=["GET"])
def index():
  #return json_response(Service(g.oidc_token_info['sub']).find_all_kudos())
  return json_response("Hello, World!")


@app.route("/employee", methods=["POST"])
def create():
  userid = employeeSchema().load(json.loads(request.data))
  
  if userid.errors:
    return json_response({'error': userid.errors}, 422)

  service = Service(g.oidc_token_info['sub']).create_emp_for(userid)
  return json_response(service)

def json_response(payload, status=200):
  return (json.dumps(payload), status, {'content-type': 'application/json'})