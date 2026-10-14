package com.learnhub.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.learnhub.dto.AuthResponse;
import com.learnhub.dto.LoginRequest;
import com.learnhub.dto.RegisterRequest;
import com.learnhub.dto.UserSummaryResponse;
import com.learnhub.entity.Role;
import com.learnhub.service.AuthService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import java.time.LocalDateTime;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

class AuthControllerTest {

    private MockMvc mockMvc;
    private ObjectMapper objectMapper;
    private StubAuthService stubAuthService;

    static class StubAuthService extends AuthService {
        private AuthResponse registerResponse;
        private AuthResponse loginResponse;

        public StubAuthService() {
            super(null, null, null, null);
        }

        public void setRegisterResponse(AuthResponse registerResponse) {
            this.registerResponse = registerResponse;
        }

        public void setLoginResponse(AuthResponse loginResponse) {
            this.loginResponse = loginResponse;
        }

        @Override
        public AuthResponse register(RegisterRequest request) {
            return registerResponse;
        }

        @Override
        public AuthResponse login(LoginRequest request) {
            return loginResponse;
        }
    }

    @BeforeEach
    void setUp() {
        objectMapper = new ObjectMapper();
        stubAuthService = new StubAuthService();
        mockMvc = MockMvcBuilders.standaloneSetup(new AuthController(stubAuthService)).build();
    }

    @Test
    @DisplayName("POST /api/auth/register with valid request returns 201 and token")
    void testRegisterSuccess() throws Exception {
        RegisterRequest request = new RegisterRequest(
                "harshith",
                "harshith@example.com",
                "Password123",
                "Harshith Kumar",
                Role.ROLE_STUDENT
        );

        UserSummaryResponse userSummary = new UserSummaryResponse(
                1L,
                "harshith",
                "harshith@example.com",
                "Harshith Kumar",
                Role.ROLE_STUDENT,
                null,
                null,
                LocalDateTime.now()
        );

        AuthResponse authResponse = new AuthResponse("mock-jwt-token", 86400000L, userSummary);
        stubAuthService.setRegisterResponse(authResponse);

        mockMvc.perform(post("/api/auth/register")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(request)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.success").value(true))
                .andExpect(jsonPath("$.data.token").value("mock-jwt-token"))
                .andExpect(jsonPath("$.data.user.username").value("harshith"));
    }

    @Test
    @DisplayName("POST /api/auth/login with valid request returns 200 and token")
    void testLoginSuccess() throws Exception {
        LoginRequest request = new LoginRequest("harshith", "Password123");

        UserSummaryResponse userSummary = new UserSummaryResponse(
                1L,
                "harshith",
                "harshith@example.com",
                "Harshith Kumar",
                Role.ROLE_STUDENT,
                null,
                null,
                LocalDateTime.now()
        );

        AuthResponse authResponse = new AuthResponse("mock-jwt-token", 86400000L, userSummary);
        stubAuthService.setLoginResponse(authResponse);

        mockMvc.perform(post("/api/auth/login")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(request)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.success").value(true))
                .andExpect(jsonPath("$.data.token").value("mock-jwt-token"))
                .andExpect(jsonPath("$.data.user.email").value("harshith@example.com"));
    }

    @Test
    @DisplayName("GET /api/auth/roles returns 200 and available roles")
    void testGetRoles() throws Exception {
        mockMvc.perform(get("/api/auth/roles"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.success").value(true))
                .andExpect(jsonPath("$.data[0]").value("ROLE_STUDENT"))
                .andExpect(jsonPath("$.data[1]").value("ROLE_INSTRUCTOR"));
    }
}
