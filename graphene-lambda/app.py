from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

cors = CORS(app, resources={r"/graphql": {"origins": "http://localhost:3000"}})

if __name__ == '__main__':
    app.run(threaded=True, debug=True)

@app.route("/")
def hello2():
    return "Hello World!"


