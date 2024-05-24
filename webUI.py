import streamlit as st

def main():
    st.title("Pizza Calculator")
    
    st.write("Welcome to the Pizza Calculator!")
    
    num_pizzas = st.number_input("How many pizzas?", min_value=1, step=1)
    
    hydration_rate = st.number_input("Hydration rate (default is 0.7)", value=0.7, min_value=0.0, step=0.05)
    
    # flour + water per pizza = 220g
    flour = 220 / (1 + hydration_rate) * num_pizzas
    water = flour * hydration_rate
    
    st.subheader("Recipe:")
    st.write(f"{int(flour)}g flour")
    st.write(f"{int(water)}g water")
    st.write(f"{num_pizzas * 5}g salt")
    st.write(f"{round(num_pizzas * 0.1,1)}g yeast")

if __name__ == "__main__":
    main()
