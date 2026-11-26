from romfart import calcDist, calcFuel, welcomeTravaleer
import pytest

@pytest.mark.parametrize("fart,timer,forventet", 
                         [
                            (1000,10,10000),
                            (100,10,1000),
                            (1000,20,20000)
                         ])
def test_calcDist(fart, timer, forventet):
    #assert calcDist(1000,10) == 10000, "Feil i calcDist. Kanskje speed ikke blir ganget med hours"
    assert calcDist(fart, timer) == forventet, "Feil i calcDist. Kanskje speed ikke blir ganget med hours"

def test_calcFuel():
    assert calcFuel(40,2) == 80, "Feilmelding"

def test_distWith0Hours():
    assert calcDist(1000,0) == 0, "egg"

def test_calcDist_withLessThan0Hours():
    with pytest.raises(ValueError):
        calcDist(-100,-1)

def test_desimal():
    assert 0.1 + 0.2 == pytest.approx(0.3), "The floatingpoint error has floatingpoint errored"

def test_welcomeTravaleer():
    assert welcomeTravaleer("Loopert") == "Well hello there Travaleer Loopert. How do you do fellow space Travaleer?"