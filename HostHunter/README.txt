# 🛰️ HostHunter

**Author:** `sh3ll5n4k3`  
**Version:** `1.0`

---

## 📌 Description

**HostHunter** is a lightweight Bash tool designed to assist CTF players, pentesters, and red teamers in **enumerating and mapping subdomains to an IP address** quickly by modifying `/etc/hosts`.

It simulates DNS resolution for potential subdomains by adding entries to your local hosts file and then probing each one for HTTP `302 Found` responses — commonly used in redirects or login portals.

> ⚠️ This tool is intended for **CTF labs**, **authorized testing environments**, or **educational use** only.

---

## 🔧 Features

- Adds a list of subdomains to `/etc/hosts` using a specified IP
- Scans each subdomain for HTTP `302` responses
- Supports `-v` verbose mode to display full HTTP status codes
- Cleans up `/etc/hosts` automatically on exit or interruption
- Displays progress percentage during execution

---

## 🧰 Usage

```bash
./hosthunter.sh <DOMAIN> <WORDLIST> <IP> [-v]
```

### Required Arguments:

| Argument     | Description                                       |
|--------------|---------------------------------------------------|
| `<DOMAIN>`   | The base domain (e.g., `example.com`)             |
| `<WORDLIST>` | File containing subdomains (one per line)         |
| `<IP>`       | The IP to map the subdomains to                   |

### Optional:

- `-v` → verbose mode to print **all** HTTP response codes

---

## 💡 Example

```bash
./hosthunter.sh ctfbox.local subdomains.txt 10.10.10.10 -v
```

This will:
- Map each word in `subdomains.txt` as a subdomain of `ctfbox.local`
- Add `10.10.10.10 subdomain.ctfbox.local` entries to `/etc/hosts`
- Scan each for `302` responses and show verbose HTTP codes

---

## 🧪 Output Example

```
Backup of /etc/hosts created.
Adding entries to /etc/hosts...
Progress: 100% (100/100)
Checking for 302 responses...
Response Code 200: http://admin.ctfbox.local
302 Found: http://login.ctfbox.local
...
HostHunter complete!
```

---

## ⚠️ Requirements

- Linux/Unix environment
- `bash`, `curl`, `figlet`, and `tput`
- `sudo` privileges to modify `/etc/hosts`

---

## 🔒 Legal Disclaimer

This tool is for **educational and authorized use only**.  
Do not use it on networks or domains without **explicit permission**.

---

## 📜 License

MIT License

---

## 🤝 Contributing

Pull requests, issues, and suggestions are welcome!
