#!/usr/bin/python

import web

from dtc import log_config
from dtc.config.ui.url import urls, mapping
from dtc.code_lookup import initialize

initialize()

app = web.application(urls, mapping)
app.run()

