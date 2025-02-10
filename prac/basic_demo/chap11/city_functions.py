def city_country(city,country,population=''):
    """返回一个形如'Santiago, Chile - population 5000000'的字符串。"""
    output_string = f"{city.title()},{country.title()}"
    if population:
        output_string += f"-population {population}"
        return output_string
    return output_string

# print(city_country('santiago', 'chile'))