import pytest
import main

def test_calc_sal():
    values = [
        [6.25, 160, 1.3, 987],
        [20.5, 240, 1.7, 4836.36],
        [13.9, 200, 6.48, 2599.86],
    ]

    for value in values:
        hora = value[0]
        aula = value[1]
        inss = value[2]
        result = value[3]
        assert main.calc_sal(hora, aula, inss) == result

def test_calc_9desc():
    values =[
        [100, 91.00],
        [1500, 1365.00],
        [60000, 54600.00],
    ]

    for value in values:
        assert main.calc_9desc(value[0]) == value[1]

def test_calc_sub_desc():
    values = [
        [500.00, 50.00, 450.00],
        [10500.00, 500.00, 10000.00],
        [90.00, 0.80, 89.20],
    ]

    for value in values:
        preco = value[0]
        desc = value[1]
        result = value[2]
        assert main.calc_sub_desc(preco, desc) == result

def test_cal_tax():
    values = [
        [75.00, 82.50, 7.5],
        [125, 137.50, 12.5],
        [350.87, 385.96, 35.09],
    ]

    for value in values:
        valor = value[0]
        total = value[1]
        gorjeta = value[2]

        total_conta, gorjeta_conta = main.cal_tax(valor)

        assert total == total_conta and gorjeta == gorjeta_conta