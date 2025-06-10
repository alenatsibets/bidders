import strawberry

@strawberry.type
class BidderType:
    user_id: int
    email: str
    is_verified: bool

@strawberry.input
class BidderInput:
    email: str
    password: str
