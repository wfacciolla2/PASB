import streamlit as st

with open('style.css') as f
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)
st.markdown(f'''
    # Ficha para atendimento
    ## Pronto Atendimento
    
    Prefeitura Municipal de Santa Branca
''')
