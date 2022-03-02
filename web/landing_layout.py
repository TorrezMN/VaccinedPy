#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

import dash_bootstrap_components as dbc

menu = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="COVID - Paraguay",
    brand_href="#",
    color="primary",
    dark=True,
)
