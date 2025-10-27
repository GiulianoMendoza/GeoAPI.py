from fastapi.testclient import TestClient
from app.main import app


def _login_token(client: TestClient) -> str:
    r = client.post("/v1/auth/login", params={"username": "admin", "password": "1234"})
    assert r.status_code == 200
    return r.json()["access_token"]


def test_route_offline_with_auth():
    client = TestClient(app)
    token = _login_token(client)

    headers = {"Authorization": f"Bearer {token}"}
    r = client.get(
        "/v1/Geolocalizacion/route-offline",
        params={
            "from_lat": -34.6037,
            "from_lon": -58.3816,
            "to_lat": -34.9214,
            "to_lon": -57.9545,
            "metric": "time",
        },
        headers=headers,
    )
    assert r.status_code == 200
    data = r.json()
    assert data["metric"] in ("time", "distance")
    assert isinstance(data["total"], (int, float))
    assert "path" in data and isinstance(data["path"], list) and len(data["path"]) >= 2

