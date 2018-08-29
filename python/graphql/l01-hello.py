# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年08月29日 星期三 14时33分47秒
from flask import Flask
from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView

class Query(ObjectType):
    hello = String(description='这是hello的文档')
    #def resolve_hello(self, args, context, info):
    def resolve_hello(self, info):
        print(info)
        return 'World'

schema=Schema(query=Query)
view_func = GraphQLView.as_view('graphql', schema=schema, graphiql=True)

app = Flask(__name__)
app.add_url_rule('/', view_func=view_func)

if __name__ == '__main__':
    app.run(debug=True)
