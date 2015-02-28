# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Edit conf file (mainly for programatic API)."""

from ._hook import (conf_file, mk_conf, pkg_options, pkg_path, pkg_version,
                    print_conf, reg_apikey, reg_mod, reg_myopt, reg_plugin)

__all__ = ('pkg_version', 'pkg_path', 'pkg_options',
           'reg_mod', 'reg_plugin', 'reg_apikey', 'reg_myopt',
           'conf_file', 'mk_conf', 'print_conf')
