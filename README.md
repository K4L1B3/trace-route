
# 🌍 Business Distance Calculator 🔍

## 📊 Análise de Distâncias para Empresas de Energia e Gás

Um projeto elegante que permite analisar distâncias entre sua localização central e empresas do setor energético, facilitando decisões estratégicas baseadas em dados geográficos.

---

## ✨ Funcionalidades
- 📥 **Importação de Dados**: Lê e processa planilhas Excel existentes através da biblioteca pandas, permitindo trabalhar com grandes bases de dados empresariais
- 🔎 **Filtragem Inteligente**: Identifica automaticamente empresas de energia e gás em grandes conjuntos de dados
- 📍 **Geocodificação Precisa**: Converte endereços brasileiros em coordenadas geográficas
- 📏 **Cálculo de Distâncias**: Utiliza a fórmula matemática de Haversine para determinar distâncias precisas em linha reta
- 📊 **Exportação para Excel**: Gera planilhas detalhadas com todos os dados e métricas calculadas

## 🚀 Começando

### Pré-requisitos

- 🐍 Python 3.9 ou superior
- 📦 Poetry para gerenciamento de dependências
- 🔑 Chave de API do Google (com acesso a Geocoding API)

### 📥 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/business-distance-calculator.git
   cd business-distance-calculator
   ```

2. Instale as dependências com Poetry:
   ```bash
   poetry install
   ```

3. Configure o arquivo `.env` na raiz do projeto:
   ```
   GOOGLE_API_KEY=sua_chave_api_do_google
   ```

## 🔧 Como Usar

1. Prepare sua planilha de dados no formato Excel (.xlsx) e coloque-a na pasta `data/` com o nome `business_data.xlsx`

2. Execute o programa:
   ```bash
   poetry run python main.py
   ```

3. Os resultados serão salvos em `data/business_data_filtrado_com_distancias_COMPLETO.xlsx`

4. Para testes com um conjunto menor de dados, descomente as linhas 133-142 no arquivo `main.py`

## 📁 Estrutura do Projeto

```
business-distance-calculator/
├── data/
│   ├── business_data.xlsx                    # Planilha com dados de entrada
│   └── business_data_filtrado_com_distancias_COMPLETO.xlsx  # Resultados
├── main.py                                   # Script principal
├── calculate_distances.py                    # Implementação do algoritmo Haversine
├── filter.py                                 # Função de filtragem de empresas
├── formatter.py                              # Formatação de endereços brasileiros
├── .env                                      # Variáveis de ambiente (não versionado)
├── pyproject.toml                            # Configurações do Poetry
└── README.md                                 # Este arquivo
```

## 📊 Formato dos Dados

A planilha de entrada deve conter campos como:
- Tipo Logradouro (ex: AVENIDA, RUA)
- Logradouro (nome da rua)
- Numero (número do estabelecimento)
- Complemento
- Bairro
- Municipio
- UF (estado)
- CEP
- Ramo de Atividade

## 🔐 Segurança

- **Nunca** compartilhe sua chave de API do Google
- O arquivo `.env` está incluído no `.gitignore` para proteção
- Considere configurar restrições de domínio/IP para sua chave de API no console do Google Cloud

## 🔍 Personalização

- Para modificar os critérios de filtragem, edite a função em `filter.py`
- A fórmula de cálculo de distância pode ser customizada em `calculate_distances.py`
- Ajuste o formato de endereços em `formatter.py` conforme necessário

---

## 💡 Observações Importantes

- O cálculo de distância usa a fórmula de Haversine, que fornece a distância em linha reta ("como um pássaro voa")
- Para trajetos reais por estradas, seria necessário usar a API Routes do Google (implementação parcial incluída mas não utilizada)
- Geocodificação em massa pode gerar custos na API do Google - monitore seu uso!

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

---

Desenvolvido com ❤️ usando Python e Google APIs
