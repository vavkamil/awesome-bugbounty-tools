# Awesome Bug Bounty Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated list of various bug bounty tools

## Contents

- [Recon](#Recon)
    - [Subdomains](#Subdomains)
    - [Ports](#Ports)
    - [Screenshots](#Screenshots)
    - [Technologies](#Technologies)
    - [Files/directories](#Files/directories)
    - [Secrets](#Secrets)
    - [Buckets](#Buckets)
    - [Git](#Git)

- [Exploitation](#Exploitation)
    - [CMS](#)
    - [Command Injection](#)
    - [CORS Misconfiguration](#CORS Misconfiguration)
    - [CRLF Injection](#CRLF Injection)
    - [CSRF Injection](#CSRF Injection)
    - [Directory Traversal](#)
    - [File Inclusion](#)
    - [GraphQL Injection](GraphQL Injection)
    - [HTTP Parameter Pollution](#)
    - [Insecure Deserialization](#)
    - [Insecure Direct Object References](#)
    - [JSON Web Token](#JSON Web Token)
    - [Open Redirect](#)
    - [postMessage](#postMessage)
    - [Race Condition](#)
    - [Request Smuggling](#)
    - [Server Side Request Forgery](#Server Side Request Forgery)
    - [SQL Injection](#SQL Injection)
    - [Subdomain takeover](#)
    - [XSS Injection](#)
    - [XXE Injection](#XXE Injection)


---

## Exploitation

Lorem ipsum dolor sit amet

### CORS Misconfiguration

Lorem ipsum dolor sit amet

- [Corsy](https://github.com/s0md3v/Corsy) - CORS Misconfiguration Scanner
- [CORStest](https://github.com/RUB-NDS/CORStest) - A simple CORS misconfiguration scanner
- [cors-scanner](https://github.com/laconicwolf/cors-scanner) - A multi-threaded scanner that helps identify CORS flaws/misconfigurations

### CRLF Injection

Lorem ipsum dolor sit amet

- [crlfuzz](https://github.com/dwisiswant0/crlfuzz) - A fast tool to scan CRLF vulnerability written in Go
- [CRLF-Injection-Scanner](https://github.com/MichaelStott/CRLF-Injection-Scanner) - Command line tool for testing CRLF injection on a list of domains.
- [Injectus](https://github.com/BountyStrike/Injectus) - CRLF and open redirect fuzzer

### CSRF Injection

Lorem ipsum dolor sit amet

- [XSRFProbe](https://github.com/0xInfection/XSRFProbe) -The Prime Cross Site Request Forgery (CSRF) Audit and Exploitation Toolkit.

### GraphQL Injection

Lorem ipsum dolor sit amet

- [inql](https://github.com/doyensec/inql) - InQL - A Burp Extension for GraphQL Security Testing
- [GraphQLmap](https://github.com/swisskyrepo/GraphQLmap) - GraphQLmap is a scripting engine to interact with a graphql endpoint for pentesting purposes.
- [shapeshifter](https://github.com/szski/shapeshifter) - GraphQL security testing tool
- [graphql_beautifier](https://github.com/zidekmat/graphql_beautifier) - Burp Suite extension to help make Graphql request more readable

### JSON Web Token

Lorem ipsum dolor sit amet

- [jwt_tool](https://github.com/ticarpi/jwt_tool) - A toolkit for testing, tweaking and cracking JSON Web Tokens
- [c-jwt-cracker](https://github.com/brendan-rius/c-jwt-cracker) - JWT brute force cracker written in C
- [jwt-heartbreaker](https://github.com/wallarm/jwt-heartbreaker) - The Burp extension to check JWT (JSON Web Tokens) for using keys from known from public sources
- [jwtear](https://github.com/KINGSABRI/jwtear) - Modular command-line tool to parse, create and manipulate JWT tokens for hackers
- [jwt-key-id-injector](https://github.com/dariusztytko/jwt-key-id-injector) - Simple python script to check against hypothetical JWT vulnerability.

### postMessage

Lorem ipsum dolor sit amet

- [postMessage-tracker](https://github.com/fransr/postMessage-tracker) - A Chrome Extension to track postMessage usage (url, domain and stack) both by logging using CORS and also visually as an extension-icon
- [PostMessage_Fuzz_Tool](https://github.com/kiranreddyrebel/PostMessage_Fuzz_Tool) - #BugBounty #BugBounty Tools #WebDeveloper Tool

### Server Side Request Forgery

Lorem ipsum dolor sit amet

- [SSRFmap](https://github.com/swisskyrepo/SSRFmap) - Automatic SSRF fuzzer and exploitation tool
- [Gopherus](https://github.com/tarunkant/Gopherus) - This tool generates gopher link for exploiting SSRF and gaining RCE in various servers
- [ground-control](https://github.com/jobertabma/ground-control) - A collection of scripts that run on my web server. Mainly for debugging SSRF, blind XSS, and XXE vulnerabilities.
- [Gf-Patterns](https://github.com/1ndianl33t/Gf-Patterns) - GF Paterns For (ssrf,RCE,Lfi,sqli,ssti,idor,url redirection,debug_logic, interesting Subs) parameters grep
- [SSRFire](https://github.com/micha3lb3n/SSRFire) - An automated SSRF finder. Just give the domain name and your server and chill! ;) Also has options to find XSS and open redirects
- [httprebind](https://github.com/daeken/httprebind) - Automatic tool for DNS rebinding-based SSRF attacks
- [ssrf-sheriff](https://github.com/teknogeek/ssrf-sheriff) - A simple SSRF-testing sheriff written in Go
- [B-XSSRF](https://github.com/SpiderMate/B-XSSRF) - Toolkit to detect and keep track on Blind XSS, XXE & SSRF
- [extended-ssrf-search](https://github.com/Damian89/extended-ssrf-search) - Smart ssrf scanner using different methods like parameter brute forcing in post and get...
- [gaussrf](https://github.com/KathanP19/gaussrf) - Fetch known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and Common Crawl and Filter Urls With OpenRedirection or SSRF Parameters.
- [ssrfDetector](https://github.com/JacobReynolds/ssrfDetector) - Server-side request forgery detector
- [grafana-ssrf](https://github.com/RandomRobbieBF/grafana-ssrf) - Authenticated SSRF in Grafana
- [sentrySSRF](https://github.com/xawdxawdx/sentrySSRF) - Tool to searching sentry config on page or in javascript files and check blind SSRF

### SQL Injection

Lorem ipsum dolor sit amet

- [sqlmap](https://github.com/sqlmapproject/sqlmap) - Automatic SQL injection and database takeover tool
- [NoSQLMap](https://github.com/codingo/NoSQLMap) - Automated NoSQL database enumeration and web application exploitation tool.
- [SQLiScanner](https://github.com/0xbug/SQLiScanner) - Automatic SQL injection with Charles and sqlmap api
- [SleuthQL](https://github.com/RhinoSecurityLabs/SleuthQL) - Python3 Burp History parsing tool to discover potential SQL injection points. To be used in tandem with SQLmap.
- [mssqlproxy](https://github.com/blackarrowsec/mssqlproxy) - mssqlproxy is a toolkit aimed to perform lateral movement in restricted environments through a compromised Microsoft SQL Server via socket reuse
- [sqli-hunter](https://github.com/zt2/sqli-hunter) - SQLi-Hunter is a simple HTTP / HTTPS proxy server and a SQLMAP API wrapper that makes digging SQLi easy.
- [waybackSqliScanner](https://github.com/ghostlulzhacks/waybackSqliScanner) - Gather urls from wayback machine then test each GET parameter for sql injection.
- [ESC](https://github.com/NetSPI/ESC) - Evil SQL Client (ESC) is an interactive .NET SQL console client with enhanced SQL Server discovery, access, and data exfiltration features.
- [mssqli-duet](https://github.com/Keramas/mssqli-duet) - SQL injection script for MSSQL that extracts domain users from an Active Directory environment based on RID bruteforcing
- [burp-to-sqlmap](https://github.com/Miladkhoshdel/burp-to-sqlmap) - Performing SQLInjection test on Burp Suite Bulk Requests using SQLMap
- [BurpSQLTruncSanner](https://github.com/InitRoot/BurpSQLTruncSanner) - Messy BurpSuite plugin for SQL Truncation vulnerabilities.
- [andor](https://github.com/sadicann/andor) - Blind SQL Injection Tool with Golang
- [Blinder](https://github.com/mhaskar/Blinder) - A python library to automate time-based blind SQL injection

### XXE Injection

Lorem ipsum dolor sit amet

- [ground-control](https://github.com/jobertabma/ground-control) - A collection of scripts that run on my web server. Mainly for debugging SSRF, blind XSS, and XXE vulnerabilities.
- [dtd-finder](https://github.com/GoSecure/dtd-finder) - List DTDs and generate XXE payloads using those local DTDs.
- [docem](https://github.com/whitel1st/docem) - Uility to embed XXE and XSS payloads in docx,odt,pptx,etc (OXML_XEE on steroids)
- [xxeserv](https://github.com/staaldraad/xxeserv) - A mini webserver with FTP support for XXE payloads
- [xxexploiter](https://github.com/luisfontes19/xxexploiter) - Tool to help exploit XXE vulnerabilities
- [B-XSSRF](https://github.com/SpiderMate/B-XSSRF) - Toolkit to detect and keep track on Blind XSS, XXE & SSRF
- [XXEinjector](https://github.com/enjoiz/XXEinjector) - Tool for automatic exploitation of XXE vulnerability using direct and different out of band methods.
- [oxml_xxe](https://github.com/BuffaloWill/oxml_xxe) - A tool for embedding XXE/XML exploits into different filetypes


## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.


## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, vavkamil has waived all copyright and
related or neighboring rights to this work.
