from typing import Any, Dict

from lxml import html
from rsserpent_rev.utils import HTTPClient, cached


path = "/slackware-news"


@cached
async def provider() -> Dict[str, Any]:
    """Return the latest news from The Slackware Linux Project.

    Returns:
        Dict[str, Any]: The Slackware Linux Project news.
    """
    async with HTTPClient() as client:
        response = await client.get("http://www.slackware.com/")
        tree = html.fromstring(response.content.decode())
        items = []
        for table in tree.xpath("//center[not(parent::body)]/table"):
            title = table.xpath("./tr[1]//b")[0]
            content = table.xpath("./tr[2]/td[1]")[0]
            date = table.xpath("normalize-space(./tr[2]/td[2]//b)")
            items.append(
                {
                    "title": title.text_content(),
                    "description": content.text_content(),
                    "link": "http://www.slackware.com/",
                    "pub_date": date,
                }
            )
        return {
            "title": "The Slackware Linux Project",
            "link": "http://www.slackware.com/",
            "description": "The Slackware Linux Project News",
            "items": items,
        }
