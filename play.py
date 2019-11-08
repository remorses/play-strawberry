import strawberry
from typing import Optional
from graphql import DirectiveLocation


@strawberry.interface
class Node:
    id: Optional[strawberry.ID]

@strawberry.type
class User(Node):
    name: str
    age: int
    id: Optional[strawberry.ID]

@strawberry.type
class Query:
    @strawberry.field
    def user(self, info) -> User:
        return User(name="Patrick", age=100)


@strawberry.directive(
    locations=[DirectiveLocation.FIELD], description="Sample description"
)
def uppercase(value: str) -> str:
    return value.upper()


@strawberry.type(is_input=True)
class Input:
    name: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    def fuckYou(self, info, input: Input) -> str:
        return "ciao " + input.name


schema = strawberry.Schema(query=Query, mutation=Mutation)
