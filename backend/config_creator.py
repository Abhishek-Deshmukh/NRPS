def creator(proxies):
    string = ""
    for proxy in proxies:
        string += "server{listen 80"
        if proxy["id"] == 1:
            string += " default_server"
        string += (
            ";server_name "
            + proxy["nameserver"]
            + "; location / { proxy_set_header X-Real-IP $remote_addr; proxy_pass "
            + proxy["address"]
            + "}}"
        )
    return string


if __name__ == "__main__":
    DATA = [
        {"id": 1, "nameserver": "www.dunce.com", "address": "http://localhost:80/",},
        {
            "id": 2,
            "nameserver": "other.dunce.com",
            "address": "http://localhost:8005/",
        },
    ]
    print(creator(DATA))
