import vulners

def get_fix_information(service_name, service_version):
    vulners_api = vulners.Vulners(api_key="YOUR_VULNERS_API_KEY")
    search_query = f"{service_name} {service_version}"
    results = vulners_api.search(search_query)

    fix_info = []
    for result in results:
        fix_info.append({
            "title": result["title"],
            "description": result["description"],
            "fix_url": result.get("href"),
            "publication_date": result["published"],
            "cvss_score": result["cvss"]["score"]
        })

    return fix_info

service_name = "nginx"
service_version = "1.18.0"
fix_info = get_fix_information(service_name, service_version)
for info in fix_info:
    print(f"Title: {info['title']}")
    print(f"Description: {info['description']}")
    print(f"Fix URL: {info['fix_url']}")
    print(f"Published: {info['publication_date']}")
    print(f"CVSS Score: {info['cvss_score']}\n")
