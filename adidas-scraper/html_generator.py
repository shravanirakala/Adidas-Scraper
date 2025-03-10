from typing import List
from models import SearchProduct

def generate_html_email(products: List[SearchProduct], gender: str, sorttype: str, size: int) -> tuple[str, str]:
    """Generates HTML and plain text content for email."""
    plain_text = f"""
    Hello, Greetings!\n\n
    Check out the {gender} {sorttype} discounts on Adidas products for UK size:{size}.
    URL: https://www.adidas.co.uk\n\n
    """

    html_content = f"""<html><body>
        <p>Hello, Greetings!<br><br>
        Check out these <b>{gender} {sorttype} discounts</b> on Adidas products, available for size UK:{size}.<br><br>
        <table style="border-collapse: collapse; width: 100%;">"""

    for i, item in enumerate(products[:9]):
        if i % 3 == 0:
            html_content += "<tr>"
        
        html_content += f"""
            <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">
                <a href="https://www.adidas.co.uk{item.url}" target="_blank">
                    <img src="{item.image}" alt="Product Image" width="200">
                </a>
                <br>
                <b>{item.title}</b><br>
                <span style="color:grey;"> {item.subTitle} </span><br>
                <span style="color: red; font-weight: bold;">£{item.priceData['salePrice']}</span>
                <span style="color: grey; font-size: 10px;"><del>£{item.priceData['price']}</del></span>
                <span style="color: red; font-weight: bold;"> -{item.priceData['discountText']}</span><br>
            </td>"""

        if i % 3 == 2 or i == len(products) - 1:
            html_content += "</tr>"
    
    html_content += "</table></body></html>"
    return plain_text, html_content
