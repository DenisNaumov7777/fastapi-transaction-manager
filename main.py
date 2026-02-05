from fastapi import FastAPI, Request, Form, status, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

# 1. App Initialization with Metadata
app = FastAPI(
    title="Transaction Manager",
    description="A robust web application for managing financial transactions.",
    version="1.0.0",
    contact={
        "name": "Denis Naumov",
        "url": "https://github.com/DenisNaumov7777",
        "email": "denis@example.com",
    },
)

# 2. Template Configuration
templates = Jinja2Templates(directory="templates")

# 3. Sample Data (In-memory Database)
transactions = [
    {'id': 1, 'date': '2025-06-01', 'amount': 100},
    {'id': 2, 'date': '2025-06-02', 'amount': -200},
    {'id': 3, 'date': '2025-06-03', 'amount': 300}
]

# --- READ OPERATION (Dashboard) ---
@app.get("/", response_class=HTMLResponse)
def get_transactions(request: Request):
    """
    Render the main dashboard displaying the list of all transactions.
    """
    return templates.TemplateResponse("transactions.html", {
        "request": request, 
        "transactions": transactions
    })

# --- CREATE OPERATION ---

@app.get("/add", response_class=HTMLResponse)
def add_form(request: Request):
    """
    Render the HTML form for creating a new transaction.
    """
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/add")
def add_transaction(date: str = Form(...), amount: float = Form(...)):
    """
    Handle the form submission to create a new transaction.
    """
    # Generate a new ID (increment the last ID, or start at 1)
    new_id = transactions[-1]['id'] + 1 if transactions else 1
    
    # Create the transaction object
    new_transaction = {
        'id': new_id,
        'date': date,
        'amount': amount
    }
    
    # Save to the database
    transactions.append(new_transaction)
    
    # Redirect to the main page (PRG Pattern)
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

# --- UPDATE OPERATION ---

@app.get("/edit/{transaction_id}", response_class=HTMLResponse)
def edit_form(request: Request, transaction_id: int):
    """
    Render the edit form pre-filled with existing transaction data.
    """
    # Find the transaction by ID
    transaction = next((t for t in transactions if t['id'] == transaction_id), None)
    
    # Handle case where ID does not exist
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
        
    return templates.TemplateResponse("edit.html", {"request": request, "transaction": transaction})

@app.post("/edit/{transaction_id}")
def edit_transaction(transaction_id: int, date: str = Form(...), amount: float = Form(...)):
    """
    Process the update request and modify the existing record.
    """
    # Iterate through the list to find and update the record
    for t in transactions:
        if t['id'] == transaction_id:
            t['date'] = date
            t['amount'] = amount
            break
            
    # Redirect back to the dashboard
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

# --- DELETE OPERATION ---

@app.post("/delete/{transaction_id}")
def delete_transaction(transaction_id: int):
    """
    Securely delete a transaction using the POST method.
    """
    # Find the index and remove the item
    for i, t in enumerate(transactions):
        if t['id'] == transaction_id:
            del transactions[i]
            break
            
    # Redirect back to the dashboard
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

# 4. Entry Point
if __name__ == "__main__":
    import uvicorn
    # Run the server on 0.0.0.0 to allow external access (e.g., Docker/Hetzner)
    uvicorn.run(app, host="0.0.0.0", port=8080)