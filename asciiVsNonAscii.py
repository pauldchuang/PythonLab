import json

# Example body with non-ASCII characters
body = {
    "key": "你"
}

# Escaped JSON (with ensure_ascii=True, which is the default)
escaped_json = json.dumps(body)
print("Escaped JSON:")
print(escaped_json)

# Non-Escaped JSON (with ensure_ascii=False)
non_escaped_json = json.dumps(body, ensure_ascii=False)
print("\nNon-Escaped JSON:")
print(non_escaped_json)

# Encode both JSON strings in UTF-8
encoded_escaped_json = escaped_json.encode("utf-8")
encoded_non_escaped_json = non_escaped_json.encode("utf-8")

# Print the encoded versions
print("\nEncoded Escaped JSON (UTF-8):", encoded_escaped_json)
print("Encoded Non-Escaped JSON (UTF-8):", encoded_non_escaped_json)

# Compare if both encoded byte sequences are the same
print("\nAre the encoded byte sequences the same?", encoded_escaped_json == encoded_non_escaped_json)