import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
from streamlit.logger import get_logger
import fitur

LOGGER = get_logger(__name__)


FITUR = OrderedDict(
    [
        ("—", (fitur.intro, None)),
        (
            "Fitur 1.a",
            (
                fitur.fitur_a,
                """
                Jumlah produksi minyak mentah terhadap waktu (tahun) dari suatu negara
                """,
            ),
        ),
        (
            "Fitur 1.b",
            (
                fitur.fitur_b,
                """
                Negara dengan produksi minyak mentah terbesar pada suatu tahun
                """,
            ),
        ),
        (
            "Fitur 1.c",
            (
                fitur.fitur_c,
                """
                Negara dengan total produksi minyak mentah keseluruhan tahun terbesar
                """,
            ),
        ),
        (
            "Fitur 1.d",
            (
                fitur.fitur_d,
                """
                Summary
                """,
            ),
        ),
        (
            "Fitur tambahan",
            (
                fitur.fitur_tambahan,
                """
                Membandingkan produksi minyak mentah antar dua negara tiap tahunnya
                """,
            ),
        ),
    ]
)


def run():
    demo_name = st.sidebar.selectbox("Pilih fitur", list(FITUR.keys()), 0)
    demo = FITUR[demo_name][0]

    if demo_name == "—":
        pass
    else:
        st.markdown("# %s" % demo_name)
        description = FITUR[demo_name][1]
        if description:
            st.write(description)

        for i in range(10):
            st.empty()

    demo()


if __name__ == "__main__":
    run()