# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年08月29日 星期三 20时10分29秒
import graphene
from flask import Flask
from flask_graphql import GraphQLView
from data_starwars import get_droid, get_hero, get_human, \
    Character, Human, Droid, Episode


class Query(graphene.ObjectType):
    """Query API"""
    hero = graphene.Field(Character, episode=Episode(), description='hero文档')
    human = graphene.Field(Human, id=graphene.String())
    droid = graphene.Field(Droid, id=graphene.String())

    def resolve_hero(self, info, episode=None):
        return get_hero(episode)

    def resolve_human(self, info, id):
        print(id)
        return get_human(id)

    def resolve_droid(self, info, id):
        return get_droid(id)


app = Flask(__name__)
schema = graphene.Schema(query=Query)
GraphQLView.graphiql_html_title = 'test'
view_func = GraphQLView.as_view('graphql', schema=schema, graphiql=True)
app.add_url_rule('/graphql', view_func=view_func)

if __name__ == '__main__':
    """
    {human(id: "1002") {
      id
      name
      friends {
        id
        name
      }
      homePlanet
    }}
    """
    app.run(debug=True)
