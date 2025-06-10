import strawberry
from app.db.models import Bidder
from app.schema.types import BidderType
from app.db.session import get_db_session
from sqlalchemy.future import select


@strawberry.type
class Query:
    @strawberry.field
    async def get_bidders(self) -> list[BidderType]:
        async with get_db_session() as session:
            result = await session.execute(select(Bidder))
            bidders = result.scalars().all()
            return [
                BidderType(user_id=b.user_id, email=b.email_encrypted, is_verified=b.is_verified)
                for b in bidders
            ]
