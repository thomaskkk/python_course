#!/usr/bin/env python3

def cheque_por_extenso(number):
    
    #extract centavos
    if round(number % 1, 2) != 0:
        result_dict_centavos = numero_para_extenso(int((str(number)).split(".")[1]))
        if len(result_dict_centavos) > 1:
            result_string_centavos = " e ".join(result_dict_centavos)
        else:
            result_string_centavos = ''.join(result_dict_centavos)
        result_string_centavos += " centavos"
    #extract reais
    if int(number) >= 1:
        result_dict_reais = numero_para_extenso(int(number))
        if len(result_dict_reais) > 1:
            result_string_reais = " e ".join(result_dict_reais)
        else:
            result_string_reais = ''.join(result_dict_reais)
        result_string_reais += " reais"

    #return string
    if result_string_reais and result_string_reaisresult_string_centavos:
        return result_string_reais + " e " + result_string_centavos
    elif result_string_reais:
        return result_string_reais
    elif result_string_centavos:
        return result_string_centavos

def numero_para_extenso(number):
    ''''Return a list of the numbers as we read them'''
    
    extenso_20 = {
        20:"vinte", 19:"dezenove", 18:"dezoito", 17:"dezessete", 16:"dezesseis", 15:"quinze", 14:"quatorze", 13:"treze", 12:"doze", 11:"onze",
        10:"dez", 9:"nove", 8:"oito", 7:"sete", 6:"seis", 5:"cinco", 4:"quatro", 3:"tres", 2:"dois", 1:"um"
    }
    extenso_90 = {
        90:"noventa", 80:"oitenta", 70:"setenta", 60:"sessenta", 50:"cinquenta", 40:"quarenta", 30:"trinta"
    }
    extenso_1000 = {
        1000:"mil", 900:"novecentos", 800:"oitocentos", 700:"setecentos", 600:"seiscentos", 500:"quinhentos", 400:"quatrocentos", 300:"trezentos", 200:"duzentos", 100:"cento"
    }
    
    result_dict = []
    while number > 0 :
        if  number >= 30 and number < 90:
            for key, value in extenso_90.items():
                if number == key:
                    result_dict.append(value)
                    number -= key
        elif number < 30:
            for key, value in extenso_20.items():
                if number == key:
                    result_dict.append(value)
                    number -= key
            if 
    return result_dict

if __name__ == "__main__":
    print(numero_para_extenso(21))