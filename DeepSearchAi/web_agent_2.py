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

import json
import os

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Step 1: Access web_agent.json & Analyze Response Key
    web_agent_path = os.path.join(script_dir, "web_agent.json")
    with open(web_agent_path, "r") as f:
        data = json.load(f)
    response = data["Response"]

    # Step 2: Extract list items and store them in query files
    queries = response.split("\n")
    for i, query in enumerate(queries):
        if query.strip().startswith(f"{i+1}."):
            query_text = query.strip()[3:].strip()
            query_filename = os.path.join(script_dir, f"query{i+1}.json")
            # Read existing query file data
            try:
                with open(query_filename, "r") as query_file:
                    query_data = json.load(query_file)
            except FileNotFoundError:
                query_data = {}
            # Update the "Query" key
            query_data["Query"] = query_text
            # Write back the updated data
            with open(query_filename, "w") as query_file:
                json.dump(query_data, query_file, indent=4)

    # Step 3: Set Total Query Counter and Current Query Counter in web_agent.json
    data["Total Query Counter"] = len(queries)
    data["Current Query Counter"] = 1
    with open(web_agent_path, "w") as f:
        json.dump(data, f, indent=4)

    # Step 4: Execute web_agent_3.py
    os.system("python " + os.path.join(script_dir, "web_agent_3.py"))

if __name__ == "__main__":
    main()
