import json

with open('tres.json') as f:
    dados = json.load(f)

faturamento_diario = [d['faturamento'] for d in dados['faturamento_diario'] if d['faturamento'] > 0]

menor_faturamento = min(faturamento_diario)

maior_faturamento = max(faturamento_diario)

media_faturamento = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_da_media = sum(1 for f in faturamento_diario if f > media_faturamento)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
