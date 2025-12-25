# API Reference Documentation Standards

## Page Structure

Every API endpoint page must include these sections in order:

1. Endpoint overview with HTTP method and path
2. Description
3. Authentication requirements
4. Parameters (Path, Query, Headers, Body)
5. Code examples
6. Response format
7. Error responses

## Endpoint Title

Format: `[HTTP Method] [Endpoint Path]`

```markdown
## POST /api/v1/users

Creates a new user account with the provided information.
```

## Authentication

State authentication requirements clearly at the top:

```markdown
<Info>
  Requires authentication with API key in header
</Info>
```

## Parameters

### Structure Parameters by Type

Group parameters into clear sections:

```markdown
## Parameters

### Path Parameters

| Parameter | Type   | Required | Description                    |
| --------- | ------ | -------- | ------------------------------ |
| `userId`  | string | Yes      | Unique identifier for the user |

### Query Parameters

| Parameter | Type    | Required | Description                             |
| --------- | ------- | -------- | --------------------------------------- |
| `limit`   | integer | No       | Maximum number of results (default: 10) |
| `offset`  | integer | No       | Number of results to skip (default: 0)  |

### Headers

| Header          | Type   | Required | Description                     |
| --------------- | ------ | -------- | ------------------------------- |
| `Authorization` | string | Yes      | Bearer token for authentication |
| `Content-Type`  | string | Yes      | Must be `application/json`      |

### Body Parameters

| Parameter | Type   | Required | Description                 |
| --------- | ------ | -------- | --------------------------- |
| `email`   | string | Yes      | User's email address        |
| `name`    | string | Yes      | User's full name            |
| `role`    | string | No       | User role (default: "user") |
```

### Parameter Details

For each parameter include:

- Clear, descriptive name
- Data type (string, integer, boolean, object, array)
- Whether required or optional
- Brief description including defaults, constraints, or format requirements

For complex nested objects, show the structure:

```markdown
### Body Parameters

| Parameter          | Type   | Required | Description                    |
| ------------------ | ------ | -------- | ------------------------------ |
| `user`             | object | Yes      | User information object        |
| `user.email`       | string | Yes      | User's email address           |
| `user.profile`     | object | No       | Optional profile information   |
| `user.profile.bio` | string | No       | User biography (max 500 chars) |
```

## Code Examples

Use tabs to show multiple languages. Always include these common formats:

````markdown
<CodeGroup>

```bash cURL
curl -X POST https://api.example.com/v1/users \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "name": "John Doe",
    "role": "admin"
  }'
```
````

```python Python
import requests

url = "https://api.example.com/v1/users"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "email": "user@example.com",
    "name": "John Doe",
    "role": "admin"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

```javascript JavaScript
const response = await fetch("https://api.example.com/v1/users", {
    method: "POST",
    headers: {
        Authorization: "Bearer YOUR_API_KEY",
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        email: "user@example.com",
        name: "John Doe",
        role: "admin",
    }),
});

const data = await response.json();
console.log(data);
```

</CodeGroup>
```

**Code Example Guidelines:**

- Use realistic, working examples
- Replace sensitive values with placeholders (YOUR_API_KEY)
- Show complete requests including all headers
- Use consistent example data across languages

## Response Format

### Success Response

Show the successful response with status code and structure:

````markdown
## Response

### Success Response (200 OK)

```json
{
    "id": "usr_1234567890",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "admin",
    "createdAt": "2024-01-15T10:30:00Z",
    "status": "active"
}
```
````

**Response Fields:**

| Field       | Type   | Description                                 |
| ----------- | ------ | ------------------------------------------- |
| `id`        | string | Unique user identifier                      |
| `email`     | string | User's email address                        |
| `name`      | string | User's full name                            |
| `role`      | string | Assigned user role                          |
| `createdAt` | string | ISO 8601 timestamp of creation              |
| `status`    | string | Account status (active, suspended, deleted) |

````

### Error Responses

Document all possible error scenarios:

```markdown
## Error Responses

### 400 Bad Request

Returned when request parameters are invalid.

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Invalid email format",
    "field": "email"
  }
}
````

### 401 Unauthorized

Returned when authentication fails or token is missing.

```json
{
    "error": {
        "code": "UNAUTHORIZED",
        "message": "Invalid or missing API key"
    }
}
```

### 409 Conflict

Returned when the email already exists.

```json
{
    "error": {
        "code": "DUPLICATE_EMAIL",
        "message": "A user with this email already exists"
    }
}
```

### 429 Too Many Requests

Returned when rate limit is exceeded.

```json
{
    "error": {
        "code": "RATE_LIMIT_EXCEEDED",
        "message": "Too many requests. Retry after 60 seconds.",
        "retryAfter": 60
    }
}
```

### 500 Internal Server Error

Returned when an unexpected server error occurs.

```json
{
    "error": {
        "code": "INTERNAL_ERROR",
        "message": "An unexpected error occurred. Please try again later."
    }
}
```

````

**Error Documentation Guidelines:**
- Include all HTTP status codes the endpoint can return
- Show the exact error response structure
- Explain what causes each error
- Include any relevant error codes or fields

## Response Field Documentation

For every field in the response, document:
- Field name and type
- Clear description of what it represents
- Possible values (for enums)
- Format requirements (for dates, IDs, etc.)
- Whether the field is always present or conditional

## Additional Sections

### Rate Limiting

If applicable, document rate limits:

```markdown
## Rate Limiting

This endpoint is rate limited to 100 requests per minute per API key.

Rate limit headers are included in all responses:
- `X-RateLimit-Limit`: Maximum requests per window
- `X-RateLimit-Remaining`: Remaining requests in current window
- `X-RateLimit-Reset`: Unix timestamp when the window resets
````

### Pagination

For list endpoints, document pagination:

````markdown
## Pagination

Results are paginated using `limit` and `offset` parameters.

The response includes pagination metadata:

```json
{
  "data": [...],
  "pagination": {
    "total": 150,
    "limit": 10,
    "offset": 0,
    "hasMore": true
  }
}
```
````

````

### Webhooks

If the endpoint triggers webhooks, note this:

```markdown
<Info>
  This action triggers a `user.created` webhook event.
</Info>
````

## Writing Guidelines

**Do:**

- Use present tense ("Returns a list" not "Will return")
- Be specific about data types and formats
- Include realistic example values
- Document every possible response
- Test all code examples

**Don't:**

- Use vague descriptions ("some data")
- Skip error responses
- Assume knowledge of authentication
- Leave out required headers
- Use inconsistent naming between sections

## Consistency

Maintain consistency across all API reference pages:

- Use the same parameter table format
- Show code examples in the same order
- Use identical error response structure
- Follow the same section ordering
- Use consistent terminology for similar concepts
