import flet as ft
import pandas as pd
import openpyxl
import logging
import asyncio
import os
from logging import error, info

# Configuração do logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(),
    ],
)


def main(page: ft.Page):
    """
    Função principal da aplicação Flet.
    """
    page.title = "Calculo Regressão LInear"
    page.window.width = 500
    page.window.height = 350
    page.window.resizable = False

    texto_etapas = ft.Text(value="Aguardando Invomações...", size=16)
    carregando = ft.Ref[ft.ProgressRing]()

    # Botão Executar
    botao_executar = ft.ElevatedButton("Executar", width=200, on_click=executar_validacao)

    def atualizar_texto(nova_etapa: str):
        texto_etapas.value = nova_etapa
        page.update()

    # Alerta inicial
    def fechar_alerta(e):
        page.dialog.open = False
        page.dialog = None
        page.update()

    alerta = ft.AlertDialog(
        modal=True,
        title=ft.Text(
            "Antes de importar os arquivos para validação",
            size=20,
            weight="bold",
            text_align=ft.TextAlign.CENTER,
        ),
        content=ft.Column(
            [
                ft.Text(
                    "\n• Verifique se Inventário foi realizado no Varejo Fácil; \n\n"
                    "• Salve os arquivos, que serão importados, com a extensão .xlsx.",
                    size=15,
                    weight="italic",
                    text_align=ft.TextAlign.JUSTIFY,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        actions=[ft.ElevatedButton("Fechar", on_click=fechar_alerta)],
    )

    page.dialog = alerta
    alerta.open = True
    page.update()

    page.add(
        ft.Stack(
            [
                # Elementos da tela principal
                ft.Column(
                    [
                        upload_vd,
                        upload_vf,
                        botao_executar,
                        texto_etapas,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                # Loading sobreposto (inicialmente invisível)
                ft.ProgressRing(
                    visible=False,
                    ref=carregando,
                    width=40,
                    height=40,
                    left=140,
                    right=140,
                    top=15,
                    bottom=80,
                ),
            ],
            width=450,
            height=270,
        )
    )


ft.app(target=main)