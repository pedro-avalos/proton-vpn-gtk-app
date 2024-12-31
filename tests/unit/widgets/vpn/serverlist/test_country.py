"""
Copyright (c) 2023 Proton AG

This file is part of Proton VPN.

Proton VPN is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Proton VPN is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ProtonVPN.  If not, see <https://www.gnu.org/licenses/>.
"""
import time
from unittest.mock import Mock

import pytest

from proton.vpn.connection.states import ConnectionStateEnum, Connecting, Connected, Disconnected
from proton.vpn.session.servers import ServerList, Country, LogicalServer

from proton.vpn.app.gtk.controller import Controller
from proton.vpn.app.gtk.widgets.vpn.serverlist.country import DeferredCountryRow
from proton.vpn.app.gtk.widgets.vpn.serverlist.icons import UnderMaintenanceIcon
from tests.unit.testing_utils import process_gtk_events
from proton.vpn.logging import logging


FREE_TIER = 0
PLUS_TIER = 2
COUNTRY_CODE = "AR"


@pytest.fixture
def country_servers():
    api_data = {
        "LogicalServers": [
            {
                "ID": 1,
                "Name": "AR#1",
                "Status": 1,
                "Load": 50,
                "Servers": [{"Status": 1}],
                "ExitCountry": COUNTRY_CODE,
                "Tier": 1,
            },
            {
                "ID": 2,
                "Name": "AR#2",
                "Status": 1,
                "Load": 50,
                "Servers": [{"Status": 1}],
                "ExitCountry": COUNTRY_CODE,
                "Tier": 2,
            },
        ]
    }
    return ServerList(
        user_tier=PLUS_TIER,
        logicals=[LogicalServer(server) for server in api_data["LogicalServers"]]
    )


@pytest.fixture
def country(country_servers):
    return Country(code=COUNTRY_CODE, servers=country_servers)


@pytest.fixture
def mock_controller():
    return Mock(Controller)
