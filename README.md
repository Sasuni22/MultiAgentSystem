# 📘 Multi-Agent Bookstore Management System

An **academic project** that demonstrates the use of a **Multi-Agent System (MAS)** for simulating bookstore operations. The system leverages **ontology modeling** and **SWRL rules** to model intelligent agent behavior such as customer purchases and employee restocking, along with a simple interactive simulation dashboard.

---

## 🎯 Project Overview

This project explores how **agents, ontologies, and rule-based reasoning** can be used to model real-world systems. A bookstore environment is simulated where:

* Customers purchase books
* Employees monitor stock levels and restock when needed
* Inventory changes dynamically based on predefined rules

The system is designed for **learning and demonstration purposes**, focusing on concepts from Artificial Intelligence and Multi-Agent Systems.

---

## 🚀 Key Features

* 🧠 **Ontology-based modeling** of a bookstore domain
* 👥 **Customer and Employee agents** with simple behaviors
* 📜 **SWRL rules** to automate inventory updates
* 📊 **Streamlit dashboard** to run and observe the simulation
* 📈 **Visualization of inventory changes** using Matplotlib

---

## 🛠️ Technology Stack

* **Python 3** – Core programming language
* **Owlready2** – Ontology modeling and reasoning
* **SWRL** – Rule-based reasoning for agent actions
* **Streamlit** – Interactive simulation dashboard
* **Matplotlib** – Inventory data visualization

---

## 🏗️ System Architecture

* **Ontology Layer**: Defines Books, Customers, Employees, and Inventory concepts
* **Agent Layer**: Implements Customer and Employee agents
* **Rule Layer**: SWRL rules trigger stock updates and restocking actions
* **Presentation Layer**: Streamlit UI for running simulations and viewing results

---


## ⚙️ Installation & Setup

### Prerequisites

* Python 3.9+
* pip

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/multi-agent-bookstore-management-system.git
cd multi-agent-bookstore-management-system
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Simulation Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser and allow you to execute the bookstore simulation.

---

## 🧪 Simulation Behavior

* Customers attempt to purchase books
* Inventory levels decrease accordingly
* SWRL rules detect low stock
* Employee agents automatically restock items
* Inventory changes are visualized in real time


## 🌱 Future Enhancements

* More complex agent behaviors and decision-making
* Multiple customer profiles and demand patterns
* Advanced reasoning rules
* Persistent storage of simulation data

---

## 📚 Academic Context

This project was developed as part of an **Artificial Intelligence / Multi-Agent Systems** module to demonstrate:

* Ontology reasoning
* Rule-based systems
* Agent-based simulation


