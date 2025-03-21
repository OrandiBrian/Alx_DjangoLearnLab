# Security Best Practices for LibraryProject

## 1. Django Settings
- DEBUG is disabled in production.
- CSRF and session cookies are set to secure.
- HSTS is enabled for HTTPS enforcement.

## 2. Views Protection
- CSRF protection is enforced using `{% csrf_token %}`.
- User inputs are sanitized through Django Forms.
- ORM queries are used instead of raw SQL.

## 3. Content Security Policy (CSP)
- External scripts are blocked unless whitelisted.
- Only trusted styles and fonts are allowed.