from math import log
def create_legends():
    """
    Создает легенды для переменных модели электрофизиологии клетки.
    Ключи словарей соответствуют именам переменных (например, V, y, m).
    """
    # Инициализация словарей
    legend_states = {}
    legend_rates = {}
    legend_algebraic = {}
    legend_constants = {}
    legend_voi = "time in component environment (second)"

    # Определение констант
    legend_constants = {
        "R": "R in component membrane (joule_per_kilomole_kelvin)",
        "T": "T in component membrane (kelvin)",
        "F": "F in component membrane (coulomb_per_mole)",
        "C": "C in component membrane (microF)",
        "RTONF": "RTONF in component membrane (millivolt)",
        "g_f": "g_f in component hyperpolarising_activated_current (microS)",
        "ACh": "ACh in component acetylcholine_sensitive_current (millimolar)",
        "g_Kr": "g_Kr in component rapid_delayed_rectifier_potassium_current (microS)",
        "E_K_1": "E_K_1 in component transient_outward_potassium_current (millivolt)",
        "E_K": "E_K in component rapid_delayed_rectifier_potassium_current (millivolt)",
        "Ki": "Ki in component intracellular_potassium_concentration (millimolar)",
        "Kc": "Kc in component extracellular_potassium_concentration (millimolar)",
        "g_K1": "g_K1 in component time_independent_potassium_current (microS)",
        "g_b": "g_b in component background_current (microS)",
        "E_b": "E_b in component background_current (millivolt)",
        "I_p": "I_p in component sodium_potassium_pump (nanoA)",
        "Nai": "Nai in component intracellular_sodium_concentration (millimolar)",
        "kNaCa": "kNaCa in component sodium_calcium_exchange_current (nanoA)",
        "k34": "k34 in component sodium_calcium_exchange_current (dimensionless)",
        "k43": "k43 in component sodium_calcium_exchange_current (dimensionless)",
        "Qci": "Qci in component sodium_calcium_exchange_current (dimensionless)",
        "Qn": "Qn in component sodium_calcium_exchange_current (dimensionless)",
        "Qco": "Qco in component sodium_calcium_exchange_current (dimensionless)",
        "Kci": "Kci in component sodium_calcium_exchange_current (millimolar)",
        "K1ni": "K1ni in component sodium_calcium_exchange_current (millimolar)",
        "K2ni": "K2ni in component sodium_calcium_exchange_current (millimolar)",
        "K3ni": "K3ni in component sodium_calcium_exchange_current (millimolar)",
        "Kcni": "Kcni in component sodium_calcium_exchange_current (millimolar)",
        "K3no": "K3no in component sodium_calcium_exchange_current (millimolar)",
        "K1no": "K1no in component sodium_calcium_exchange_current (millimolar)",
        "K2no": "K2no in component sodium_calcium_exchange_current (millimolar)",
        "Kco": "Kco in component sodium_calcium_exchange_current (millimolar)",
        "Cao": "Cao in component extracellular_calcium_concentration (millimolar)",
        "Nao": "Nao in component extracellular_sodium_concentration (millimolar)",
        "g_Na": "g_Na in component fast_sodium_current (microlitre_per_second)",
        "E_Na": "E_Na in component fast_sodium_current (millivolt)",
        "delta_m": "delta_m in component fast_sodium_current_m_gate (millivolt)",
        "g_Cal": "g_CaL in component L_type_calcium_current (microS)",
        "E_CaL": "E_CaL in component L_type_calcium_current (millivolt)",
        "act_shift": "act_shift in component L_type_calcium_current_d_gate (millivolt)",
        "slope_factor_act": "slope_factor_act in component L_type_calcium_current_d_gate (millivolt)",
        "inact_shift": "inact_shift in component L_type_calcium_current_f_gate (millivolt)",
        "inact_shift_f2": "inact_shift in component L_type_calcium_current_f2_gate (millivolt)",
        "E_st": "E_st in component sustained_outward_potassium_current (millivolt)",
        "g_st": "g_st in component sustained_outward_potassium_current (microS)",
        "g_to": "g_to in component transient_outward_potassium_current (microS)",
        "g_ACh_max": "g_ACh_max in component acetylcholine_sensitive_current (microS)",
        "K_ACh": "K_ACh in component acetylcholine_sensitive_current (millimolar)",
        "alpha_achf": "alpha_achf in component acetylcholine_sensitive_current_achf_gate (per_second)",
        "alpha_achs": "alpha_achs in component acetylcholine_sensitive_current_achs_gate (per_second)",
        "V_up": "V_up in component intracellular_calcium_concentration (micrometre3)",
        "V_rel": "V_rel in component intracellular_calcium_concentration (micrometre3)",
        "V_sub": "V_sub in component intracellular_calcium_concentration (micrometre3)",
        "Vi": "Vi in component intracellular_calcium_concentration (micrometre3)",
        "V_cell": "V_cell in component intracellular_calcium_concentration (micrometre3)",
        "P_rel": "P_rel in component intracellular_calcium_concentration (per_second)",
        "K_up": "K_up in component intracellular_calcium_concentration (millimolar)",
        "tau_tr": "tau_tr in component intracellular_calcium_concentration (second)",
    }

    # Определение состояний
    legend_states = {
        "V": "V in component membrane (millivolt)",
        "y": "y in component hyperpolarising_activated_current_y_gate (dimensionless)",
        "paf": "paf in component rapid_delayed_rectifier_potassium_current_paf_gate (dimensionless)",
        "pas": "pas in component rapid_delayed_rectifier_potassium_current_pas_gate (dimensionless)",
        "pik": "pik in component rapid_delayed_rectifier_potassium_current_pik_gate (dimensionless)",
        "Casub": "Casub in component intracellular_calcium_concentration (millimolar)",
        "m": "m in component fast_sodium_current_m_gate (dimensionless)",
        "h1": "h1 in component fast_sodium_current_h1_gate (dimensionless)",
        "h2": "h2 in component fast_sodium_current_h2_gate (dimensionless)",
        "d": "d in component L_type_calcium_current_d_gate (dimensionless)",
        "f": "f in component L_type_calcium_current_f_gate (dimensionless)",
        "f2": "f2 in component L_type_calcium_current_f2_gate (dimensionless)",
        "r": "r in component transient_outward_potassium_current_r_gate (dimensionless)",
        "q_fast": "q_fast in component transient_outward_potassium_current_qfast_gate (dimensionless)",
        "q_slow": "q_slow in component transient_outward_potassium_current_qslow_gate (dimensionless)",
        "qa": "qa in component sustained_outward_potassium_current_qa_gate (dimensionless)",
        "qi": "qi in component sustained_outward_potassium_current_qi_gate (dimensionless)",
        "achf": "achf in component acetylcholine_sensitive_current_achf_gate (dimensionless)",
        "achs": "achs in component acetylcholine_sensitive_current_achs_gate (dimensionless)",
        "Cai": "Cai in component intracellular_calcium_concentration (millimolar)",
        "Ca_up": "Ca_up in component intracellular_calcium_concentration (millimolar)",
        "Ca_rel": "Ca_rel in component intracellular_calcium_concentration (millimolar)",
        "f_TC": "f_TC in component intracellular_calcium_concentration (dimensionless)",
        "f_TMC": "f_TMC in component intracellular_calcium_concentration (dimensionless)",
        "f_TMM": "f_TMM in component intracellular_calcium_concentration (dimensionless)",
        "f_CMi": "f_CMi in component intracellular_calcium_concentration (dimensionless)",
        "f_CMs": "f_CMs in component intracellular_calcium_concentration (dimensionless)",
        "f_CQ": "f_CQ in component intracellular_calcium_concentration (dimensionless)",
        "f_CSL": "f_CSL in component intracellular_calcium_concentration (dimensionless)",
    }

    # Определение скоростей изменения состояний
    legend_rates = {key: f"d/dt {description}" for key, description in legend_states.items()}

    # Определение алгебраических переменных
    legend_algebraic = {
        "i_Na": "i_Na in component fast_sodium_current (nanoA)",
        "i_CaL": "i_CaL in component L_type_calcium_current (nanoA)",
        "i_to": "i_to in component transient_outward_potassium_current (nanoA)",
        "i_Kr": "i_Kr in component rapid_delayed_rectifier_potassium_current (nanoA)",
        "i_f": "i_f in component hyperpolarising_activated_current (nanoA)",
        "i_st": "i_st in component sustained_outward_potassium_current (nanoA)",
        "i_K1": "i_K1 in component time_independent_potassium_current (nanoA)",
        "i_NaCa": "i_NaCa in component sodium_calcium_exchange_current (nanoA)",
        "i_p": "i_p in component sodium_potassium_pump (nanoA)",
        "i_b": "i_b in component background_current (nanoA)",
        "i_ACh": "i_ACh in component acetylcholine_sensitive_current (nanoA)",
        "y_inf": "y_inf in component hyperpolarising_activated_current_y_gate (dimensionless)",
        "tau_y": "tau_y in component hyperpolarising_activated_current_y_gate (second)",
        "paf_infinity": "paf_infinity in component rapid_delayed_rectifier_potassium_current_paf_gate (dimensionless)",
        "tau_paf": "tau_paf in component rapid_delayed_rectifier_potassium_current_paf_gate (second)",
        "pas_infinity": "pas_infinity in component rapid_delayed_rectifier_potassium_current_pas_gate (dimensionless)",
        "tau_pas": "tau_pas in component rapid_delayed_rectifier_potassium_current_pas_gate (second)",
        "pik_infinity": "pik_infinity in component rapid_delayed_rectifier_potassium_current_pik_gate (dimensionless)",
        "alpha_pik": "alpha_pik in component rapid_delayed_rectifier_potassium_current_pik_gate (per_second)",
        "beta_pik": "beta_pik in component rapid_delayed_rectifier_potassium_current_pik_gate (per_second)",
        "tau_pik": "tau_pik in component rapid_delayed_rectifier_potassium_current_pik_gate (second)",
        "g_K1_prime": "g_K1_prime in component time_independent_potassium_current (microS)",
        "x1": "x1 in component sodium_calcium_exchange_current (dimensionless)",
        "x2": "x2 in component sodium_calcium_exchange_current (dimensionless)",
        "x3": "x3 in component sodium_calcium_exchange_current (dimensionless)",
        "x4": "x4 in component sodium_calcium_exchange_current (dimensionless)",
        "k41": "k41 in component sodium_calcium_exchange_current (dimensionless)",
        "k34": "k34 in component sodium_calcium_exchange_current (dimensionless)",
        "k23": "k23 in component sodium_calcium_exchange_current (dimensionless)",
        "k21": "k21 in component sodium_calcium_exchange_current (dimensionless)",
        "k32": "k32 in component sodium_calcium_exchange_current (dimensionless)",
        "k43": "k43 in component sodium_calcium_exchange_current (dimensionless)",
        "k12": "k12 in component sodium_calcium_exchange_current (dimensionless)",
        "k14": "k14 in component sodium_calcium_exchange_current (dimensionless)",
        "do": "do in component sodium_calcium_exchange_current (dimensionless)",
        "di": "di in component sodium_calcium_exchange_current (dimensionless)",
        "alpha_m": "alpha_m in component fast_sodium_current_m_gate (per_second)",
        "beta_m": "beta_m in component fast_sodium_current_m_gate (per_second)",
        "E0_m": "E0_m in component fast_sodium_current_m_gate (millivolt)",
        "alpha_h1": "alpha_h1 in component fast_sodium_current_h1_gate (per_second)",
        "beta_h1": "beta_h1 in component fast_sodium_current_h1_gate (per_second)",
        "h1_inf": "h1_inf in component fast_sodium_current_h1_gate (dimensionless)",
        "tau_h1": "tau_h1 in component fast_sodium_current_h1_gate (second)",
        "alpha_h2": "alpha_h2 in component fast_sodium_current_h2_gate (per_second)",
        "beta_h2": "beta_h2 in component fast_sodium_current_h2_gate (per_second)",
        "h2_inf": "h2_inf in component fast_sodium_current_h2_gate (dimensionless)",
        "tau_h2": "tau_h2 in component fast_sodium_current_h2_gate (second)",
        "alpha_d": "alpha_d in component L_type_calcium_current_d_gate (per_second)",
        "beta_d": "beta_d in component L_type_calcium_current_d_gate (per_second)",
        "d_inf": "d_inf in component L_type_calcium_current_d_gate (dimensionless)",
        "tau_d": "tau_d in component L_type_calcium_current_d_gate (second)",
        "f_inf": "f_inf in component L_type_calcium_current_f_gate (dimensionless)",
        "tau_f": "tau_f in component L_type_calcium_current_f_gate (second)",
        "f2_inf": "f2_inf in component L_type_calcium_current_f2_gate (dimensionless)",
        "tau_f2": "tau_f2 in component L_type_calcium_current_f2_gate (second)",
        "tau_r": "tau_r in component transient_outward_potassium_current_r_gate (second)",
        "r_infinity": "r_infinity in component transient_outward_potassium_current_r_gate (dimensionless)",
        "tau_qfast": "tau_qfast in component transient_outward_potassium_current_qfast_gate (second)",
        "qfast_infinity": "qfast_infinity in component transient_outward_potassium_current_qfast_gate (dimensionless)",
        "tau_qslow": "tau_qslow in component transient_outward_potassium_current_qslow_gate (second)",
        "qslow_infinity": "qslow_infinity in component transient_outward_potassium_current_qslow_gate (dimensionless)",
        "tau_qa": "tau_qa in component sustained_outward_potassium_current_qa_gate (second)",
        "qa_infinity": "qa_infinity in component sustained_outward_potassium_current_qa_gate (dimensionless)",
        "alpha_qa": "alpha_qa in component sustained_outward_potassium_current_qa_gate (per_second)",
        "beta_qa": "beta_qa in component sustained_outward_potassium_current_qa_gate (per_second)",
        "tau_qi": "tau_qi in component sustained_outward_potassium_current_qi_gate (second)",
        "alpha_qi": "alpha_qi in component sustained_outward_potassium_current_qi_gate (per_second)",
        "beta_qi": "beta_qi in component sustained_outward_potassium_current_qi_gate (per_second)",
        "qi_infinity": "qi_infinity in component sustained_outward_potassium_current_qi_gate (dimensionless)",
        "g_ACh": "g_ACh in component acetylcholine_sensitive_current (microS)",
        "beta_achf": "beta_achf in component acetylcholine_sensitive_current_achf_gate (per_second)",
        "beta_achs": "beta_achs in component acetylcholine_sensitive_current_achs_gate (per_second)",
        "i_up": "i_up in component intracellular_calcium_concentration (millimolar_per_second)",
        "i_tr": "i_tr in component intracellular_calcium_concentration (millimolar_per_second)",
        "i_rel": "i_rel in component intracellular_calcium_concentration (millimolar_per_second)",
        "i_diff": "i_diff in component intracellular_calcium_concentration (millimolar_per_second)",
        "diff_f_TC": "diff_f_TC in component intracellular_calcium_concentration (per_second)",
        "diff_f_TMC": "diff_f_TMC in component intracellular_calcium_concentration (per_second)",
        "diff_f_TMM": "diff_f_TMM in component intracellular_calcium_concentration (per_second)",
        "diff_f_CMi": "diff_f_CMi in component intracellular_calcium_concentration (per_second)",
        "diff_f_CMs": "diff_f_CMs in component intracellular_calcium_concentration (per_second)",
        "diff_f_CQ": "diff_f_CQ in component intracellular_calcium_concentration (per_second)",
        "diff_f_CSL": "diff_f_CSL in component intracellular_calcium_concentration (per_second)",
    }

    return legend_states, legend_algebraic, legend_voi, legend_constants


