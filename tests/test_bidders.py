import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_graphql_get_bidders():
    query = """
    query {
        getBidders {
            userId
            email
            isVerified
        }
    }
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/graphql", json={"query": query})
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert "getBidders" in data["data"]

