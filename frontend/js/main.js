//const API_URL = "http://localhost:5000/api"; // Update with deployed URL (e.g., Vercel)
const API_URL = "https://sherlocks-life-task.onrender.com"

let currentTable = "agents";

document.getElementById("table-select").addEventListener("change", (e) => {
    currentTable = e.target.value;
    loadTableData();
    loadChart();
});

async function loadTableData() {
    try {
        const response = await fetch(`${API_URL}/${currentTable}`);
        if (!response.ok) throw new Error(`Failed to fetch ${currentTable} data`);
        const data = await response.json();
        if (!data || data.length === 0) {
            console.warn(`No data returned for ${currentTable}`);
        }
        renderTable(data);
        document.getElementById("download-csv").style.display = data.length ? "block" : "none";
        updateChart(data);
    } catch (error) {
        console.error(`Error loading ${currentTable} data:`, error);
        renderTable([]);
    }
}

// Initial load
loadTableData();
