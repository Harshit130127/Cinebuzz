# CineBuzz- Django REST API 

This project is part of my learning journey while following a Django REST Framework course.  
I’m building a complete backend step-by-step, covering core DRF concepts, authentication systems, and API design.

---

## Progress Covered So Far

### ✔ Django + DRF Basics
- Setting up Django project & apps  
- Models and migrations  
- Returning JSON responses  
- Introduction to DRF  
- Browsable API basics  

### ✔ Serializers
- Basic serializers  
- Handling GET, POST, PUT, DELETE  
- Validation  
- Serializer fields & arguments  
- ModelSerializer  
- Custom serializer fields  
- Updating models  

### ✔ DRF Views
- APIView  
- GenericAPIView + Mixins  
- Concrete view classes  
- Viewsets  
- Routers  
- ModelViewSet  
- URL structure and routing  

### ✔ Relationships & Nested Data
- Django model relationships  
- Nested serializers  
- Serializer relations  
- Hyperlinked serializers  

### ✔ Authentication (Before JWT)
- Basic Authentication  
- Session Authentication  
- Token Authentication (DRF TokenAuth)  
- Login, logout, registration flow  

---

##  Completed: JWT Authentication Module

Recently completed the full JWT section of the course.

### Features implemented:
- Login & registration endpoints  
- Access + Refresh token generation  
- Token verification endpoint  
- Blacklist support for secure logout  
- Serializer validation for auth inputs  
- Used both APIView and ViewSet patterns  
- Protected endpoints using `IsAuthenticated`  
- Tested all endpoints using Postman  
- Handled invalid and expired tokens  

---

## Throttling (Rate Limiting)

Added DRF throttling to control request frequency and prevent abuse.

- Enabled global throttling  
  - `AnonRateThrottle` (e.g., 3/day for anonymous users)  
  - `UserRateThrottle` (e.g., 10/day for authenticated users)

- Added scoped throttling for specific endpoints  
  - Example: reviews API using `ScopedRateThrottle`

- Implemented basic custom throttle classes for fine-grained per-view limits


## Filtering, Search & Ordering

- Added filtering using `DjangoFilterBackend`
- Added search support using `SearchFilter`
- Added ordering using `OrderingFilter`
- Configured `filterset_fields`, `search_fields`, and `ordering_fields`
- Implemented a custom `FilterSet` for advanced filters


## Pagination Methods

- Implemented PageNumber, LimitOffset, and Cursor pagination
- Added custom pagination class with adjustable page size
- Configured global pagination settings in DRF
- Tested pagination responses in Browsable API and Postman
- Learned how to switch Browsable API to JSON-only output


##  Next Topics (Upcoming Modules)
- API test cases  
- Deployment  


---

##  Tech Stack
- Python  
- Django  
- Django REST Framework  
- SimpleJWT  
- SQLite (development)  
- Postman  
- Git & GitHub  

---

##  Goal
To fully understand backend fundamentals, build clean API structures, and prepare for backend roles using Python/Django in 2026.
