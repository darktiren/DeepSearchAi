# Copyright (C) [2024] [Christopher Garner]

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    web_agent_json_path = os.path.join(script_dir, "web_agent.json")
    web_agent_compile_path = os.path.join(script_dir, "web_agent_compile.py")
    
    # Step 1: Check Current Query Counter
    web_agent_data = read_json(web_agent_json_path)
    current_query_counter = web_agent_data.get("Current Query Counter", 0)
    total_query_counter = web_agent_data.get("Total Query Counter", 0)

    if current_query_counter > total_query_counter:
        os.system(f"python {web_agent_compile_path}")
    else:
        # Step 2: Access query'value'.json
        query_value_json_path = os.path.join(script_dir, f"query{current_query_counter}.json")
        if os.path.exists(query_value_json_path):
            query_value_data = read_json(query_value_json_path)
            current_website_counter = query_value_data.get("Current Website Counter", 0)
            total_website_counter = query_value_data.get("Total Website Counter", 0)

            if current_website_counter > total_website_counter:
                # Step 3: Increase Current Query Counter and rerun script
                web_agent_data["Current Query Counter"] += 1
                write_json(web_agent_json_path, web_agent_data)
                os.system("python web_agent_5.py")
            else:
                os.system("python web_agent_6.py")
        else:
            print(f"Query value JSON file not found: {query_value_json_path}")

if __name__ == "__main__":
    main()
