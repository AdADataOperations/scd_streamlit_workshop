import streamlit as st

# You have just opened a new pizzeria and want to build a dashboard that allows you to create and order your own pizzas
# and display information about the process.
# You can view the dashboard by "streamlit run starter.py" in terminal.
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    # TODO: Set a "title" for your Pizza Dashboard!
    st.title("")

    # TODO: Find a place for the configuration input and set a "header" (use "st." for the main canvas, "st.sidebar."
    #  for the sidebar).
    # st.sidebar.header("Pizza Configurator")

    # TODO: Get the customer's name via "text_input".
    customer = None
    # TODO: Get the delivery date via "date_input".
    delivery_date = None
    # TODO: Get the number of pizzas via "number_input" and set min and max limits.
    n_pizza = None
    # TODO: Get the pizza toppings via "multiselect" and pass possible toppings as options.
    pizza_toppings = None
    # TODO: Get the free drink selection via "radio" and pass some drinks as options.
    free_drink = None
    # TODO: Get optional Home Delivery via "toggle".
    home_delivery = None

    if st.sidebar.button("Order Pizza"):
        # Define 3 columns in the main canvas via "st.columns(3).
        columns = st.columns(3)
        # TODO: Write the logistics data (customer name, delivery date, delivery option) in the first column.
        columns[0].header("Logistic Data")
        # TODO: Write the shopping list for the cook (ingredients and respective quantities) in the second column.
        columns[1].header("Shopping List")
        # TODO: Write the invoice for the customer (number of pizzas, total price, delivery fee) in the third column.
        columns[2].header("Invoice")

    # Feel free to add further features, e.g. save data to csv and provide for download!
