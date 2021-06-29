import streamlit as st
#import datetime




st.write("""
# My first app
Hello *world!*
""")

#d = st.date_input("When's your birthday") #di default mette la data di oggi
#d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
#st.write('Your birthday is:', d)

data=st.date_input("per il giorno")
#data=st.date_input("per il giorno", value=None, key=None, help=None
st.write(data)


options = st.selectbox('Che tipo di movimento stai per introdurre?',('-----', 'Entrata', 'Uscita'))
st.write('You selected:', options)
if options=="-----":
    pass
elif options=='Uscita':
    option_uscita = st.selectbox('Che tipo di uscita è?',('Mangiare fuori', 'Spesa base (benzina/alimenti)', 'Sfizi', 'Beneficienza', 'Caffè', 'Amazon', 'Regali obbligati'))
    st.write('You selected:', option_uscita)
else:
    option_entrata = st.selectbox('Che tipo di entrata è?',('Stipendio', 'Bonifico Parenti', 'PoliMi'))
    st.write('You selected:', option_entrata)