# Multi-stage Dockerfile for LearnHub Spring Boot Backend
# Optimized for cloud deployment (Render, Railway, Fly.io) with low memory footprint

# --- Build Stage ---
FROM maven:3.9.6-eclipse-temurin-17-alpine AS build
WORKDIR /app

# Cache Maven dependencies
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Copy source code and build production jar
COPY src ./src
RUN mvn clean package -DskipTests -B

# --- Production Runtime Stage ---
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app

# Create a non-privileged system user for security
RUN addgroup -S learnhub && adduser -S learnhub -G learnhub
USER learnhub

# Copy the built JAR from builder stage
COPY --from=build --chown=learnhub:learnhub /app/target/*.jar app.jar

# Dynamic PORT environment variable (Render sets PORT, defaults to 8080)
ENV PORT=8080
EXPOSE 8080

# Java options: constrained memory to fit cleanly inside Render's 512MB free tier
ENTRYPOINT ["sh", "-c", "java -XX:+UseContainerSupport -XX:MaxRAMPercentage=75.0 -Xmx384m -Xms128m -Djava.security.egd=file:/dev/./urandom -jar app.jar"]
