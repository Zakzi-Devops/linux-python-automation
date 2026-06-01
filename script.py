import os
import platform
from datetime import datetime
import requests


def get_system_info():
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "machine": platform.machine(),
        "python_version": platform.python_version(),
        "current_directory": os.getcwd(),
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    }


def check_api(url):
    try:
        response = requests.get(url, timeout=10)
        return {
            "url": url,
            "status_code": response.status_code,
            "success": response.ok,
        }
    except requests.RequestException as e:
        return {
            "url": url,
            "status_code": None,
            "success": False,
            "error": str(e),
        }


def write_log(system_info, api_results):
    with open("health_report.txt", "w", encoding="utf-8") as f:
        f.write("==== System Info ====\n")
        for key, value in system_info.items():
            f.write(f"{key}: {value}\n")

        f.write("\n==== API Check ====\n")
        for api_result in api_results:
            for key, value in api_result.items():
                f.write(f"{key}: {value}\n")
            f.write("------\n")


if __name__ == "__main__":
    system_info = get_system_info()
    api_list = ["https://api.github.com", "https://google.com", "https://microsoft.com"]

    api_results = []

    for url in api_list:
        result = check_api(url)
        api_results.append(result)

    print("=== System Info ===")
    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\n=== API Check ===")
    for api_result in api_results:
        for key, value in api_result.items():
            print(f"{key}: {value}")
        print("------")

    write_log(system_info, api_results)
    print("\nReport saved to health_report.txt")