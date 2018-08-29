# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年08月29日 星期三 14时44分15秒
from flask import Flask
from flask_graphql import GraphQLView
import graphene
app = Flask(__name__)

class Query(graphene.ObjectType):
    """查询API"""

    description = "测试API"
    hello = graphene.String(name=graphene.String(default_value="ibbd"),
                            description='这是hello的文档')
    hello_list = graphene.List(of_type=graphene.String,
                               description="这是hello list的文档")
    hello_json = graphene.JSONString(description="这是hello json的文档")
    hello_obj = graphene.JSONString(description="这是hello object的文档")

    def resolve_hello(self, info, name):
        print(info)
        return 'Hello ' + name

    def resolve_hello_list(self, info):
        print(info)
        return ['Hello', 'world']

    def resolve_hello_json(self, info):
        print(info)
        return {'Hello': 'world'}

    def resolve_hello_obj(self, info):
        print(info)
        return {'Hello': 'world'}


schema = graphene.Schema(query=Query)
view_func = GraphQLView.as_view('graphql', schema=schema, graphiql=True)
app.add_url_rule('/graphql', view_func=view_func)

if __name__ == '__main__':
    # {hello}
    # {hello(name: "world")}
    app.run(debug=True)
