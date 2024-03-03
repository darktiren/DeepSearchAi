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
from googlesearch import search

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Step 1: Access web_agent.json & Check Current Query Counter
    web_agent_path = os.path.join(script_dir, "web_agent.json")
    with open(web_agent_path, "r") as f:
        data = json.load(f)
    current_query_counter = data["Current Query Counter"]
    total_query_counter = data["Total Query Counter"]

    # Step 2: Check if Current Query Counter is greater than Total Query Counter
    if current_query_counter > total_query_counter:
        os.system("python " + os.path.join(script_dir, "web_agent_4.py"))
        return

    # Step 3: Access appropriate query'number'.json
    query_filename = os.path.join(script_dir, f"query{current_query_counter}.json")
    with open(query_filename, "r") as query_file:
        query_data = json.load(query_file)
    query = query_data["Query"]

    # Step 4: Use googlesearch to get list of 5 website URLs
    num_results = 5  # Fetch more results
    websites = list(search(query, num=num_results, stop=num_results))

    # Step 5: Store URLs in appropriate keys
    for i, website in enumerate(websites):
        key = f"Website {i+1}"
        query_data[key] = website

    query_data["Total Website Counter"] = num_results
    query_data["Current Website Counter"] = 1

    with open(query_filename, "w") as query_file:
        json.dump(query_data, query_file, indent=4)

    # Step 6: Increase Current Query Counter by 1
    data["Current Query Counter"] += 1
    with open(web_agent_path, "w") as f:
        json.dump(data, f, indent=4)
        
    # Step 7: Execute web_agent_3.py
    os.system("python " + os.path.join(script_dir, "web_agent_3.py"))

if __name__ == "__main__":
    main()
