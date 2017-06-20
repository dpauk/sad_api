This API is very sad.  No-one has given it any security love and it's feeling all vulnerable.  It really hopes that you aren't go to try and break it.

This is an intentionally vulnerable API that can be used to learn techniques for finding vulnerabilities within APIs.

Potential flaws:
* API key enumeration
* Cross-site Request Forgery
* Horizontal privilege escalation
* Lack of input validation
* Lack of validation of incoming content-types
* Lack of whitelisting of allowable HTTP methods
* SQL injection
* Vertical privilege escalation
* XXE


This is based on vulnerabilites defined at:
* [OWASP REST Security Cheat Sheet](https://www.owasp.org/index.php/REST_Security_Cheat_Sheet)
