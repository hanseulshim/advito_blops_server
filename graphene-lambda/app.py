from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(threaded=True, debug=True)

@app.route("/")
def hello2():
    return "Hello World!"


