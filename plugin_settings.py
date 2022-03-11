from utils import plugins

PLUGIN_NAME = 'Liquid XSLT Plugin'
DISPLAY_NAME = 'Liquid XSLT'
DESCRIPTION = 'A plugin for editing Janeway XSLT files.'
AUTHOR = 'Andy Byers'
VERSION = '0.1'
SHORT_NAME = 'liquidxslt'
MANAGER_URL = 'liquidxslt_manager'
JANEWAY_VERSION = "1.3.8"


class LiquidxsltPlugin(plugins.Plugin):
    plugin_name = PLUGIN_NAME
    display_name = DISPLAY_NAME
    description = DESCRIPTION
    author = AUTHOR
    short_name = SHORT_NAME
    manager_url = MANAGER_URL

    version = VERSION
    janeway_version = JANEWAY_VERSION


def install():
    LiquidxsltPlugin.install()


def hook_registry():
    LiquidxsltPlugin.hook_registry()


def register_for_events():
    pass
