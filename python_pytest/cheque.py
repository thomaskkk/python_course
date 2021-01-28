#!/usr/bin/env python3

def cheque_por_extenso(number):
    
    #Fix round
    number = round(number, 2)
    #extract centavos
    result_string_centavos = ""
    if number % 1 != 0:
        result_dict_centavos = numero_para_extenso((str(number)).split(".")[1])
        if len(result_dict_centavos) > 1:
            result_string_centavos = " e ".join(result_dict_centavos)
        else:
            result_string_centavos = ''.join(result_dict_centavos)
        result_string_centavos += " centavos"
    #extract reais
    result_string_reais = ""
    if int(number) >= 1:
        result_dict_reais = numero_para_extenso(int(number))
        if len(result_dict_reais) > 1:
            result_string_reais = " e ".join(result_dict_reais)
        else:
            result_string_reais = ''.join(result_dict_reais)
        result_string_reais += " reais"

    #return string
    if result_string_centavos != "" and result_string_reais != "":
        return result_string_reais + " e " + result_string_centavos
    else:
        return result_string_reais + result_string_centavos

def numero_para_extenso(number_as_str):
    ''''Return a list of the numbers as we read them'''
    extenso_9 = {
        9:"nove", 8:"oito", 7:"sete", 6:"seis", 5:"cinco", 4:"quatro", 3:"tres", 2:"dois", 1:"um"
    }
    extenso_19 = {
        19:"dezenove", 18:"dezoito", 17:"dezessete", 16:"dezesseis", 15:"quinze", 14:"quatorze", 13:"treze", 12:"doze", 11:"onze", 10:"dez"
    }
    extenso_90 = {
        9:"noventa", 8:"oitenta", 7:"setenta", 6:"sessenta", 5:"cinquenta", 4:"quarenta", 3:"trinta",  2:"vinte"
    }
    extenso_900 = {
        9:"novecentos", 8:"oitocentos", 7:"setecentos", 6:"seiscentos", 5:"quinhentos", 4:"quatrocentos", 3:"trezentos", 2:"duzentos", 1:"cento"
    }
    
    split_numbers = []
    if len(str(number_as_str)) > 1:
        split_numbers = [int(i) for i in number_as_str]
        split_numbers.reverse()
    else:
        split_numbers.append(number_as_str)

    result_dict = []
    team_10 = False
    for p in range(len(split_numbers)):
        if p == 2 and split_numbers[p] != 0:
            result_dict.insert(0, extenso_900.get(split_numbers[p]))
        elif p == 1 and split_numbers[p] == 1:
            #special case check number order 1 get result and break
            number = split_numbers[-2:]
            number.reverse()
            number = ''.join(map(str, number))
            result_dict.pop()
            result_dict.append(extenso_19.get(int(number)))
            break
        elif p == 1 and split_numbers[p] != 0:
            result_dict.insert(0, extenso_90.get(split_numbers[p]))
        elif p == 0 and split_numbers[p] != 0:
            result_dict.insert(0, extenso_9.get(split_numbers[p]))
            
    return result_dict

if __name__ == "__main__":
    print(cheque_por_extenso(2.15))