const API_URL = 'http://127.0.0.1:8000';

async function loadTransactions() {
    try {
        const response = await fetch(`${API_URL}/transactions`);
        const transactions = await response.json();
    
        const tableBody = document.getElementById('transaction-table-body');

        for (const transaction of transactions) {
            const row = document.createElement('tr');
            
            const values = [transaction.description, transaction.amount, transaction.category, transaction.type, transaction.date];
            for (const value of values) {
                const cell = document.createElement('td');
                cell.textContent = value;
                row.appendChild(cell);
            }

            tableBody.appendChild(row);
            }
        } catch (error) {
        console.error('Error loading transactions:', error);
    }
}

loadTransactions();
