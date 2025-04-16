import streamlit as st

def convert_units(value,unit_from_unit_to):
    
    conversion ={
       "meter_kilometer": 0.001,
       "kilometer_meter":1000,
       "gram_kilogram": 0.001,
       "kil0gram_gram":1000,

    }
    key =f"{"unit_from"}_{"unit_to"}"

    if key in conversion:
        conversion = conversion[key]
        return value * conversion
    else:
        return"Coversion not supported"
    
    st.title("Unit Converter") 

    value =st.number_input("Enter the value:")
    
    unit_from =st.selectbox("Converter from:",["meter","kilometer","gram, Kilogram"])

    unit_to =st.selectbox("Convert to:",[ "meter","kilometer","gram","kilogram"])

    if st.button("Convert"):
        result = convert_units(value, unit_from_unit_to)
        st.write(f"Conveted value:{result}")
    
 




