import streamlit as st
import os.path
import csv
import pandas as pd
#import datetime
st.write("""
# MoneyTracker v1.0
Programma per gestire le *finanze* personali
""")

data=st.date_input("Movimento relativo al giorno (YYYY/MM/DD):")
#data=st.date_input("per il giorno", value=None, key=None, help=None
#st.write('Hai selezionato:', data)

if st.button('Hit me'):
    st.write('Pippo')
else:
    pass

options = st.selectbox('Che tipo di movimento stai per introdurre?',('-----', 'Entrata', 'Uscita'))
#st.write('Hai selezionato:', options)
if options=="-----":
    option_elem=0
    pass
elif options=='Uscita':
    option_elem = st.selectbox('Che tipo di uscita è?',('Mangiare fuori', 'Spesa base (benzina/alimenti)', 'Sfizi', 'Beneficienza', 'Caffè', 'Amazon', 'Regali obbligati'))
    st.write('Hai selezionato una ',options,'avvenuta il giorno ',str(data),'con causale ',  option_elem)
elif options=='Entrata':
    option_elem = st.selectbox('Che tipo di entrata è?',('Stipendio', 'Bonifico Parenti', 'PoliMi'))
    st.write('Hai selezionato una ',options,', avvenuta il giorno ',str(data),', con causale ',  option_elem)

tripletta=st.radio("In che range è la cifra?", ('0-200 €','201-1000 €','1001-3000 €'))
cifra=0

if tripletta=="0-200 €":
    cifra=st.slider("Inserisci la cifra: ", 0,200)
elif tripletta=='201-1000 €':
    cifra=st.slider("Inserisci la cifra: ", 201,1000)
elif tripletta=='1001-3000 €':
    cifra=st.slider("Inserisci la cifra: ", 1001,3000)

if cifra!=0:
    st.write('Ora inizio ad elaborare il file')
    inserimento=[data,cifra, option_elem, options] 
    st.write('Gli elementi inseriti sono',str(data),str(cifra),'€', option_elem, options)
    end_this_op = st.selectbox('Hai terminato questa operazione?',('NO', 'YES'))
    if end_this_op=='NO':
        st.write('Sbrigati e poi torna qua a mettere YES')
    elif end_this_op=='YES':
        new_item=inserimento
        
        csv.register_dialect('standard',lineterminator='\n')
        anno=str(data)[0:4]
        mese=str(data)[5:7]
        filetabella="Spese_"+anno+"_"+(mese)+".csv"
        file_exists=os.path.exists(filetabella)
        if file_exists==True:
            st.write("Il file di questo mese esiste già! Che fortuna!")
        else:
            intitolazione=["Giorno","Mese","Cifra","Motivo","E/U"]  
            with open(filetabella, 'w') as file_base:
                writerobj=csv.writer(file_base, dialect='standard')
                writerobj.writerow(intitolazione)

        with open(filetabella, 'a') as file:
            writerobj=csv.writer(file, dialect='standard')
            writerobj.writerow(new_item)
        ########################################################################
        exit=st.radio("Vuoi inserire altre operazioni?", ('NO','SI'))
        #if exit=="SI":
         #   st.write("RICOMINCIAMO!")
        #else:
         #   st.write("Ciao grazie per avere utilizzato questo tool!")
else:
    pass
            
