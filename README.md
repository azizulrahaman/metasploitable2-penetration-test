# 🔐 Penetration Test — Metasploitable 2

**Tester:** Azizul Rahman
**Program:** Masters of Cybersecurity
**Date:** 23 February 2026
**Risk Rating:** 🔴 CRITICAL

## Summary
Full infrastructure penetration test against Metasploitable 2
using Kali Linux and Metasploit Framework.

## Key Findings
| # | Vulnerability | CVE | Risk | CVSS |
|---|---|---|---|---|
| 1 | Unauthenticated Root Backdoor | — | Critical | 10.0 |
| 2 | vsftpd 2.3.4 Backdoor RCE | CVE-2011-2523 | Critical | 10.0 |
| 3 | Samba Usermap Script RCE | CVE-2007-2447 | Critical | 9.3 |
| 4 | Default SSH Credentials + Privesc | — | Critical | 9.0 |
| 5 | SQL Injection (UNION-based) | — | High | 8.5 |
| 6 | OS Command Injection | — | High | 8.0 |
| 7 | Reflected + Stored XSS | — | High | 7.2 |

## Tools Used
- Kali Linux + Metasploit Framework
- Nmap, Netcat, John the Ripper
- DVWA (Damn Vulnerable Web App)
- Meterpreter

## Methodology
PTES: Reconnaissance → Scanning → Exploitation
→ Post-Exploitation → Web App Testing → Reporting

## ⚠️ Disclaimer
Conducted in an isolated VirtualBox lab environment
for educational purposes only.
