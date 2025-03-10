from api import new_session, search_api
from email_sender import send_email
from html_generator import generate_html_email
from rich.console import Console

console = Console()

def main():
    """Main function to fetch Adidas discounts and send an email."""
    session = new_session()

    gender = "Women"
    sorttype = "top-sellers"
    size = 9

    search_results = search_api(session, "DISCOUNT", gender, sorttype, size)
    if not search_results.items:
        console.print("[bold yellow]No products found.[/bold yellow]")
        return

    plain_text, html_content = generate_html_email(search_results.items, gender, sorttype, size)
    email_status = send_email(plain_text, html_content, "recipient_mail@example.com")
    console.print(email_status)

    session.close()

if __name__ == "__main__":
    main()
