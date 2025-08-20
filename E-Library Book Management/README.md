# 🚆 Virtual Train Route Planner (Python)

A simple **Virtual Train Route Planner** implemented in Python.  
This project simulates navigation between train stations using **doubly linked lists** and **circular linked lists** for flexible route planning.  

---

## 📌 Overview
The Train Route Planner allows users to **navigate stations forward and backward** (using a doubly linked list), and also handles **loop routes** (using a circular linked list).  
This mimics real-life train journeys where routes may be linear or circular.  

---

## ✨ Features
- ➕ **Add Stations** – Create train stations dynamically.  
- ⏩ **Forward Navigation** – Move to the next station.  
- ⏪ **Backward Navigation** – Move to the previous station.  
- 🔄 **Circular Routes** – Navigate continuously in looped routes.  
- 📍 **Display Current Route** – Show available stations in the route.  

---

## 🛠 Data Structures Used
- **Doubly Linked List**  
  - Used for **forward/backward navigation** in linear routes.  
  - Each station node stores:  
    - `name` (station name)  
    - `prev` (previous station)  
    - `next` (next station)  

- **Circular Linked List**  
  - Used for **loop routes** where the train keeps cycling through stations.  
  - Last station points back to the first station.  

---

## ▶️ How It Runs
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/train-route-planner.git
   cd train-route-planner

