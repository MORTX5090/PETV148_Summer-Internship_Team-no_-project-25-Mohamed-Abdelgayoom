import requests
import urllib3
from urllib.parse import urlparse

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Required Security Headers (Header : Score)
SECURITY_HEADERS = {
    "Content-Security-Policy": 20,
    "Strict-Transport-Security": 20,
    "X-Frame-Options": 15,
    "X-Content-Type-Options": 15,
    "Referrer-Policy": 15,
    "Permissions-Policy": 15
}

# Browser User-Agent
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
}


def normalize_url(url):
    """
    Ensure URL starts with http:// or https://
    """
    url = url.strip()

    parsed = urlparse(url)

    if not parsed.scheme:
        url = "https://" + url

    return url


def analyze_headers(headers):
    """
    Analyze security headers and calculate score.
    """

    score = 0
    results = []
    recommendations = []

    for header, points in SECURITY_HEADERS.items():

        if header in headers:

            score += points

            results.append({
                "header": header,
                "status": "Present",
                "score": points,
                "value": headers.get(header, ""),
                "recommendation": ""
            })

        else:

            recommendation = f"Add the '{header}' security header."

            results.append({
                "header": header,
                "status": "Missing",
                "score": 0,
                "value": "-",
                "recommendation": recommendation
            })

            recommendations.append(recommendation)

    # Final Grade
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 40:
        grade = "D"
    else:
        grade = "F"

    return score, grade, results, recommendations


def scan_headers(url):
    """
    Scan a website for HTTP Security Headers.
    """

    url = normalize_url(url)

    try:

        response = requests.get(
            url,
            headers=REQUEST_HEADERS,
            timeout=5,
            verify=False,
            allow_redirects=True
        )

        headers = response.headers

        score, grade, results, recommendations = analyze_headers(headers)

        return {
            "success": True,
            "url": url,
            "status_code": response.status_code,
            "score": score,
            "grade": grade,
            "results": results,
            "recommendations": recommendations
        }

    except requests.exceptions.Timeout:

        return {
            "success": False,
            "error": "Connection timed out."
        }

    except requests.exceptions.ConnectionError:

        return {
            "success": False,
            "error": "Unable to connect to the website."
        }

    except requests.exceptions.RequestException as e:

        return {
            "success": False,
            "error": str(e)
        }


# ------------------------
# Test Scanner
# ------------------------

if __name__ == "__main__":

    website = input("Enter website URL: ")

    result = scan_headers(website)

    if result["success"]:

        print("\n" + "=" * 80)
        print("              HTTP SECURITY HEADERS SCANNER")
        print("=" * 80)

        print(f"Website      : {result['url']}")
        print(f"HTTP Status  : {result['status_code']}")
        print(f"Security Score : {result['score']}/100")
        print(f"Grade        : {result['grade']}")

        print("\n" + "-" * 110)

        print("{:<35} {:<10} {:<6} {}".format(
            "Header",
            "Status",
            "Score",
            "Value"
        ))

        print("-" * 110)

        for item in result["results"]:

            value = item["value"]

            if value != "-" and len(value) > 60:
                value = value[:60] + "..."

            print("{:<35} {:<10} {:<6} {}".format(
                item["header"],
                item["status"],
                item["score"],
                value
            ))

        print("-" * 110)

        print("\nRecommendations")
        print("-" * 110)

        if result["recommendations"]:

            for recommendation in result["recommendations"]:
                print(f"• {recommendation}")

        else:

            print("All recommended security headers are present.")

        print("\nScan Completed Successfully.")

    else:

        print("\nScan Failed")
        print("-" * 40)
        print(result["error"])