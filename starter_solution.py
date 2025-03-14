import streamlit as st

# You have just opened a new pizzeria and want to build a dashboard that allows you to create and order your own pizzas
# and display information about the process.
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    # Set a "title" for your Pizza Dashboard!
    st.title("Pizza Dashboard")

    # Find a place for the configuration input and set a "header" (use "st." for the main canvas, "st.sidebar." for the
    # sidebar).
    st.sidebar.header("Pizza Configurator")

    # Get the customer's name via "text_input".
    customer = st.sidebar.text_input("Customer Name")
    # Get the delivery date via "date_input".
    delivery_date = st.sidebar.date_input("Delivery Data")
    # Get the number of pizzas via "number_input" and set min and max limits.
    n_pizza = st.sidebar.number_input("Number of Pizzas", 1, 10)
    # Get the pizza toppings via "multiselect" and pass possible toppings as options.
    pizza_toppings = st.sidebar.multiselect("Toppings", ["cheese", "pepper", "tomato", "pineapple"])
    # Get the free drink selection via "radio" and pass some drinks as options.
    free_drink = st.sidebar.radio("Free drink", ["water", "coke", "beer"])
    # Get optional Home Delivery via "toggle".
    home_delivery = st.sidebar.toggle("Home delivery")

    if st.sidebar.button("Order Pizza"):
        # Define 3 columns in the main canvas via "st.columns(3).
        columns = st.columns(3)
        # Write the logistics data (customer name, delivery date, delivery option) in the first column.
        columns[0].header("Logistic Data")
        s_delivery_date = delivery_date.strftime("%d.%m.%Y")
        s = f"**Customer Name:** {customer}\n\n**Delivery Date:** {s_delivery_date}\n\n"
        s += "Home Delivery" if home_delivery else "Take Away"
        columns[0].markdown(s)
        # Write the shopping list for the cook (ingredients and respective quantities) in the second column.
        columns[1].header("Shopping List")
        s = ""
        for topping in pizza_toppings:
            s += f"{n_pizza} x {topping}\n\n"
        columns[1].markdown(s)
        # Write the invoice for the customer (number of pizzas, total price, delivery fee) in the third column.
        columns[2].header("Invoice")
        prices = {"cheese": 2, "pepper": 3, "tomato": 1, "pineapple": 5}
        s = ""
        topping_price = 0
        for topping in pizza_toppings:
            topping_price += n_pizza*prices[topping]
            s += f"{topping}: {topping_price}€\n\n"
        columns[2].markdown(s)
        columns[2].divider()
        columns[2].markdown(f"**Total**: {topping_price}€")
