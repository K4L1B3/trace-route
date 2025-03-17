def format_address(row):
    """
    Builds a Brazilian address string using fields like:
      - Tipo Logradouro (e.g., 'AVENIDA', 'RUA')
      - Logradouro (street name)
      - Numero (house number)
      - Complemento (additional info)
      - Bairro (neighborhood)
      - Municipio (city)
      - UF (state)
      - CEP (postal code)

    Adjust this function according to your DataFrame's column names and needs.
    """
    # Converte todos os valores para string
    address_type = str(row.get("Tipo Logradouro", ""))
    street_name = str(row.get("Logradouro", ""))
    number = str(row.get("Numero", ""))
    complement = str(row.get("Complemento", ""))
    neighborhood = str(row.get("Bairro", ""))
    city = str(row.get("Municipio", ""))
    state = str(row.get("UF", ""))
    postal_code = str(row.get("CEP", ""))

    # Basic construction, for example:
    # "AVENIDA EUSEBIO DE QUEIROZ, 3993 - SALA 4 - A108, CENTRO, Eusebio - CE, 61760046"
    address_string = f"{address_type} {street_name}, {number}"

    # Optionally add complement if it exists and is not something like "S/N"
    if complement and complement.upper() not in ("S/N", "SN"):
        address_string += f" - {complement}"

    # Add neighborhood, city, and state
    if neighborhood:
        address_string += f", {neighborhood}"
    if city:
        address_string += f", {city}"
    if state:
        address_string += f" - {state}"

    # Finally add the postal code (CEP)
    if postal_code:
        address_string += f", {postal_code}"

    # You can also append ", Brazil" if needed:
    # address_string += ", Brazil"

    return address_string
