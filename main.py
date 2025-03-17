import os
import time
import pandas as pd
import requests
from dotenv import load_dotenv
from filter import filter_energia_gas
from formatter import format_address
from calculate_distances import haversine_distance

def get_geocode(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": api_key}
    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("status") == "OK" and len(data["results"]) > 0:
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        print(f"[Geocode] Erro ou endereço não encontrado: {address} -> {data.get('status')}")
        return None, None

def get_distance_v2(origin_lat, origin_lon, dest_lat, dest_lon, api_key):
    url = f"https://routes.googleapis.com/directions/v2:computeRoutes?key={api_key}"
    
    headers = {
        "X-Goog-FieldMask": "routes.distanceMeters,routes.duration,routes.polyline.encodedPolyline",
        "Content-Type": "application/json"
    }
    
    payload = {
        "origin": {
            "location": {
                "latLng": {"latitude": origin_lat, "longitude": origin_lon}
            }
        },
        "destination": {
            "location": {
                "latLng": {"latitude": dest_lat, "longitude": dest_lon}
            }
        },
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    if "error" in data:
        print(f"[Routes API] Erro: {data['error'].get('message')}")
        return None, None

    routes = data.get("routes", [])
    if not routes:
        print(f"[Routes API] Nenhuma rota encontrada. Resposta: {data}")
        return None, None

    route = routes[0]
    distance_meters = route.get("distanceMeters")
    duration_str = route.get("duration")
    return distance_meters, duration_str

def annotate_distances(df, origin_lat, origin_lon, api_key):
    """
    Anota as distâncias entre um ponto de origem e os endereços das empresas.
    Usa a fórmula de Haversine para calcular a distância em linha reta.
    """
    
    df = df.copy()
    
    geocoded_lat = []
    geocoded_lon = []
    distances_km = []
    distances_m = []
    
    for _, row in df.iterrows():
        try:
            endereco = format_address(row)
            print(f"Geocodificando: {endereco}")
            
            # Ainda precisa geocodificar o endereço para obter as coordenadas
            lat, lon = get_geocode(endereco, api_key)
            
            if lat is not None and lon is not None:
                geocoded_lat.append(lat)
                geocoded_lon.append(lon)
                
                # Calcular distância usando o método de Haversine
                dist_km = haversine_distance(origin_lat, origin_lon, lat, lon)
                dist_m = dist_km * 1000  # Converter para metros
                
                distances_km.append(f"{dist_km:.2f} km")
                distances_m.append(int(dist_m))
            else:
                geocoded_lat.append(None)
                geocoded_lon.append(None)
                distances_km.append("N/A")
                distances_m.append(None)
                
        except Exception as e:
            print(f"Erro ao processar linha: {e}")
            geocoded_lat.append(None)
            geocoded_lon.append(None)
            distances_km.append("N/A")
            distances_m.append(None)
    
    df.loc[:, "geocoded_lat"] = geocoded_lat
    df.loc[:, "geocoded_lon"] = geocoded_lon
    df.loc[:, "distance_km"] = distances_km
    df.loc[:, "distance_m"] = distances_m
    
    return df

def main():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("ERRO: Variável GOOGLE_API_KEY não encontrada no .env.")
        return

    # Coordenada principal
    main_lat = -3.7342023
    main_lon = -38.505481

    # Carrega o Excel original
    df = pd.read_excel("./data/business_data.xlsx")

    # Filtra para Energia e Gás
    df_filtered = filter_energia_gas(df)
    print(f"Filtered data shape: {df_filtered.shape}")

    # Código de teste com 5 linhas
    # df_filtered_5 = df_filtered.head(5).copy()
    # print(f"Processando apenas {len(df_filtered_5)} linhas...")
    #
    # # Anotando distâncias (somente nessas 5 linhas)
    # df_with_distances = annotate_distances(df_filtered_5, main_lat, main_lon, api_key)
    #
    # # Exporta para Excel (só vai ter essas 5 linhas)
    # output_file = "./data/business_data_filtrado_com_distancias_TESTE.xlsx"
    # df_with_distances.to_excel(output_file, index=False)
    # print(f"Planilha gerada com 5 linhas de teste: {output_file}")

    print(f"Processando todas as {len(df_filtered)} linhas filtradas...")
    
    # Anotando distâncias para todas as linhas filtradas
    df_with_distances = annotate_distances(df_filtered, main_lat, main_lon, api_key)
    
    # Exporta o resultado completo para Excel
    output_file = "./data/business_data_filtrado_com_distancias_COMPLETO.xlsx"
    df_with_distances.to_excel(output_file, index=False)
    print(f"Planilha completa gerada com {len(df_filtered)} linhas: {output_file}")

if __name__ == "__main__":
    main()
