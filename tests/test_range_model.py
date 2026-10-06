"""Non-invasive checks for units, input provenance and inherited switch behavior."""
from pathlib import Path
import sys
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src/python"))
from range_model import calculate_ranges, get_hvac_power, get_p_motor_avg, load_cycle


class RangeChecks(unittest.TestCase):
    def test_supplied_cycle(self):
        speed = load_cycle(ROOT / "data/raw/class3data.csv")
        self.assertEqual(speed.size, 1801)
        self.assertAlmostEqual(float(speed.max()), 131.3)

    def test_power_units_at_60_kmh(self):
        # Independent force calculation: 164.808 N rolling + 122.5 N drag.
        expected_w = (164.808 + 122.5) * (50 / 3) / 0.9
        self.assertAlmostEqual(get_p_motor_avg(np.array([60.0])), expected_w)

    def test_stationary_traction(self):
        self.assertEqual(get_p_motor_avg(np.zeros(5)), 0)

    def test_ptc_load(self):
        self.assertEqual(get_hvac_power("PTC", -15), 4725.0)

    def test_switch_boundary(self):
        self.assertEqual(get_hvac_power("R1234yf", -10.0001), get_hvac_power("PTC", -10.0001))
        self.assertLess(get_hvac_power("R1234yf", -10), get_hvac_power("PTC", -10))

    def test_no_cooling_above_target(self):
        for mode in ("OFF", "PTC", "Propane", "R1234yf"):
            self.assertEqual(get_hvac_power(mode, 25), 0)

    def test_unknown_mode(self):
        with self.assertRaises(ValueError):
            get_hvac_power("unknown", 0)

    def test_energy_to_range_units(self):
        # Zero-speed cycle has zero range even when battery/auxiliary time is finite.
        result = calculate_ranges(np.zeros(5), np.array([-15.0]))
        for values in result.values():
            self.assertEqual(float(values[0]), 0)


if __name__ == "__main__":
    unittest.main()
