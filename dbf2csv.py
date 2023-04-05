from simpledbf import Dbf5

try:
    entrada_dbf = input('dbf file name: ')

    saida_csv = input('output file name: ')

    dbf = Dbf5(entrada_dbf)
    dbf.to_csv(saida_csv)

except Exception as e:
    print(f"Erro {e}")