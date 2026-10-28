cat << 'EOF' > main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import SessionLocal, init_db, Product, Customer, Sale

app = FastAPI(title="Small-Business Inventory API")

init_db()

TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"

def send_whatsapp_receipt(customer_phone: str, customer_name: str, product_name: str, quantity: int, total_price: float):
    if TWILIO_ACCOUNT_SID == "YOUR_TWILIO_ACCOUNT_SID":
        return False
    try:
        from twilio.rest import Client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message_body = (
            f"Hello {customer_name}!\n\n"
            f"Thank you for your purchase!\n"
            f"Item: {product_name}\n"
            f"Quantity: {quantity}\n"
            f"Total: ${total_price:.2f}\n\n"
            f"We appreciate your business!"
        )
        to_number = customer_phone if customer_phone.startswith("whatsapp:") else f"whatsapp:{customer_phone}"
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message_body,
            to=to_number
        )
        return True
    except Exception as e:
        print(f"Twilio dispatch error: {e}")
        return False

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Inventory & Invoice Automation API is running!"}

# --- PRODUCTS ---
@app.post("/products/")
def add_product(name: str, price: float, stock_quantity: int, low_stock_limit: int = 5, db: Session = Depends(get_db)):
    new_product = Product(name=name, price=price, stock_quantity=stock_quantity, low_stock_limit=low_stock_limit)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"message": "Product added successfully", "product": new_product}

@app.get("/products/")
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# --- CUSTOMERS ---
@app.post("/customers/")
def add_customer(name: str, phone_number: str, email: str = None, db: Session = Depends(get_db)):
    new_customer = Customer(name=name, phone_number=phone_number, email=email)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return {"message": "Customer created successfully", "customer": new_customer}

@app.get("/customers/")
def list_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

# --- SALES & AUTOMATION ---
@app.post("/sales/")
def record_sale(product_id: int, customer_id: int, quantity: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    if product.stock_quantity < quantity:
        raise HTTPException(
            status_code=400, 
            detail=f"Not enough stock! Only {product.stock_quantity} remaining."
        )

    product.stock_quantity -= quantity
    total_amount = product.price * quantity

    new_sale = Sale(product_id=product_id, customer_id=customer_id, quantity_sold=quantity, total_price=total_amount)
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    low_stock_alert = product.stock_quantity <= product.low_stock_limit
    whatsapp_sent = send_whatsapp_receipt(customer.phone_number, customer.name, product.name, quantity, total_amount)

    return {
        "message": "Sale recorded successfully!",
        "invoice": {
            "customer": customer.name,
            "product": product.name,
            "quantity": quantity,
            "total_price": total_amount,
            "remaining_stock": product.stock_quantity
        },
        "low_stock_warning": low_stock_alert,
        "whatsapp_receipt_sent": whatsapp_sent
    }

# --- SALES HISTORY & REVENUE ---
@app.get("/sales/")
def get_sales_history(db: Session = Depends(get_db)):
    sales = db.query(Sale).all()
    total_revenue = db.query(func.sum(Sale.total_price)).scalar() or 0.0
    history = [{"sale_id": s.id, "customer_name": s.customer.name, "product_name": s.product.name, "quantity_sold": s.quantity_sold, "total_price": s.total_price, "date": s.created_at} for s in sales]
    return {"total_sales_count": len(history), "total_revenue": total_revenue, "sales_history": history}
EOF