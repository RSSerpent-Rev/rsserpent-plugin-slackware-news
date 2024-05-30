from rsserpent_rev.models import Persona, Plugin

from . import route

plugin = Plugin(
    name="rsserpent-plugin-slackware-news",
    author=Persona(
        name="EkkoG",
        link="https://github.com/EkkoG",
        email="beijiu572@gmail.com",
    ),
    prefix="/slackware-news",
    repository="https://github.com/EkkoG/rsserpent-plugin-slackware-news",
    routers={route.path: route.provider},
)
