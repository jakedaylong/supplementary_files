#!/USr/bin/env python
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def supply_test_data():
    aa = 25
    bb = 35
    cc = 45
    return [aa, bb, cc]


def test_compare_with_aa(supply_test_data):
    zz = 35
    assert supply_test_data[0] == zz, "aa and zz failed"


def test_compare_with_bb(supply_test_data):
    zz = 25
    assert supply_test_data[1] == zz, "bb and zz comparison failed"


def test_compare_with_cc(supply_test_data):
    zz = 35
    assert supply_test_data[2] == zz, "cc and zz comparison failed"


def test_passes(supply_test_data):
    zz = 25
    assert supply_test_data[0] == zz
