# LearnHub – Skill Learning & Assessment Platform

A modern, full-stack web application designed for skill learning and comprehensive assessments. Built with **React.js + Vite** on the frontend and **Java + Spring Boot 3 + Maven** on the backend.

---

## 🛠️ Technology Stack

| Layer | Technology | Details |
|---|---|---|
| **Frontend** | React 19 + Vite | Fast HMR, component-driven UI architecture |
| **Backend** | Java 17+ / Spring Boot 3 | Modular layered enterprise REST API |
| **Build Tool** | Maven 3.9+ / Maven Wrapper | Dependency management & reproducible builds |
| **Database** | MySQL 8.0+ | Relational data persistence |
| **ORM** | Spring Data JPA + Hibernate | Entity lifecycle & declarative data access |
| **Validation** | Jakarta Bean Validation | REST request payload validation |
| **Dev Tools** | Spring Boot DevTools | Fast automatic restarts during development |

---

## 📂 Project Directory Structure

```text
LearnHub/
├── frontend/
│   ├── public/
│   │   └── favicon.svg
│   ├── src/
│   │   ├── assets/               # Static image & vector assets
│   │   ├── components/           # Reusable UI components (StatusBadge, TechCard)
│   │   ├── context/              # Context providers (ThemeContext)
│   │   ├── hooks/                # Custom React hooks (useHealthCheck)
│   │   ├── layouts/              # App layout wrappers (MainLayout)
│   │   ├── pages/                # Page views (LandingPage)
│   │   ├── routes/               # Routing declarations (AppRoutes)
│   │   ├── services/             # HTTP clients & API services (api.js)
│   │   ├── utils/                # Constants and helpers (constants.js)
│   │   ├── App.jsx               # Root application component
│   │   ├── index.css             # Design system styling & design tokens
│   │   └── main.jsx              # React DOM mounting entry point
│   ├── .env                      # Local frontend environment variables
│   ├── .env.example              # Frontend environment template
│   ├── index.html                # HTML template
│   ├── package.json              # Frontend npm dependencies and scripts
│   └── vite.config.js            # Vite bundler configuration
│
├── backend/
│   ├── .mvn/wrapper/             # Maven Wrapper files
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/learnhub/
│   │   │   │   ├── config/       # Global CORS & application configuration
│   │   │   │   ├── controller/   # REST API controllers (HealthController)
│   │   │   │   ├── dto/          # Data Transfer Objects (HealthCheckResponse, ApiResponse)
│   │   │   │   ├── entity/       # JPA entities (BaseEntity)
│   │   │   │   ├── exception/    # Custom exceptions & GlobalExceptionHandler
│   │   │   │   ├── repository/   # Spring Data JPA repositories
│   │   │   │   ├── service/      # Business logic services (HealthService)
│   │   │   │   └── LearnHubApplication.java # Spring Boot main entry point
│   │   │   └── resources/
│   │   │       └── application.properties   # Backend application configuration
│   │   └── test/
│   │       └── java/com/learnhub/
│   │           └── LearnHubApplicationTests.java # Context load test
│   ├── mvnw                      # Maven Wrapper script (Linux/macOS)
│   ├── mvnw.cmd                  # Maven Wrapper script (Windows)
│   └── pom.xml                   # Maven dependencies and build definition
│
├── .gitignore                    # Global Git ignore rules
└── README.md                     # Project documentation & setup instructions
```

---

## 🚀 Getting Started

### Prerequisites

- **Java Development Kit (JDK)**: Version 17 or higher
- **Node.js**: Version 18 or higher (with npm)
- **MySQL Server**: Version 8.0 or higher (optional for initial health check)
- **Git**

---

### 1. Backend Setup & Run

The backend is configured with the **Maven Wrapper (`mvnw` / `mvnw.cmd`)**, so you do not need Maven pre-installed.

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Run the Spring Boot application:
   - On **Windows**:
     ```powershell
     .\mvnw.cmd spring-boot:run
     ```
   - On **macOS / Linux**:
     ```bash
     ./mvnw spring-boot:run
     ```

3. The server starts on `http://localhost:8080`.
4. Test the health-check endpoint:
   - URL: `http://localhost:8080/api/health`
   - Expected HTTP Status: `200 OK`
   - Example Response:
     ```json
     {
       "status": "UP",
       "message": "LearnHub Skill Learning & Assessment Platform backend is running successfully.",
       "service": "learnhub-backend",
       "version": "0.0.1-SNAPSHOT",
       "timestamp": "2026-10-12T22:15:00"
     }
     ```

---

### 2. Frontend Setup & Run

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Copy the environment variables template (if not already copied):
   ```bash
   cp .env.example .env
   ```

3. Install frontend dependencies:
   ```bash
   npm install
   ```

4. Start the Vite development server:
   ```bash
   npm run dev
   ```

5. Open your browser and navigate to:
   ```text
   http://localhost:5173
   ```

The landing page will display real-time connectivity status with the backend on `http://localhost:8080/api/health`.

---

## 🗄️ MySQL Database Setup (Next Steps)

In this initial phase, the backend runs independently with `DataSourceAutoConfiguration` excluded so you can verify the service before configuring your local database.

To connect your local MySQL database:

1. **Log in to MySQL and create the database**:
   ```sql
   CREATE DATABASE learnhub_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

2. **Configure your credentials**:
   Set environment variables or edit `backend/src/main/resources/application.properties`:
   ```properties
   spring.datasource.url=jdbc:mysql://localhost:3306/learnhub_db?createDatabaseIfNotExist=true&useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true
   spring.datasource.username=root
   spring.datasource.password=YOUR_MYSQL_PASSWORD
   ```
   *(Or pass them as `DB_URL`, `DB_USERNAME`, `DB_PASSWORD` in your terminal environment).*

3. **Enable Data Source Auto-Configuration**:
   In `backend/src/main/resources/application.properties`, remove or comment out:
   ```properties
   # spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration,org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration
   ```

4. Restart the backend to activate Hibernate automatic schema creation and JPA repositories.

---

## 🔒 CORS Configuration

CORS is globally configured in `backend/src/main/java/com/learnhub/config/CorsConfig.java`. By default, it allows requests from:
- `http://localhost:5173` (Vite dev server)
- `http://localhost:3000`

Origins can be overridden via `cors.allowed-origins` in `application.properties` or through the `CORS_ALLOWED_ORIGINS` environment variable.

---

## 🧪 Verification Commands

| Command | Working Directory | Description |
|---|---|---|
| `.\mvnw.cmd compile` | `backend/` | Compiles Java backend code |
| `.\mvnw.cmd test` | `backend/` | Runs Spring Boot test suite |
| `.\mvnw.cmd spring-boot:run` | `backend/` | Starts backend server on port 8080 |
| `npm run build` | `frontend/` | Builds frontend production bundle |
| `npm run dev` | `frontend/` | Starts frontend development server |
