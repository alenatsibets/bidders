import strawberry
from app.db.session import get_db_session
from app.db.models import Bidder
from app.schema.types import BidderInput, BidderType
from app.security.crypto import hash_password

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def register_bidder(self, input: BidderInput) -> BidderType:
        async with get_db_session() as session:
            new_bidder = Bidder(
                email=input.email,  # setter handles encryption
                password_hash=hash_password(input.password),
                is_verified=False
            )
            session.add(new_bidder)
            await session.commit()
            await session.refresh(new_bidder)

            return BidderType(
                user_id=new_bidder.user_id,
                email=new_bidder.email_encrypted,
                is_verified=new_bidder.is_verified
            )