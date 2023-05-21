import pandas as pd
import streamlit as st

import src.answers as asw
from src.extraction import load_data

st.set_page_config(layout="wide")


def create_dataframe_section(df):
    st.title("Sections - Database Description")

    col_1, col_2 = st.columns(2)

    col_1.header("Database")
    col_1.dataframe(df, height=530)

    col_2.header("Data Description")

    data_description = """
                        | Coluna | Descrição |
                        | :----- | --------: |
                        | ID | Identificador da linha/registro |
                        | name | Fabricante e Modelo da Moto |
                        | selling_price | Preço de Venda |
                        | year | Ano de Fabricação da Moto |
                        | seller_type | Tipo de Vendedor - Se é vendedor pessoal ou revendedor |
                        | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
                        | km_driven | Quantidade de Quilometros percorrido pela moto |
                        | ex_showroom_price | Preço da motocicleta sem as taxas de seguro e registro |
                        | age | Quantidade de anos em que a moto está em uso |
                        | km_class | Classificação das motos conforme a quilometragem percorrida |
                        | km_per_year | Quantidade de Quilometros percorridos a cada ano |
                        | km_per_month | Quantidade de Quilometros percorridos por mês |
                        | company | Fabricante da Motocicleta |
    """

    col_2.markdown(data_description)


def create_answers_section(df):
    st.title("Main Questions Answers")

    st.header("First Round")
    st.subheader(
        "How many motorcycles are being sold by individual owners and how many motorcycles are being sold by distributors?"
    )
    asw.rd1_question_9(df)

    st.subheader("How many motorcycles being sold have had a unique owner?")
    asw.rd1_question_13(df)

    st.subheader(
        "Are motorcycles with high mileage more expensive than motorcycles with lower mileage?"
    )
    asw.rd1_question_14(df)

    st.subheader(
        "On average, are motorcycles with a single owner more expensive than other motorcycles?"
    )
    asw.rd2_question_1(df)

    st.subheader(
        "On average, do motorcycles with multiple owners also have higher mileage?"
    )
    asw.rd2_question_2(df)

    st.subheader("Which company has the highest number of registered motorcycles?")
    asw.rd2_question_7(df)

    st.subheader("Which company has the highest average price for motorcycles?")
    asw.rd3_question_2(df)

    st.subheader(
        "Is the company with the highest average price for registered motorcycles also the company with the highest number of registered motorcycles?"
    )
    asw.rd3_question_5(df)

    st.subheader("Which motorcycles are recommended for purchasing?")
    asw.rd3_question_7(df)


def create_main_layout():
    df = load_data()

    create_dataframe_section(df)

    create_answers_section(df)


if __name__ == "__main__":
    create_main_layout()
