import elements as el

# FODO circular accelerator from Klaus Wille Chapter 3.13.3
D1 = el.Drift('D1', length=0.55)
Q1 = el.Quad('Q1', length=0.2, k1=1.2)
B1 = el.Bend('B1', length=1.5, angle=0.392701, e1=0.1963505, e2=0.1963505)
Q2 = el.Quad('Q2', length=0.4, k1=-1.2)
fodo = el.Cell('fodo-cell', [Q1, D1, B1, D1, Q2, D1, B1, D1, Q1])
ring = el.MainCell('fodo-ring', [fodo] * 8)

lin = el.LinBeamDyn(ring)
twiss = lin.get_twiss(betatron_phase=True)


def test_beta():
    beta_x_start = twiss.beta_x[0]
    beta_x_end = twiss.beta_x[-1]
    beta_y_start = twiss.beta_y[0]
    beta_y_end = twiss.beta_y[-1]
    assert 9.8176 == round(beta_x_start, 4)
    assert 9.8176 == round(beta_x_end, 4)
    assert 1.2376 == round(beta_y_start, 4)
    assert 1.2376 == round(beta_y_end, 4)


def test_dispersion():
    eta_x_start = twiss.eta_x[0]
    eta_x_end = twiss.eta_x[-1]
    assert 3.4187 == round(eta_x_start, 4)
    assert 3.4187 == round(eta_x_end, 4)


def test_tune_integer():
    assert 2 == round(twiss.tune_x)  # depends on number of matrices
    assert 3 == round(twiss.tune_y)  # depends on number of matrices


def test_tune_fractional():
    assert 0.8970 == round(1 - twiss.tune_x_fractional, 4)
    assert 0.5399 == round(1 - twiss.tune_y_fractional, 4)