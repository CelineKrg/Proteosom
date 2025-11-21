from pyteomics import achrom
from proteomics.liquid_chromatography import (
    predict_lc_retention_times,
    plot_retention_time, 
    select_retention_time_window
)

def test_predict_lc_retention_times():
    peptides = ["DWENAPVIPIESR"]
    expected = {"DWENAPVIPIESR": round(float(achrom.calculate_RT('DWENAPVIPIESR', achrom.RCs_guo_ph7_0)), 2)}


    actual = predict_lc_retention_times(peptides)
    assert actual == expected

test_predict_lc_retention_times()


def test_select_retention_time_window():
    peptide_rt_map = {
        "PEPTIDE1": 12.5,
        "PEPTIDE2": 25.0,
        "PEPTIDE3": 40.0,
        "PEPTIDE4": 52.2
    }
    selected = select_retention_time_window(peptide_rt_map, lower_ret_time=20, upper_ret_time=41)
    expected = {
        "PEPTIDE2": 25.0,
        "PEPTIDE3": 40.0,
    }
    assert selected == expected

    selected_all = select_retention_time_window(peptide_rt_map, lower_ret_time=10, upper_ret_time=53)
    expected_all = {
        "PEPTIDE1": 12.5,
        "PEPTIDE2": 25.0,
        "PEPTIDE3": 40.0,
        "PEPTIDE4": 52.2
    }
    assert selected_all == expected_all

    selected_none = select_retention_time_window(peptide_rt_map, lower_ret_time=30, upper_ret_time=35)
    expected_none = {}
    assert selected_none == expected_none

test_select_retention_time_window()