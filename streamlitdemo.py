import streamlit as st
#import datetime




st.write("""
# MoneyTracker v1.0
Programma per gestire le *finanze* personali
""")

#d = st.date_input("When's your birthday") #di default mette la data di oggi
#d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
#st.write('Your birthday is:', d)

data=st.date_input("Movimento relativo al giorno (YYYY/MM/DD):")
#data=st.date_input("per il giorno", value=None, key=None, help=None
#st.write('Hai selezionato:', data)


options = st.selectbox('Che tipo di movimento stai per introdurre?',('-----', 'Entrata', 'Uscita'))
#st.write('Hai selezionato:', options)
if options=="-----":
    pass
elif options=='Uscita':
    option_uscita = st.selectbox('Che tipo di uscita è?',('Mangiare fuori', 'Spesa base (benzina/alimenti)', 'Sfizi', 'Beneficienza', 'Caffè', 'Amazon', 'Regali obbligati'))
    st.write('Hai selezionato una ',options,'avvenuta il giorno ',str(data),'con causale ',  option_uscita)
elif options=='Entrata':
    option_entrata = st.selectbox('Che tipo di entrata è?',('Stipendio', 'Bonifico Parenti', 'PoliMi'))
    st.write('Hai selezionato una ',options,', avvenuta il giorno ',str(data),', con causale ',  option_entrata)

tripletta=st.radio("In che range è la cifra?", ('0-200 €','201-1000 €','1001-3000 €'))


if tripletta=="0-200 €":
    cifra=st.slider("Inserisci la cifra: ", 0,200)
elif tripletta=='201-1000 €':
    cifra=st.slider("Inserisci la cifra: ", 201,1000)
elif tripletta=='1001-3000 €':
    cifra=st.slider("Inserisci la cifra: ", 1001,3000)

st.write(str(cifra), '€')
