"""
Payment Request Generator
Generates payment links for services
"""

# PayPal.me link (replace with actual)
PAYPAL_LINK = "https://paypal.me/davidmartin0127"

# Crypto wallet addresses (BTC, ETH)
BTC_ADDRESS = "bc1q..."  # Add your BTC address
ETH_ADDRESS = "0x..."    # Add your ETH address

def create_invoice(service, amount, description):
    """Generate invoice and payment links"""
    invoice = f"""
INVOICE
=======
Service: {service}
Description: {description}
Amount: ${amount}

Payment Options:
1. PayPal: {PAYPAL_LINK}
2. BTC: {BTC_ADDRESS}
3. ETH: {ETH_ADDRESS}

Terms: Net 30
"""
    return invoice

def create_paypal_link(amount):
    """Create PayPal payment link"""
    return f"{PAYPAL_LINK}/{amount}"

if __name__ == "__main__":
    # Example
    print(create_invoice("Email Automation", 99, "Basic email auto-responder"))
