import strawberry
from enum import Enum
from typing import Optional
from graphql import DirectiveLocation


@strawberry.interface
class Node:
    id: Optional[strawberry.ID]

@strawberry.enum
class StringTest(Enum):
    A = "c"
    B = "i"
    C = "a"
    D = "o"

@strawberry.type
class User:
    name: str
    age: int
    enum: StringTest
    id: Optional[strawberry.ID] = None

@strawberry.type
class Query:
    @strawberry.field
    def user(self, info) -> User:
        return User(name="Patrick", age=100, enum=StringTest.A)


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
