# End-to-End Retail Data Pipeline & Analytics Engine

A comprehensive data engineering and business intelligence project that demonstrates the full lifecycle of corporate data—from programmatic synthesis and relational database modeling to advanced SQL analysis and executive dashboarding.

## 📊 System Architecture & Workflow
1. **Data Synthesis (Python):** Generated a 250-row relational retail dataset with strict data integrity constraint checks.
2. **Database Architecture (MySQL):** Designed and deployed a Star Schema (`fact_sales`, `dim_products`, `dim_customers`) on a local Laragon instance.
3. **Advanced Analytics (SQL):** Authored complex queries utilizing multi-table `INNER JOIN`s, set operations (`UNION`), and advanced window functions (`DENSE_RANK() OVER (PARTITION BY...)`).
4. **Business Intelligence (BI Dashboard):** Extracted backend metrics into an interactive dashboard to track revenue and product performance.

---

## 🛠️ Tech Stack & Utilities
* **Languages:** Python 3.x, SQL (Structured Query Language)
* **Database Engine:** MySQL Server (Managed via Laragon Local Environment)
* **Libraries Engine:** Pandas, Random (For data synthesis)
* **Visualization:** Power BI / Microsoft Excel

---

## 📐 Database Schema Design (Star Schema)

### `fact_sales` (Transactional Ledger)
* `SalesID` (Primary Key)
* `ProductID` (Foreign Key linked to `dim_products`)
* `CustomerID` (Foreign Key linked to `dim_customers`)
* `UnitsSold` (Integer)
* `SaleDate` (Temporal Attribute)

### `dim_products` (Dimension Table)
* `ProductID` (Primary Key)
* `Product_Name` (Text)
* `Subcategory` (Text Category Mapping)
* `Product_Price` (Decimal)

### `dim_customers` (Dimension Table)
* `CustomerID` (Primary Key)
* `Customer_Name` (Text)
* `Customer_City` (Text)

---

## 🚀 Key Analytical Case Studies Addressed

### 1. Advanced Window Function Partitioning
**Business Problem:** Identify internal transaction rankings for individual products to find peak performance limits without collapsing raw data layers.
```sql
SELECT 
    SalesID,
    ProductID,
    UnitsSold,
    DENSE_RANK() OVER (
        PARTITION BY ProductID 
        ORDER BY UnitsSold DESC
    ) AS Product_Internal_Rank
FROM fact_sales;