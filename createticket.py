subject = doc.subject
email = doc.email
description = doc.description
via_web_form = doc.via_web_form

contact = frappe.get_value("Contact", {"email_ids": {"email_id": email}})
if not contact:
    contact = frappe.get_doc(
        {
            "doctype": "Contact",
            "first_name": email.split("@")[0],
            "email_ids": [{"email_id": email, "is_primary": 1}],
        }
    ).insert()
else:
    contact = frappe.get_doc("Contact", contact)

doc.contact = contact.name

try:
    hd_ticket = frappe.get_doc(
        {
            "doctype": "HD Ticket",
            "subject": subject,
            "raised_by": email,
            "status": "Open",
            "description": description,
            "via_customer_portal": via_web_form,
            "contact": doc.contact,
        }
    ).insert(ignore_permissions=True)

    hd_ticket.create_communication_via_contact(hd_ticket.description)
except Exception as e:
    frappe.log_error(frappe.get_traceback(), "Helpdesk Ticket Creation Failed")
    # frappe.throw(_("There was an error creating the helpdesk ticket. Please try again later."))
