#!/bin/bash

# Prompt for original name
read -p "What is the initial name? " original_name

# Prompt for new name
read -p "What is the new name? " new_name

# Check if new_name contains "-"
if [[ "$new_name" == *-* ]]; then
    echo "New project name should not contain any '-'. Replace '-' by '_'"
    exit 1
fi

# Check if new_name is empty or too short
if [[ -z "$new_name" ]]; then
    echo "New project name is empty"
    exit 1
fi

if [[ ${#new_name} -lt 4 ]]; then
    echo "New project name '$new_name' is too short"
    exit 1
fi

echo "Renaming everything"
echo "Changing from '$original_name' to '$new_name'"

# Function to replace text in file
rename_in_file() {
    local file="$1"
    local old="$2"
    local new="$3"
    sed -i "s/$old/$new/g" "$file"
}

# Function to iterate over files in a folder
rename_in_folder() {
    local folder="$1"
    local old="$2"
    local new="$3"
    find "$folder" -type f -print0 | while IFS= read -r -d '' file; do
        rename_in_file "$file" "$old" "$new"
    done
}

# MAIN
rename_in_folder "$original_name" "$original_name" "$new_name"
rename_in_folder "tests" "$original_name" "$new_name"

if [[ -d "$original_name" ]]; then
    mv "$original_name" "$new_name"
fi

rename_in_folder "conf" "$original_name" "$new_name"
rename_in_file "docs/conf.py" "$original_name" "$new_name"
rename_in_file "docs/index.rst" "$original_name" "$new_name"
rename_in_file "tox.ini" "$original_name" "$new_name"
