"""
test_004_reset_pw3.py - test resetting pw3

Copyright (C) 2018  g10 Code GmbH
Author: NIIBE Yutaka <gniibe@fsij.org>

This file is a part of Gnuk, a GnuPG USB Token implementation.

Gnuk is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Gnuk is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from card_const import *

# Gnuk specific feature of clear PW3
def test_setup_pw3_null(card):
    r = card.change_passwd(3, FACTORY_PASSPHRASE_PW3, None)
    assert r

def test_verify_pw3(card):
    v = card.verify(3, FACTORY_PASSPHRASE_PW3)
    assert v

# Check PW1 again to see the possiblity of admin-less mode
def test_verify_pw1(card):
    v = card.verify(1, FACTORY_PASSPHRASE_PW1)
    assert v

def test_verify_pw1_2(card):
    v = card.verify(2, FACTORY_PASSPHRASE_PW1)
    assert v