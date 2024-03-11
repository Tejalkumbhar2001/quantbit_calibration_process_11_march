import frappe
                
@frappe.whitelist()
def get_raw_materials(sales_entry):
    deli_or = {}
    if sales_entry:
        doc_name = frappe.get_value('Equipment Maintenance Order', {'name': sales_entry, 'docstatus': 1}, "name")
        if doc_name:
            doc = frappe.get_doc('Equipment Maintenance Order', doc_name)
            deli_or['items'] = []

            for d in doc.get("items"):
                item_data = {
                    "item_code": d.item_code,
                    "item_name": d.item_name,
                    "qty":d.quantity,
                
                }
                deli_or['items'].append(item_data)
                # frappe.throw(str(deli_or))
    return deli_or
