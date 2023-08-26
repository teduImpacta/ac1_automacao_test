def cal_desc(value, desc):
    desc_value = (value / 100) * desc
    return round(value - desc_value, 2)

def calc_sal(valor_hora, qtd_aula, inss):
    return cal_desc(valor_hora * qtd_aula, inss)

def calc_9desc(valor):
    return cal_desc(valor, 9)

def calc_sub_desc(valor, desc):
    return valor - desc

def cal_tax(valor):
    gorjeta = round((valor / 100) * 10, 2)
    return (round(valor + gorjeta, 2), gorjeta)