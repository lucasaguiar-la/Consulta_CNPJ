from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()
def salvar_planilha(dados):
    df_acumulado = pd.DataFrame(dados)

    with pd.ExcelWriter(os.getenv("PASTA_SALVOS"), engine="openpyxl") as writer:
        print(f"\nTotal de consultas: {len(dados)}")

        df_acumulado.to_excel(writer, sheet_name="CNPJs", index=False)
        print("\nPlanilha de CNPJs criada com sucesso!\n")