# CineBuzz: Robust Django REST API 

A comprehensive, production-ready backend project built with Django REST Framework (DRF), designed to demonstrate mastery of core API development principles, authentication, authorization, and advanced optimization techniques.

##  Project Goal

To master modern backend fundamentals using **Python/Django**, build clean, maintainable API structures, and prepare for professional backend engineering roles.

---

## Key Architectural Features

This project implements all critical components required for a secure and scalable REST API:

### Security & Access Control

* **JSON Web Token (JWT) Authentication:** Implemented full authentication flow using **Django SimpleJWT** for stateless security.
    * **Features:** Login, Registration, **Access** & **Refresh** token generation, Token verification, and **Blacklist** support for secure logout.
* **Permissions System:** Protected all endpoints using DRF's built-in permissions.
    * `IsAuthenticated`: Ensures only logged-in users can access resources.
    * **Custom Permissions:** Implemented granular object-level permissions (e.g., `IsReviewUserOrReadOnly`, `IsAdminOrReadOnly`).

### Rate Limiting & Throttling

Advanced control over request frequency to prevent abuse and ensure fair access.
* **Global Limits:** Implemented `AnonRateThrottle` (anonymous users) and `UserRateThrottle` (authenticated users).
* **Scoped Throttling:** Used `ScopedRateThrottle` to enforce unique, view-specific limits (e.g., 5 requests per minute on review creation).
* **Custom Classes:** Developed custom throttling classes for fine-grained control.

### Optimization & Data Handling

* **Filtering & Searching:** Enabled advanced data discovery across endpoints.
    * **Filtering:** Utilized `DjangoFilterBackend` with custom `FilterSet` classes.
    * **Search:** Integrated `SearchFilter` (e.g., searching WatchLists by title/description).
    * **Ordering:** Enabled dynamic result sorting using `OrderingFilter`.
* **Pagination:** Implemented three distinct pagination methods for efficient data transfer and client-side handling:
    * `PageNumberPagination`
    * `LimitOffsetPagination`
    * `CursorPagination` (for fast, consistent ordering).
* **Data Relationships:** Handled complex **many-to-many** and **one-to-many** model relationships using nested and Hyperlinked serializers.

---

## Core DRF Implementation

| Concept | Implementation Details |
| :--- | :--- |
| **Views** | Full coverage of **APIView**, **GenericAPIView + Mixins**, **Concrete View Classes**, **ViewSets**, and **ModelViewSets** using Routers. |
| **Serializers** | Mastery of `ModelSerializer`, custom fields, advanced validation logic, and handling the full **GET/POST/PUT/DELETE** lifecycle. |
| **Testing** | Comprehensive **API Test Suite** using DRF's `APITestCase`. Full coverage for authentication, permissions, CRUD operations, and edge-case behavior (e.g., duplicate review prevention). |

---

## Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Backend** | Python, Django, **Django REST Framework (DRF)** |
| **Auth** | **SimpleJWT** |
| **Database** | SQLite (Development) |
| **Tools** | Postman, Git, GitHub |