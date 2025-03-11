# Helpdesk

This project contains a server script to create a ticket in Frappe Helpdesk from a web form submission.

## File Structure

- `createticket.py`: The main script to create a helpdesk ticket.

## Script Details

The script performs the following actions:

1. Extracts the `subject`, `email`, `description`, and `via_web_form` fields from the provided document.
1. Checks if a contact exists for the given email address; creates a new contact if not found.
1. Associates the new or existing contact with the helpdesk ticket.
1. Creates a new helpdesk ticket with the provided details (subject, description, status, and contact).
1. Creates a communication entry for the ticket.

## Usage

### Frappe Helpdesk Installation

To install Frappe Helpdesk, follow these steps:

1. Ensure you have [Frappe Bench](https://docs.frappe.io/framework/v14/user/en/installation) installed.
2. Create a new site if you don't have one:
   ```sh
   bench new-site your-site-name
   ```
3. Get the Frappe Helpdesk app:
   ```sh
   bench get-app helpdesk https://github.com/frappe/helpdesk
   ```
4. Install the app on your site:
   ```sh
   bench --site your-site-name install-app helpdesk
   ```
5. Start the bench:
   ```sh
   bench start
   ```

Now, you should have Frappe HelpDesk installed and ready to use.

### Server Script

Enable the Server Script by running the following command:

```sh
bench set-config -g server_script_enabled 1
```

Next, navigate to the _Server Script_ section in your Frappe app and create a new Server Script with the following details:

1. **Name**: `create_ticket`
2. **Script Type**: `DocType Event`
3. **Reference Document**: `Contact`
4. **DocType Event**: `AfterSave`

Finally, copy the content from `createticket.py` and paste it into the Script section. Afterward, click the _Save_ button.
