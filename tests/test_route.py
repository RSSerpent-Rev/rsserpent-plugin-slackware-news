from starlette.testclient import TestClient


def test_route(client: TestClient) -> None:
    """Test `rsserpent_plugin_slackware_news.route`."""
    response = client.get("/slackware-news")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
    assert response.text.count("Example Title") == 1
