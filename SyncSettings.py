# -*- coding: utf-8 -*-

import sys

import sublime

reloader = 'sync_settings.reloader'

if int(sublime.version()) > 3000:
    from .sync_settings.commands import *  # noqa: F403, F401

    reloader = 'SyncSettings.' + reloader
    from imp import reload
else:
    from sync_settings.commands import *  # noqa: F403, F401

# Make sure all dependencies are reloaded on upgrade
if reloader in sys.modules:
    reload(sys.modules[reloader])


def plugin_loaded():
    from .sync_settings.libs import settings
    from .sync_settings.thread_progress import ThreadProgress
    from .sync_settings import sync_version as version

    if settings.get('auto_upgrade'):
        ThreadProgress(target=version.upgrade, message='checking current version')

    settings.create_sync_settings_path(settings.get("config_location"))


'''
  Sublime Text 2 Compatibility
'''
if sys.version_info < (3,):
    plugin_loaded()
