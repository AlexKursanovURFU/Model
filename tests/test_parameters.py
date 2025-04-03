from src.model.parameters import compute_derived_constants

def test_compute_derived_constants():
     # Инициализация констант
    constants = {
        "R": 1,          
        "T": 2,               
        "F": 3,       
        "C": 4e-5,             
        "g_f": 0.001,
        "ACh": 0,
        "g_Kr": 0.0035,
        "Ki": 140,             
        "Kc": 5.4,             
        "g_K1": 0,
        "g_b": 0.0012,
        'E_b': -22.5,
        "I_p": 0.14268,
        "Nai": 8,
        "kNaCa": 2.14455,
        "Qci": 0.1369,
        "Qn": 0.4315,
        "Qco": 0,
        "Kci": 0.0207,
        "K1ni": 395.3,
        "K2ni": 2.289,
        "K3ni": 26.44,
        "Kcni": 26.44,
        "K3no": 4.663,
        "K1no": 1628,
        "K2no": 561.4,
        "Kco": 3.663,
        "Cao": 2,
        "Nao": 140,
        "g_Na": 0,
        "delta_m": 1e-5,
        "g_CaL": 0.009,
        "E_CaL": 62,
        "act_shift": -15,
        "slope_factor_act": -5,
        "inact_shift": -5,
        "inact_shift_f2": -5,
        "g_to": 0,
        "E_st": -37.4,
        "g_st": 0.0001,
        "g_Ach_max": 0.0198,
        "K_ACh": 0.00035,
        "alpha_achf": 73.1,
        "alpha_achs": 3.7,
        "V_cell": 3.18872e-6,
        "P_rel": 1500,
        "K_up": 0.0006,
        "tau_tr": 0.06,
    }

    constants = compute_derived_constants(constants)
    assert constants["RTONF"] == 2/3

    assert constants["RTONF"] == 2/3
