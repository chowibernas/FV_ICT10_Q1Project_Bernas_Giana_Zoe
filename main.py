from pyscript import window

"""The button code is from W3 schools."""
def order_now(e):
    window.location.href = "index_order_page.html"

from pyscript import document, display 
    

def get_info(e):
    _name = (document.getElementById("customer_name").value)
    _address = (document.getElementById("customer_address").value)
    _number = (document.getElementById("customer_number").value)

    if not _name or not _address or not _number:
        document.getElementById("_info").innerText = "⚠️ Please fill out the boxes!"
        document.getElementById("total_price").innerText = " "
        return
    
    details = f"""
        ORDER SUMMARY
        \nCustomer's Name: {_name}
        \nAddress: {_address}
        \nContact Number: {_number}
    """
    total = 0
    for i in range(1, 13):
        checkbox = document.getElementById(f"input{i}")
        if checkbox.checked:
            total += float(checkbox.value)

    document.getElementById("total_price").innerText = f"Total Price: PHP{total:.2f}"

    document.getElementById("_info").innerHTML = " "
    display(details, target="_info")
    print(details)
    