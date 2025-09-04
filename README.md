# 🦠 Covid-19 Impact Analysis Dashboard

This project is an interactive **Covid-19 Impact Analysis Dashboard** built with **Dash, Plotly, and Pandas**.  
It visualizes Covid-19 data (from `state_wise_daily data.csv`) to analyze the impact across states in India.

---

<img width="1353" height="685" alt="image" src="https://github.com/user-attachments/assets/87597194-7618-4cbd-8295-f8d96e627c1b" />

<img width="1326" height="501" alt="image" src="https://github.com/user-attachments/assets/8fc71211-5f84-408a-9153-2a0f37664e54" />


---

---

## 🚀 Features
- 📊 Display **Total, Active, Recovered, Deaths** in styled cards.
- 📉 Interactive **Bar Charts** for state-wise Covid-19 cases.
- 📈 **Line Graphs** to track commodities (Mask, Sanitizer, Oxygen).
- 🥧 **Pie Chart** for Zone classifications (Red, Green, Orange, Blue).
- 🎨 Responsive UI with **Bootstrap integration**.

---

## 🏗️ Project Architecture
- **Frontend** → Dash HTML & Core Components (`html.Div`, `dcc.Dropdown`, `dcc.Graph`).
- **Backend** → Flask (auto-managed by Dash).
- **Data Layer** → CSV file processed using `pandas`.
- **Visualization** → Plotly (Bar, Line, Pie charts).

## 📂 Dataset
- **File used**: `state_wise_daily data.csv`  
- Contains:  
  - `State` → Name of the state  
  - `Status` → Confirmed, Recovered, Deceased  
  - `Hospitalized`, `Recovered`, `Deceased` counts  
  - `Mask`, `Sanitizer`, `Oxygen` usage data  
  - `Zone` classification
 
## 📌 Use Cases
- 🏥 **Healthcare officials** → Track cases & allocate resources.  
- 📊 **Researchers** → Analyze recovery vs death patterns.  
- 🏛️ **Government agencies** → Monitor spread and plan response.  
- 📉 **General public** → Awareness about COVID-19 status.  

## 🛠️ Tech Stack
- **Python 3.10+**  
- **Dash (Plotly)** → UI framework  
- **Plotly Express & Graph Objects** → Charts  
- **Bootstrap** → Styling (via external CSS)  
- **Pandas** → Data analysis  

## 🛠️ Technologies Used
- [Dash](https://dash.plotly.com/)  
- [Plotly](https://plotly.com/python/)  
- [Pandas](https://pandas.pydata.org/)  
- [Numpy](https://numpy.org/)  

---

## 📂 Project Structure
