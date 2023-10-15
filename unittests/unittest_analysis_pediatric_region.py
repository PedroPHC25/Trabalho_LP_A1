from analysis_pediatric_regions import calcular_estatisticas

def test_calcular_estatisticas():
    dados = (['CENTRO-OESTE', 'NORDESTE', 'NORTE', 'SUDESTE', 'SUL'], [30450, 55476, 22550, 150046, 35870])
    estatisticas = calcular_estatisticas(dados)
    
    assert 'Média' in estatisticas
    assert 'Mediana' in estatisticas
    assert 'Desvio Padrão' in estatisticas
    assert 'Variância' in estatisticas
    
    assert isinstance(estatisticas['Média'], float)
    assert isinstance(estatisticas['Mediana'], (int, float))  # Aceita tanto inteiros quanto floats
    assert isinstance(estatisticas['Desvio Padrão'], float)
    assert isinstance(estatisticas['Variância'], float)


if __name__ == "__main__":
    test_calcular_estatisticas()
    print("Todos os testes passaram.")
