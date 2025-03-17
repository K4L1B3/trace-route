import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calcula a distância em linha reta entre dois pontos usando a fórmula de Haversine.
    Retorna a distância em quilômetros.
    """
    # Raio da Terra em km
    R = 6371.0
    
    # Converter coordenadas de graus para radianos
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Diferença entre as coordenadas
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Fórmula de Haversine
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    
    return distance  