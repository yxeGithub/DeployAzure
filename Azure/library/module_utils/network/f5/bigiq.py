# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 F5 Networks Inc.
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


import time

try:
    from f5.bigiq import ManagementRoot
    from icontrol.exceptions import iControlUnexpectedHTTPError
    HAS_F5SDK = True
except ImportError:
    HAS_F5SDK = False

try:
    from library.module_utils.network.f5.common import F5BaseClient
    from library.module_utils.network.f5.common import F5ModuleError
    from library.module_utils.network.f5.icontrol import iControlRestSession
except ImportError:
    from ansible.module_utils.network.f5.common import F5BaseClient
    from ansible.module_utils.network.f5.common import F5ModuleError
    from ansible.module_utils.network.f5.icontrol import iControlRestSession


class F5Client(F5BaseClient):
    @property
    def api(self):
        if self._client:
            return self._client
        for x in range(0, 3):
            try:
                result = ManagementRoot(
                    self.params['server'],
                    self.params['user'],
                    self.params['password'],
                    port=self.params['server_port'],
                    verify=self.params['validate_certs'],
                )
                self._client = result
                return self._client
            except Exception as ex:
                time.sleep(3)
        raise F5ModuleError(
            'Unable to connect to {0} on port {1}. '
            'The reported error was "{2}".'.format(
                self.params['server'], self.params['server_port'], str(ex)
            )
        )


class F5RestClient(F5BaseClient):
    @property
    def api(self):
        if self._client:
            return self._client
        for x in range(0, 10):
            try:
                result = iControlRestSession(
                    self.params['server'],
                    self.params['user'],
                    self.params['password'],
                    port=self.params['server_port'],
                    validate_certs=self.params['validate_certs'],
                    auth_provider='local'
                )
                self._client = result
                return self._client
            except Exception as ex:
                time.sleep(3)
        raise F5ModuleError(
            'Unable to connect to {0} on port {1}. '
            'The reported error was "{2}".'.format(
                self.params['server'], self.params['server_port'], str(ex)
            )
        )
