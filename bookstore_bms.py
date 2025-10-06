from owlready2 import *
import random
import matplotlib.pyplot as plt
import streamlit as st


# 1. Ontology Setup

onto = get_ontology("http://test.org/bookstore.owl")

with onto:
    class Book(Thing):
        pass

    class Customer(Thing):
        pass

    class Employee(Thing):
        pass

    # Object Properties
    class purchases(Customer >> Book):
        pass

    # Data Properties
    class availableQuantity(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]

    class hasPrice(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [float]

# Add books
book1 = Book("book1")
book1.availableQuantity = 5
book1.hasPrice = 12.5

book2 = Book("book2")
book2.availableQuantity = 5
book2.hasPrice = 15.0

book3 = Book("book3")
book3.availableQuantity = 5
book3.hasPrice = 9.99

books = [book1, book2, book3]

# 2. SWRL Rules 

try:
    rule1 = Imp()
    rule1.set_as_rule("""
        Customer(?c), Book(?b), purchases(?c, ?b), availableQuantity(?b, ?q)
        -> availableQuantity(?b, ?q - 1)
    """)
except Exception as e:
    print(f"[SWRL] Could not add SWRL rule: {e}")

try:
    rule2 = Imp()
    rule2.set_as_rule("""
        Employee(?e), Book(?b), availableQuantity(?b, ?q), swrlb:lessThan(?q, 2)
        -> availableQuantity(?b, ?q + 3)
    """)
except Exception as e:
    print(f"[SWRL] Could not add SWRL rule: {e}")

# 3. Simulation Functions

class CustomerAgent:
    def __init__(self, cid):
        self.cid = cid
        self.purchased = []

    def act(self, books):
        book = random.choice(books)
        if book.availableQuantity > 0:
            book.availableQuantity -= 1
            self.purchased.append(book.name)

class EmployeeAgent:
    def __init__(self, eid):
        self.eid = eid

    def act(self, books):
        for book in books:
            if book.availableQuantity < 2:
                book.availableQuantity += 3

# 4. Streamlit Interface

st.set_page_config(page_title="Bookstore MAS Simulation", layout="centered")
st.title("📚 Bookstore Multi-Agent Simulation")

# Sidebar for simulation settings
st.sidebar.header("Simulation Settings")
num_customers = st.sidebar.slider("Number of Customers", 1, 10, 5)
num_employees = st.sidebar.slider("Number of Employees", 1, 5, 2)
num_steps = st.sidebar.slider("Simulation Steps", 1, 20, 10)

if st.button("Run Simulation"):
    # Initialize agents
    customers = [CustomerAgent(i) for i in range(num_customers)]
    employees = [EmployeeAgent(i) for i in range(num_employees)]

    # Reset books
    for b in books:
        b.availableQuantity = 5

    # Run simulation
    for step in range(num_steps):
        for customer in customers:
            customer.act(books)
        for employee in employees:
            employee.act(books)
        # Conceptual SWRL reasoning
        try:
            with onto:
                sync_reasoner()
        except Exception:
            pass

    # Display inventory
    st.subheader("📦 Final Inventory")
    inventory_data = [{"Book": b.name, "Quantity": b.availableQuantity, "Price": b.hasPrice} for b in books]
    st.table(inventory_data)

    # Display purchases
    st.subheader("🛒 Customer Purchases")
    purchases_data = [{"Customer ID": c.cid, "Purchased Books": ", ".join(c.purchased)} for c in customers]
    st.table(purchases_data)

    # Professional compact inventory line plot
    fig, ax = plt.subplots(figsize=(2, 1))  # small and professional

    book_names = [b.name for b in books]
    quantities = [b.availableQuantity for b in books]

    ax.plot(book_names, quantities, marker='o', linestyle='-', color="#061631", linewidth=0.8, markersize=4)

    # Add labels on each point
    for i, qty in enumerate(quantities):
        ax.text(i, qty + 0.1, str(qty), ha='center', va='bottom', fontsize=4)

    # Minimalist styling
    ax.set_ylabel("Quantity", fontsize=4, fontweight='bold')
    ax.set_xlabel("Books", fontsize=4 , fontweight='bold')
    ax.set_title("Inventory after Simulation", fontsize=4, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='both', which='major', labelsize=4)

    st.pyplot(fig)

    # Save ontology
    onto.save("bookstore_result.owl")
    st.success("✅ Ontology saved to 'bookstore_result.owl'")