def init_consts():
    """
    Инициализация констант и начальных значений фазовых переменных модели.
    Возвращает два словаря: states (фазовые переменные) и constants (константы).
    """
    # Инициализация констант
    constants = {
        "R": 8314.472,          
        "T": 310,               
        "F": 96485.3415,       
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

    # Инициализация состояний
    states = {
        "V": -49.7094187908202,
        "y": 0.0462303183096481,
        "paf": 0.192515363116553,
        "pas": 0.0797182955833868,
        "pik": 0.949023698965401,
        "Casub": 0.000160310601192365,
        "m": 0.143642247226618,
        "h1": 0.0243210273637729,
        "h2": 0.0157156121147801,
        "d": 0.00179250298710316,
        "f": 0.975550840189597,
        "f2": 0.774394220125623,
        "r": 0.0296516611999521,
        "q_fast": 0.899732315818241,
        "q_slow": 0.190111737767474,
        "qa": 0.476404610622697,
        "qi": 0.542303657353244,
        "achf": 0.550559577208797,
        "achs": 0.567277036232041,
        "Cai": 0.000184969821581882,
        "Ca_up": 1.11092514657408,
        "Ca_rel": 0.296249516481577,
        "f_TC": 0.0356473236675985,
        "f_TMC": 0.443317425115817,
        "f_TMM": 0.491718960234865,
        "f_CMi": 0.0723007987059414,
        "f_CMs": 0.0630771339141488,
        "f_CQ": 0.261430602900137, 
        "f_CSL": 4.1497704886823e-5,
    }

    # Вычисление производных констант
    constants = compute_derived_constants(constants)

    return states, constants


def compute_derived_constants(constants):
    """
    Вычисляет производные константы на основе базовых значений.
    """
    constants["RTONF"] = (constants["R"] * constants["T"]) / constants["F"]
    constants["k34"] = constants["Nao"] / (constants["K3no"] + constants["Nao"])
    constants["E_K"] = constants["RTONF"] * log(constants["Kc"] / constants["Ki"])
    constants["E_Na"] = constants["RTONF"] * log(constants["Nao"] / constants["Nai"])
    constants["E_K_1"] = constants["RTONF"] * log(constants["Kc"] / constants["Ki"])
    constants["k43"] = constants["Nai"] / (constants["K3ni"] + constants["Nai"])
    constants["V_up"] = 0.0116000 * constants["V_cell"]
    constants["V_rel"] = 0.00120000 * constants["V_cell"]
    constants["V_sub"] = 0.0100000 * constants["V_cell"]
    constants["Vi"] = 0.460000 * constants["V_cell"] - constants["V_sub"]

    return constants