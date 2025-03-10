from curl_cffi import requests
from rich.console import Console
from models import SearchResponse, SearchProduct, ProductAvailability

console = Console()

def new_session() -> requests.Session:
    """Creates a new session with browser impersonation."""
    try:
        return requests.Session(impersonate="chrome")
    except Exception as e:
        console.print(f"[bold red]Error initializing session: {e}[/bold red]")
        raise

def search_api(session: requests.Session, query: str, gender: str, sorttype: str, size: int) -> SearchResponse:
    """Fetch Adidas product search results."""
    url = f"https://www.adidas.co.uk/plp-app/api/search?q={query}&gender={gender}&sort={sorttype}&v_size_en_gb={size}"
    
    try:
        resp = session.get(url)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        console.print(f"[bold red]Error fetching search results: {e}[/bold red]")
        return SearchResponse(count=0, startIndex=0, searchTerm=query, items=[])
    
    items = [
        SearchProduct(
            productId=product["id"],
            modelId=product["modelNumber"],
            title=product["title"],
            subTitle=product["subTitle"],   
            url=product["url"],
            image=product["image"],
            priceData= {
                "price": product["priceData"]["price"],
                "salePrice": product["priceData"]["salePrice"],
                "discountText": product["priceData"]["discountText"]
            },
            rating=product.get("rating", None)
        )
        for product in data.get("products", [])
        if product["priceData"]["discountText"] != "0%"  # Exclude 0% discounts
    ]
    
    return SearchResponse(
        count=data["info"]["count"],
        startIndex=data["info"]["startIndex"],
        searchTerm=data["info"]["searchTerm"],
        items=items
    )

def item_availability_api(session: requests.Session, item: SearchProduct) -> Optional[ProductAvailability]:
    """Fetch Adidas product availability information."""
    url = f"https://www.adidas.co.uk/api/products/{item.productId}/availability"
    
    try:
        resp = session.get(url)
        resp.raise_for_status()
        return ProductAvailability(**resp.json())
    except requests.RequestException as e:
        console.print(f"[bold red]Error fetching availability for {item.productId}: {e}[/bold red]")
        return None
