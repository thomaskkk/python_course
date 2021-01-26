from python_pytest.cheque import cheque_por_extenso


#0.05 -> cinco centavos
def test_centavos():
    # given
    num = 0.05
    # when
    result = cheque_por_extenso(num)
    # then
    assert result == "cinco centavos"

#2.25 -> dois reais e vinte e cinco centavos
def test_reais():
    # given
    num = 2.25
    # when
    result = cheque_por_extenso(num)
    # then
    assert result == "dois reais e vinte e cinco centavos"

    #15415.16 -> quinze mil quatrocentos e quinze reais e dezesseis centavos
def test_milhar():
    # given
    num = 15415.16
    # when
    result = cheque_por_extenso(num)
    # then
    assert result == "quinze mil quatrocentos e quinze reais e dezesseis centavos"




