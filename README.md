<h1 align="center">🧪 Python Mini Projects & Code Practice</h1>

<p align="center">
  This repository is my personal Python playground — a collection of bite-sized projects, code experiments, and hands-on practice sessions. From data wrangling and automation to visualization and logic building, each script reflects my growing expertise in Python.  
  <br>
  💡 Whether you're curious about my coding style, problem-solving approach, or just want to see how much Python I know — this is the place to explore!
</p>

---

## 💼 Projects Overview  

| Project | Description | Tools Used | Uploaded |
|----------|--------------|-------------|-----------|
| **📦 Flipkart_Analysis** | Flipkart Big Billion Days dashboard analyzing sales trends, revenue, and customer behavior. | Python, Pandas, Seaborn, Matplotlib | <span id="flipkart-days"></span> days ago |
| **🛒 E-commerce Analysis** | Dashboard visualizing product sales, customer orders, and profit distribution. | Excel, Power BI | <span id="ecommerce-days"></span> days ago |
| **⚡ Blinkit_DASHBOARD** | Sales and delivery performance analysis dashboard for Blinkit. | Power BI | <span id="blinkit-days"></span> days ago |
| **🧾 Retail-Sales-Analysis-SQL-Project--P2_vr** | SQL-based retail analysis focusing on revenue and customer segmentation. | SQL | <span id="retail-days"></span> days ago |
| **🧍‍♂️ Customer-Churn-analysis-main** | Churn prediction project identifying factors behind customer loss. | Python, Pandas, Matplotlib | <span id="churn-days"></span> days ago |
| **🥗 Gresorey** | Grocery store sales analysis with focus on seasonal buying trends. | Excel, Power BI | <span id="gresorey-days"></span> days ago |
| **🎓 Student Addiction Data** | Behavioral data analysis of student activities and habits. | Excel, Python | <span id="student-days"></span> days ago |
| **💰 Tip Analysis** | Analyzed restaurant tipping patterns and customer spending habits. | Python, Seaborn | <span id="tip-days"></span> days ago |
| **📘 Excel_Analysis.xlsx** | Excel-based data exploration with pivot tables and charts. | Excel | <span id="excel-days"></span> days ago |

---

### ⚙️ How it works
Below is an example snippet using **JavaScript** to dynamically calculate days since upload:

```html
<script>
  const projects = {
    flipkart: "2025-10-18",
    ecommerce: "2025-05-20",
    blinkit: "2025-05-20",
    retail: "2025-04-20",
    churn: "2025-04-20",
    gresorey: "2025-09-20",
    student: "2025-08-20",
    tip: "2025-06-20",
    excel: "2025-01-15"
  };

  const today = new Date();

  Object.keys(projects).forEach(id => {
    const uploadDate = new Date(projects[id]);
    const diffTime = Math.abs(today - uploadDate);
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    document.getElementById(`${id}-days`).innerText = diffDays;
  });
</script>
