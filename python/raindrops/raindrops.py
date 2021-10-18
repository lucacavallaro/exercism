factor_dict = {
    3: "Pling",
    5: "Plang",
    7: "Plong",
}

def convert(number):
    result = ""
    for factor, value in factor_dict.items():
        if number % factor == 0:
            result += value
    return result or str(number)
