import mage_ai

def main():
    endpoints = [
        {"name": "TableInfos", "table_name": "info"},
        {"name": "TypedDataSet", "table_name": "emergencies"},
        {"name": "DataProperties", "table_name": "properties"},
        {"name": "RegioS", "table_name": "regions"},
        {"name": "Perioden", "table_name": "periods"},
    ]
    
    for endpoint in endpoints:
        print(f"start: {endpoint['name']}")
        mage_ai.run(project_path="/home/src", pipeline_uuid="github_actions", endpoint_name=endpoint["name"], table_name=endpoint["table_name"])

if __name__ == "__main__":
    main()