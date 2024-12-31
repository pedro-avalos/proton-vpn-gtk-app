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
from time import time
from unittest.mock import Mock

from gi.repository import GLib
import pytest

from proton.vpn.session.servers import ServerList, LogicalServer

from proton.vpn.app.gtk.widgets.vpn.search_entry import SearchEntry
from proton.vpn.app.gtk.widgets.vpn.serverlist.serverlist import ServerListWidget
from tests.unit.testing_utils import process_gtk_events, run_main_loop

PLUS_TIER = 2
FREE_TIER = 0


@pytest.fixture
def api_data():
    return {
        "Code": 1000,
        "LogicalServers": [
            {
                "ID": 2,
                "Name": "AR#10",
                "Status": 1,
                "Load": 50,
                "Servers": [{"Status": 1}],
                "ExitCountry": "AR",
                "Tier": PLUS_TIER,
            },
            {
                "ID": 1,
                "Name": "JP-FREE#10",
                "Status": 1,
                "Load": 50,
                "Servers": [{"Status": 1}],
                "ExitCountry": "JP",
                "Tier": FREE_TIER,

            },
            {
                "ID": 3,
                "Name": "AR#9",
                "Status": 1,
                "Load": 50,
                "Servers": [{"Status": 1}],
                "ExitCountry": "AR",
                "Tier": PLUS_TIER,
            },
            {
                "ID": 5,
                "Name": "CH-JP#1",
                "Status": 1,
                "Load": 50,
                "Servers": [{"Status": 1}],
                "Features": 1,  # Secure core feature
                "EntryCountry": "CH",
                "ExitCountry": "JP",
                "Tier": PLUS_TIER,
            },
            {
                "ID": 4,
                "Name": "JP#9",
                "Status": 1,
                "Load": 50,
                "Servers": [{"Status": 1}],
                "ExitCountry": "JP",
                "Tier": PLUS_TIER,

            },
        ]
    }


@pytest.fixture
def server_list(api_data):
    return ServerList(
        user_tier=PLUS_TIER,
        logicals=[LogicalServer(server) for server in api_data["LogicalServers"]]
    )


@pytest.fixture
def server_list_widget(server_list):
    server_list_widget = ServerListWidget(controller=Mock())
    server_list_widget.display(user_tier=PLUS_TIER, server_list=server_list)
    process_gtk_events()
    return server_list_widget

