def config_writer(proxies):
    config = ""
    for proxy in proxies:
        config += "server{listen 80"
        if proxy["id"] == 1:
            config += " default_server"
        config += (
            ";server_name "
            + proxy["nameserver"]
            + "; location / { proxy_set_header X-Real-IP $remote_addr; proxy_pass "
            + proxy["address"]
            + ";}}"
        )
    return config


def config_parser(config):

    # local variables
    proxies = []
    proxy = {
        "id": 0,
        "nameserver": "",
        "address": "",
    }
    count = 1

    # removing uncecessary seperators
    config = config.replace("\n", "")
    config = config.replace("\t", "")

    # separating using `;`
    config_lines = config.split(";")

    # looping through lines
    for config_line in config_lines:
        config_line = config_line.strip()

        # scraping for nameserver
        if config_line.find("server_name") != -1:
            proxy["nameserver"] = config_line.split(" ", 1)[1]

        # scraping the address
        if config_line.find("proxy_pass") != -1:
            proxy["address"] = config_line.split()[-1]
            # putting in the address and appending to proxies
            proxy["id"] = count
            count += 1
            proxies.append(proxy.copy())
    return proxies


if __name__ == "__main__":
    # test
    DATA = [
        {"id": 1, "nameserver": "www.dunce.com", "address": "http://localhost:80/",},
        {
            "id": 2,
            "nameserver": "other.dunce.com",
            "address": "http://localhost:8005/",
        },
    ]
    assert config_parser(config_writer(DATA)) == DATA
